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
        val all = fences.filter { it.requestId != Fences.REFRESH }.map { Fences.spotId(it.requestId) }.distinct()
        if (all.isEmpty()) return
        val l = event.triggeringLocation
        val at = if (l != null) "  at %.5f, %.5f (±%.0fm)".format(java.util.Locale.UK, l.latitude, l.longitude, l.accuracy) else ""
        // Trust check (25 Nov): Tony was told Hounslow Heath on 24 Nov without going near it. Android can fire an
        // enter from a rough network fix (and the re-pick loop re-armed every zone every 4 minutes, giving it hundreds
        // of chances). Only count a spot when the fix is reasonably sharp and actually near one of its circles.
        val ids = if (l == null) all else {
            val spots = Spots.all(c).associateBy { it.id }
            all.filter { id ->
                val s = spots[id] ?: return@filter false
                l.accuracy <= 200f && s.points.any { p ->
                    val r = FloatArray(1); android.location.Location.distanceBetween(l.latitude, l.longitude, p.lat, p.lng, r)
                    r[0] <= p.radius + l.accuracy + 100f
                }
            }
        }
        if (ids.size < all.size) TestLog.add(c, "passed? " + (all - ids.toSet()).joinToString(", ") + at + ", ignored (fix too rough or too far away)")
        if (ids.isEmpty()) return
        Store(c).addPassed(Day.key(), ids)
        TestLog.add(c, "passed " + ids.joinToString(", ") + at)
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
