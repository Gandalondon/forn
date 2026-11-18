package com.gandalondon.stepback

import android.Manifest
import android.annotation.SuppressLint
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import androidx.core.content.ContextCompat
import com.google.android.gms.location.Geofence
import com.google.android.gms.location.GeofencingRequest
import com.google.android.gms.location.LocationServices

/** Geofences around each spot not yet told. Android logs the crossing; no GPS track is kept. */
object Fences {
    private const val SEP = "#"

    fun hasLocation(c: Context) = granted(c, Manifest.permission.ACCESS_FINE_LOCATION)
    fun hasBackground(c: Context) = granted(c, Manifest.permission.ACCESS_BACKGROUND_LOCATION)

    private fun granted(c: Context, perm: String) =
        ContextCompat.checkSelfPermission(c, perm) == PackageManager.PERMISSION_GRANTED

    private fun status(c: Context, s: String) {
        TestLog.add(c, s)
        c.getSharedPreferences("stepback", Context.MODE_PRIVATE).edit().putString("fence_status", s).apply()
    }

    fun status(c: Context): String = c.getSharedPreferences("stepback", Context.MODE_PRIVATE).getString("fence_status", "Zones not registered yet.")!!

    fun spotId(requestId: String) = requestId.substringBefore(SEP)

    private fun intent(c: Context): PendingIntent = PendingIntent.getBroadcast(
        c, 0, Intent(c, PassedReceiver::class.java),
        // Geofencing needs a mutable intent to attach the event.
        PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_MUTABLE,
    )

    @SuppressLint("MissingPermission")
    fun register(c: Context) {
        if (!hasLocation(c) || !hasBackground(c)) return
        val told = Store(c).told
        val fences = Spots.all(c).filter { it.id !in told }.flatMap { s ->
            s.points.mapIndexed { i, pt ->
                Geofence.Builder()
                    .setRequestId("${s.id}$SEP$i")
                    .setCircularRegion(pt.lat, pt.lng, pt.radius)
                    .setExpirationDuration(Geofence.NEVER_EXPIRE)
                    .setTransitionTypes(Geofence.GEOFENCE_TRANSITION_ENTER)
                    .build()
            }
        }.take(100) // Android's limit per app.
        val client = LocationServices.getGeofencingClient(c)
        client.removeGeofences(intent(c)).addOnCompleteListener {
            if (fences.isEmpty()) { status(c, "No zones left to watch: every fact has been told."); return@addOnCompleteListener }
            client.addGeofences(
                GeofencingRequest.Builder()
                    // Fires straight away if you're already inside one.
                    .setInitialTrigger(GeofencingRequest.INITIAL_TRIGGER_ENTER)
                    .addGeofences(fences)
                    .build(),
                intent(c),
            )
                // Test aid (18 Nov): say whether Android accepted the zones, and why not if it didn't.
                .addOnSuccessListener { status(c, "Watching ${fences.size} zones.") }
                .addOnFailureListener { e ->
                    val code = (e as? com.google.android.gms.common.api.ApiException)?.statusCode
                    val why = when (code) {
                        1000 -> "Android's zone service is off. Turn on Google Location Accuracy in Settings > Location > Location services."
                        1001 -> "Too many zones."
                        1004 -> "Location permission isn't set to Allow all the time."
                        else -> e.message ?: "unknown"
                    }
                    status(c, "Zones not working: $why (code $code)")
                }
        }
    }
}
