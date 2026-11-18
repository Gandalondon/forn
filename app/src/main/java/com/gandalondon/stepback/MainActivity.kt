package com.gandalondon.stepback

import android.Manifest
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.os.Build
import android.os.Bundle
import android.provider.Settings
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.core.content.ContextCompat

class MainActivity : ComponentActivity() {
    private var tick by mutableIntStateOf(0)
    private var openSpot by mutableStateOf<String?>(null)
    private var backgroundAsks = 0

    private val askLocation = registerForActivityResult(ActivityResultContracts.RequestMultiplePermissions()) { refresh() }
    private val askOne = registerForActivityResult(ActivityResultContracts.RequestPermission()) { refresh() }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        openSpot = intent.getStringExtra(Night.EXTRA_SPOT)
        setContent {
            Screen(tick) // tick changes whenever state on the phone may have changed
        }
    }

    override fun onNewIntent(intent: Intent) {
        super.onNewIntent(intent)
        openSpot = intent.getStringExtra(Night.EXTRA_SPOT) ?: openSpot
        tick++
    }

    override fun onResume() {
        super.onResume()
        refresh()
    }

    private fun refresh() {
        if (Fences.hasLocation(this) && Fences.hasBackground(this)) {
            Fences.register(this)
            Night.schedule(this)
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
        val hello = "Go about your day. Find out tonight."
        val store = Store(this)
        when {
            !Fences.hasLocation(this) -> Page(
                hello,
                "Stepback notes the old places you pass. At 9pm, one line about the best one. Your location never leaves your phone.",
                Choice("Allow location") {
                    askLocation.launch(arrayOf(Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_COARSE_LOCATION))
                },
            )

            !Fences.hasBackground(this) -> Page(
                hello,
                "To notice places while your phone's in your pocket, pick Allow all the time on the next screen.",
                Choice("Allow all the time") {
                    // After two refusals Android stops asking, so go straight to settings.
                    if (backgroundAsks++ < 2) askOne.launch(Manifest.permission.ACCESS_BACKGROUND_LOCATION)
                    else openAppSettings()
                },
            )

            !hasNotifications() -> Page(
                hello, "One quiet line at 9pm. Nothing else, ever.",
                Choice("Allow the 9pm line") {
                    if (Build.VERSION.SDK_INT >= 33) askOne.launch(Manifest.permission.POST_NOTIFICATIONS)
                },
            )

            else -> {
                val spot = (openSpot ?: store.history.firstOrNull())?.let { Spots.byId(this, it) }
                if (spot == null) {
                    val n = store.passed(Day.key()).size
                    Page(hello, if (n == 0) "Nothing yet today." else "So far today: $n ${if (n == 1) "place" else "places"}.")
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
