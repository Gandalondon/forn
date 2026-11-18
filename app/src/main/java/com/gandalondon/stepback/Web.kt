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
 * The app screen once set up (18 Nov): the rings with tonight's cards on top, as in Stepback prototype 2.
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
        @JavascriptInterface
        fun state(): String {
            val store = Store(a)
            val today = evening()
            val finds = JSONArray()
            val cards = JSONArray()
            store.history.forEach { id ->
                val s = Spots.byId(a, id) ?: return@forEach
                val day = store.toldDay(id)
                val v = store.verdict(id)
                finds.put(JSONObject()
                    .put("id", id).put("fact", s.fact).put("place", s.place).put("kind", s.kind)
                    .put("day", day).put("at", store.passedAt(day, id) ?: JSONObject.NULL)
                    .put("verdict", v ?: ""))
                if (day == today && v == null) cards.put(id)
            }
            // Tonight's cards, best first (history is newest first, and the best was told last).
            val passedDay = Day.key()
            val passed = JSONArray()
            store.passed(passedDay).mapNotNull { Spots.byId(a, it) }.sortedBy { store.passedAt(passedDay, it.id) ?: 0L }.forEach {
                passed.put(JSONObject().put("id", it.id).put("place", it.place).put("at", store.passedAt(passedDay, it.id) ?: JSONObject.NULL))
            }
            return JSONObject()
                .put("today", today).put("finds", finds).put("cards", cards).put("passed", passed)
                .put("recording", TrackService.recording).put("saved", saved)
                .toString()
        }

        @JavascriptInterface
        fun verdict(id: String, v: String) = Store(a).putVerdict(id, v.ifBlank { null })

        @JavascriptInterface
        fun tellNow() = Night.run(a)

        /** Tell me more: hand a question to the app you pick (an AI, a search, notes). */
        @JavascriptInterface
        fun share(text: String) = main.post {
            val send = Intent(Intent.ACTION_SEND).setType("text/plain").putExtra(Intent.EXTRA_TEXT, text)
            a.startActivity(Intent.createChooser(send, "Tell me more"))
        }

        /** Test aid: start or stop recording a walk. */
        @JavascriptInterface
        fun record(): String {
            main.post { toggleWalk() }
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
