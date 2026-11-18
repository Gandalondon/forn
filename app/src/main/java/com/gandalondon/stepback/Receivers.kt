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
        if (event.geofenceTransition != Geofence.GEOFENCE_TRANSITION_ENTER) return
        val ids = event.triggeringGeofences.orEmpty().map { Fences.spotId(it.requestId) }
        Store(c).addPassed(Day.key(), ids)
    }
}

class NightReceiver : BroadcastReceiver() {
    override fun onReceive(c: Context, intent: Intent) = Night.run(c)
}

/** Geofences and alarms don't survive a restart or an update. Put them back. */
class BootReceiver : BroadcastReceiver() {
    override fun onReceive(c: Context, intent: Intent) {
        Fences.register(c)
        Night.schedule(c)
    }
}
