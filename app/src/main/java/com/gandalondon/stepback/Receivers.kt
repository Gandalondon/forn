package com.gandalondon.stepback

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import com.google.android.gms.location.Geofence
import com.google.android.gms.location.GeofencingEvent

/** Android tells us a spot was passed. We note the spot id for today, nothing else. */
class PassedReceiver : BroadcastReceiver() {
    override fun onReceive(c: Context, intent: Intent) {
        val event = GeofencingEvent.fromIntent(intent) ?: return
        if (event.hasError()) return
        val fences = event.triggeringGeofences.orEmpty()
        // Left the area the nearest zones were picked for: pick again around here (only 100 zones fit at once).
        // Only a real leave (22 Nov): see Fences.leftArea.
        if (fences.any { it.requestId == Fences.REFRESH } && event.geofenceTransition == Geofence.GEOFENCE_TRANSITION_EXIT) {
            if (Fences.leftArea(c, event.triggeringLocation)) Fences.register(c)
        }
        if (event.geofenceTransition != Geofence.GEOFENCE_TRANSITION_ENTER) return
        val ids = fences.filter { it.requestId != Fences.REFRESH }.map { Fences.spotId(it.requestId) }
        if (ids.isEmpty()) return
        Store(c).addPassed(Day.key(), ids)
        val l = event.triggeringLocation
        TestLog.add(c, "passed " + ids.joinToString(", ") + (if (l != null) "  at %.5f, %.5f (±%.0fm)".format(java.util.Locale.UK, l.latitude, l.longitude, l.accuracy) else ""))
    }
}

class NightReceiver : BroadcastReceiver() {
    override fun onReceive(c: Context, intent: Intent) {
        // Asking where you are takes a moment, so keep the receiver alive until tonight's finds are told.
        val pending = goAsync()
        Night.run(c) { pending.finish() }
    }
}

/** Geofences and alarms don't survive a restart or an update. Put them back. */
class BootReceiver : BroadcastReceiver() {
    override fun onReceive(c: Context, intent: Intent) {
        Fences.register(c)
        Night.schedule(c)
    }
}
