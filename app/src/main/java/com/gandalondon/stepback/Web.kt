package com.gandalondon.stepback

import android.annotation.SuppressLint
import android.content.Intent
import android.graphics.Color
import android.os.Handler
import android.os.Looper
import android.view.WindowInsets
import android.webkit.JavascriptInterface
import android.webkit.WebView
import android.widget.FrameLayout
import org.json.JSONArray
import org.json.JSONObject
import java.time.LocalDate
import java.time.LocalDateTime

/**
 * The app screen once set up (18 Nov): the rings with tonight's cards on top, as in the second browser prototype.
 * A WebView with the page, three.js and Instrument Sans bundled in assets/web, so it runs offline.
 * Like Hlid, Sniff and Relay, it's padded by the status and gesture bars.
 */
class Web(private val a: MainActivity) {
    val view = WebView(a)
    val root = FrameLayout(a)
    private val main = Handler(Looper.getMainLooper())
    var saved = ""

    @SuppressLint("SetJavaScriptEnabled")
    fun build(): FrameLayout {
        Store(a).dropAnswers()
        root.setBackgroundColor(Color.WHITE)
        view.setBackgroundColor(Color.WHITE)
        view.settings.javaScriptEnabled = true
        view.settings.domStorageEnabled = true
        @Suppress("DEPRECATION")
        view.settings.allowUniversalAccessFromFileURLs = true // the bundled font loads from a file:// page
        view.isVerticalScrollBarEnabled = false
        view.overScrollMode = WebView.OVER_SCROLL_NEVER
        view.addJavascriptInterface(Bridge(), "Forn")
        root.addView(view, FrameLayout.LayoutParams(FrameLayout.LayoutParams.MATCH_PARENT, FrameLayout.LayoutParams.MATCH_PARENT))
        root.setOnApplyWindowInsetsListener { v, insets ->
            if (android.os.Build.VERSION.SDK_INT >= 30) {
                val sys = insets.getInsets(WindowInsets.Type.systemBars() or WindowInsets.Type.displayCutout())
                v.setPadding(sys.left, sys.top, sys.right, sys.bottom)
            } else {
                @Suppress("DEPRECATION")
                v.setPadding(insets.systemWindowInsetLeft, insets.systemWindowInsetTop, insets.systemWindowInsetRight, insets.systemWindowInsetBottom)
            }
            insets
        }
        view.loadUrl("file:///android_asset/web/index.html")
        return root
    }

    fun refresh() = view.evaluateJavascript("window.forn&&forn.refresh()", null)

    /** The evening a fact belongs to: until noon, last night's rings are still today's. */
    private fun evening(): String {
        val now = LocalDateTime.now()
        return (if (now.hour < 12) LocalDate.now().minusDays(1) else LocalDate.now()).toString()
    }

    inner class Bridge {
        /** The build number (GitHub run number = versionCode), shown under About in How it works (22 Nov). */
        @JavascriptInterface
        fun build(): Long = a.packageManager.getPackageInfo(a.packageName, 0).longVersionCode

        @JavascriptInterface
        fun state(): String {
            val store = Store(a)
            val today = evening()
            val finds = JSONArray()
            val cards = JSONArray()
            val toldOn = HashMap<String, String>()
            store.history.forEach { id ->
                if (!store.hasToldDay(id)) return@forEach // told by the v1 app before dates were kept (sw20-clay): hidden, as Tony asked 19 Nov; stays told so it never repeats
                val s = Spots.byId(a, id) ?: return@forEach
                val day = store.toldDay(id)
                toldOn[id] = day
                finds.put(JSONObject()
                    .put("id", id).put("fact", s.fact).put("place", s.place).put("kind", s.kind)
                    .put("day", day).put("at", store.passedAt(day, id) ?: JSONObject.NULL))
                if (day == today && !store.seen(today)) cards.put(id) // tonight's cards wait on top until paged through
            }
            // Dust (22 Nov): every place passed leaves a pinch on that day's ring, by the time it was passed. Where a
            // place was uncovered that night, its dust became the ball, so it's left out on that day only.
            val dust = JSONArray()
            store.passedDays().forEach { day ->
                store.passed(day).forEach { id ->
                    if (toldOn[id] != day) dust.put(JSONObject().put("id", id).put("day", day).put("at", store.passedAt(day, id) ?: JSONObject.NULL))
                }
            }
            // Tonight's cards, best first (history is newest first, and the best was told last).
            val passedDay = Day.key()
            val passed = JSONArray()
            store.passed(passedDay).mapNotNull { Spots.byId(a, it) }.sortedBy { store.passedAt(passedDay, it.id) ?: 0L }.forEach {
                passed.put(JSONObject().put("id", it.id).put("place", it.place).put("at", store.passedAt(passedDay, it.id) ?: JSONObject.NULL))
            }
            return JSONObject()
                .put("today", today).put("finds", finds).put("cards", cards).put("dust", dust).put("passed", passed)
                .put("recording", TrackService.recording).put("saved", saved).put("fences", Fences.status(a))
                .toString()
        }

        /** Tonight's cards were paged through: they don't come back. */
        @JavascriptInterface
        fun seen(day: String) = Store(a).markSeen(day)

        @JavascriptInterface
        fun tellNow() = Night.run(a)

        /** Give feedback (25 Nov): an email to hello@getforn.app, with the build, phone and Android version filled in. */
        @JavascriptInterface
        fun feedback() = main.post {
            val b = a.packageManager.getPackageInfo(a.packageName, 0).longVersionCode
            val mail = Intent(Intent.ACTION_SENDTO, android.net.Uri.parse("mailto:hello@getforn.app"))
                .putExtra(Intent.EXTRA_SUBJECT, "Forn feedback, Version 0.1 ($b)")
                .putExtra(Intent.EXTRA_TEXT, "\n\n\nForn Version 0.1 ($b), ${android.os.Build.MANUFACTURER} ${android.os.Build.MODEL}, Android ${android.os.Build.VERSION.RELEASE}")
            runCatching { a.startActivity(mail) }.onFailure { TestLog.add(a, "Feedback: no email app (${it.message})") }
        }

        /** Privacy policy (25 Nov): getforn.app/privacy in the browser. */
        @JavascriptInterface
        fun privacy() = main.post { runCatching { a.startActivity(Intent(Intent.ACTION_VIEW, android.net.Uri.parse("https://getforn.app/privacy"))) } }

        /** Tell me more: hand a question to the app you pick (an AI, a search, notes). */
        @JavascriptInterface
        fun share(text: String) = main.post {
            val send = Intent(Intent.ACTION_SEND).setType("text/plain").putExtra(Intent.EXTRA_TEXT, text)
            a.startActivity(Intent.createChooser(send, "Tell me more"))
        }

        /**
         * Send my data (19 Nov): everything the app keeps, as one JSON file in Downloads/Forn, then the share menu
         * so Tony can email it to himself and hand it to Claude. Finds, places passed and when, zone status,
         * crash notes and the last of the events log. No recorded GPX routes.
         */
        @JavascriptInterface
        fun exportData() = main.post {
            runCatching {
                fun dump(name: String) = JSONObject().also { o ->
                    a.getSharedPreferences(name, android.content.Context.MODE_PRIVATE).all.forEach { (k, v) ->
                        o.put(k, if (v is Set<*>) JSONArray(v.toList()) else v ?: JSONObject.NULL)
                    }
                }
                val log = TestLog.read(a).lines().takeLast(800).joinToString("\n")
                val json = JSONObject()
                    .put("exported", LocalDateTime.now().toString())
                    .put("app", a.packageManager.getPackageInfo(a.packageName, 0).versionName)
                    .put("state", JSONObject(state()))
                    .put("store", dump("stepback")).put("crash", dump("stepback_crash"))
                    .put("events", log)
                val name = "forn-data-" + LocalDateTime.now().toString().take(16).replace(":", "") + ".json"
                val cv = android.content.ContentValues().apply {
                    put(android.provider.MediaStore.Downloads.DISPLAY_NAME, name)
                    put(android.provider.MediaStore.Downloads.MIME_TYPE, "application/json")
                    put(android.provider.MediaStore.Downloads.RELATIVE_PATH, android.os.Environment.DIRECTORY_DOWNLOADS + "/Forn")
                }
                val uri = a.contentResolver.insert(android.provider.MediaStore.Downloads.EXTERNAL_CONTENT_URI, cv)!!
                a.contentResolver.openOutputStream(uri)!!.use { it.write(json.toString(2).toByteArray()) }
                val send = Intent(Intent.ACTION_SEND).setType("application/json")
                    .putExtra(Intent.EXTRA_STREAM, uri).putExtra(Intent.EXTRA_SUBJECT, "Forn data")
                    .addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
                a.startActivity(Intent.createChooser(send, "Send my data"))
            }.onFailure { TestLog.add(a, "Export failed: ${it.message}") }
        }

        /** Test aid: start or stop recording a walk. */
        @JavascriptInterface
        fun record(): String {
            // Run on the main thread but wait for it, so the page reads the new state straight after (a second
            // tap used to stop the walk, because the label hadn't changed yet).
            val done = java.util.concurrent.CountDownLatch(1)
            main.post { try { toggleWalk() } finally { done.countDown() } }
            done.await(3, java.util.concurrent.TimeUnit.SECONDS)
            return ""
        }
    }

    /**
     * Test aid (18 Nov): go over the recorded route and count every zone it went through, in case Android's
     * geofencing missed one (likely in a car, through a tight zone). Uses the time of the first fix inside.
     */
    private fun crossCheck(fixes: List<DoubleArray>) {
        if (fixes.isEmpty()) return
        val store = Store(a)
        val d = FloatArray(1)
        Spots.all(a).forEach { s ->
            val hit = fixes.firstOrNull { f ->
                s.points.any { pt -> android.location.Location.distanceBetween(f[0], f[1], pt.lat, pt.lng, d); d[0] <= pt.radius }
            } ?: return@forEach
            val at = hit[4].toLong()
            val day = Day.key(java.time.LocalDateTime.ofInstant(java.time.Instant.ofEpochMilli(at), java.time.ZoneId.systemDefault()))
            val already = s.id in store.passed(day)
            store.addPassedAt(day, s.id, at)
            TestLog.add(a, "route went through ${s.id}" + if (already) " (zone had already fired)" else " (zone had NOT fired)")
        }
    }

    private fun toggleWalk() {
        val i = Intent(a, TrackService::class.java)
        if (!TrackService.recording) {
            a.startForegroundService(i)
            TrackService.startTrace("Forn walk")
            TestLog.add(a, "walk started")
            saved = ""
        } else {
            TestLog.add(a, "walk stopped")
            crossCheck(TrackService.fixes())
            val gpx = TrackService.endTrace(a)
            val log = TestLog.export(a)
            a.stopService(i)
            saved = listOf(gpx, log).filter { it.isNotBlank() }.joinToString(" and ")
        }
    }
}
