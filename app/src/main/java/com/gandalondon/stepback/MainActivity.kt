package com.gandalondon.stepback

import android.Manifest
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.os.Build
import android.os.Bundle
import android.provider.Settings
import androidx.activity.ComponentActivity
import androidx.activity.SystemBarStyle
import androidx.activity.addCallback
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.runtime.getValue
import androidx.compose.runtime.key
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.core.content.ContextCompat

class MainActivity : ComponentActivity() {
    private var tick by mutableIntStateOf(0)
    private var openSpot by mutableStateOf<String?>(null)
    private var backgroundAsks = 0
    private var notifyAsks = 0

    private val askLocation = registerForActivityResult(ActivityResultContracts.RequestMultiplePermissions()) { refresh() }
    private val askOne = registerForActivityResult(ActivityResultContracts.RequestPermission()) { refresh() }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        Crash.install(this)
        // Android's back: close an open page or card in the rings first, otherwise leave the app.
        onBackPressedDispatcher.addCallback(this) {
            val w = web
            if (w == null) { isEnabled = false; onBackPressedDispatcher.onBackPressed(); isEnabled = true; return@addCallback }
            w.view.evaluateJavascript("(window.forn&&forn.back())?1:0") { r ->
                if (r != "1") { isEnabled = false; onBackPressedDispatcher.onBackPressed(); isEnabled = true }
            }
        }
        // White app: dark status and navigation icons.
        enableEdgeToEdge(
            statusBarStyle = SystemBarStyle.light(android.graphics.Color.TRANSPARENT, android.graphics.Color.TRANSPARENT),
            navigationBarStyle = SystemBarStyle.light(android.graphics.Color.TRANSPARENT, android.graphics.Color.TRANSPARENT),
        )
        openSpot = intent.getStringExtra(Night.EXTRA_SPOT)
        setContent {
            // tick changes whenever state on the phone may have changed (a permission granted, an answer tapped).
            // key() rebuilds the screen on every change: Compose was skipping Screen because it never read tick,
            // so setup only moved on after a restart (fixed 18 Nov).
            key(tick) { Screen(tick) }
        }
    }

    override fun onNewIntent(intent: Intent) {
        super.onNewIntent(intent)
        openSpot = intent.getStringExtra(Night.EXTRA_SPOT) ?: openSpot
        web?.refresh()
        tick++
    }

    override fun onResume() {
        super.onResume()
        refresh()
    }

    private var web: Web? = null

    private fun refresh() {
        if (Fences.hasLocation(this) && Fences.hasBackground(this)) {
            Fences.register(this)
            Night.schedule(this)
        }
        // Set up: from here the app is the rings (Web), with tonight's cards on top.
        if (Fences.hasLocation(this) && Fences.hasBackground(this) && hasNotifications() && Crash.last(this) == null) {
            web?.refresh() ?: Web(this).also { web = it; setContentView(it.build()) }
        }
        tick++
    }

    private var saved: String? = null

    private fun toggleWalk() {
        val i = Intent(this, TrackService::class.java)
        if (!TrackService.recording) {
            startForegroundService(i)
            TrackService.startTrace("Forn walk")
            TestLog.add(this, "walk started")
            saved = null
        } else {
            TestLog.add(this, "walk stopped")
            val gpx = TrackService.endTrace(this)
            val log = TestLog.export(this)
            stopService(i)
            saved = listOf(gpx, log).filter { it.isNotBlank() }.joinToString(" and ")
        }
        tick++
    }

    private fun hasNotifications() = Build.VERSION.SDK_INT < 33 ||
        ContextCompat.checkSelfPermission(this, Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED

    private fun openAppSettings() = startActivity(
        Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS, Uri.fromParts("package", packageName, null)),
    )

    @androidx.compose.runtime.Composable
    private fun Screen(@Suppress("UNUSED_PARAMETER") version: Int) {
        val store = Store(this)
        val crash = Crash.last(this)
        when {
            // Test aid: if the app crashed, show what happened so Tony can screenshot it.
            crash != null -> Page(
                "Forn crashed last time.",
                crash.take(700),
                Choice("Carry on") { Crash.clear(this); tick++ },
            )

            // Setup: one ask per screen, each with its own headline, so it's clear you've moved on.
            !Fences.hasLocation(this) -> Page(
                "Go about your day. Find out tonight.",
                "Forn notices the old places you pass. At 9pm, it tells you the best of them. Your location never leaves your phone.",
                Choice("Allow location") {
                    askLocation.launch(arrayOf(Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_COARSE_LOCATION))
                },
            )

            !Fences.hasBackground(this) -> Page(
                "Now pick Allow all the time.",
                "So it notices places with your phone in your pocket. Android opens the location setting: choose Allow all the time, then come back.",
                Choice("Allow all the time") {
                    // After two refusals Android stops asking, so go straight to the app's settings.
                    if (backgroundAsks++ < 2) askOne.launch(Manifest.permission.ACCESS_BACKGROUND_LOCATION)
                    else openAppSettings()
                },
            )

            !hasNotifications() -> Page(
                "One quiet moment at 9pm.",
                "A notification with the best place you passed today. Nothing else, ever.",
                Choice("Allow notifications") {
                    // Same as above: once Android stops asking, the button opens the app's settings instead of doing nothing.
                    if (Build.VERSION.SDK_INT >= 33 && notifyAsks++ < 2) askOne.launch(Manifest.permission.POST_NOTIFICATIONS)
                    else openAppSettings()
                },
            )

            else -> {
                val spot = (openSpot ?: store.history.firstOrNull())?.let { Spots.byId(this, it) }
                if (spot == null) {
                    val n = store.passed(Day.key()).size
                    // Set up and waiting: say so plainly.
                    Page(
                        if (TrackService.recording) "Recording your walk." else "Enjoy your day.",
                        saved?.let { if (it.isBlank()) "Nothing was recorded." else "Saved to $it." } ?: if (n == 0) "You're all set. Forn will tell you what you passed at 9pm." else "You're all set. So far today: $n ${if (n == 1) "place" else "places"}. Find out what at 9pm.",
                        // Test aid (18 Nov): run tonight's 9pm line now, notification and all. Remove after testing.
                        // Test aids (18 Nov): Record walk saves a GPX track and the zone log to Downloads/Forn.
                        Choice(if (TrackService.recording) "Stop and save" else "Record walk") { toggleWalk() },
                        *(if (n > 0) arrayOf(Choice("Tell me now") { Night.run(this) { tick++ } }) else emptyArray()),
                    )
                } else {
                    val verdict = store.verdict(spot.id)
                    Page(
                        spot.fact, spot.place,
                        Choice("Interesting", filled = verdict == Store.YES) { store.setVerdict(spot.id, Store.YES); tick++ },
                        Choice("Not for me", filled = verdict == Store.NO) { store.setVerdict(spot.id, Store.NO); tick++ },
                    )
                }
            }
        }
    }
}
