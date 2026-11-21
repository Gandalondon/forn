package com.gandalondon.stepback

import android.Manifest
import android.annotation.SuppressLint
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.location.Location
import android.os.Handler
import android.os.Looper
import androidx.core.content.ContextCompat
import com.google.android.gms.location.Geofence
import com.google.android.gms.location.GeofencingRequest
import com.google.android.gms.location.LocationServices
import com.google.android.gms.location.Priority
import com.google.android.gms.tasks.CancellationTokenSource

/** Geofences around the nearest spots not yet told. Android logs the crossing; no GPS track is kept. */
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

    /** Request id of the one ring that isn't a place: leave it and the nearest zones are picked again. */
    const val REFRESH = "__refresh"
    private const val MAX = 100 // Android's limit per app.

    /** Where you are now, or null. Fresh fix if Android gives one in time, else the last known one. */
    @SuppressLint("MissingPermission")
    fun here(c: Context, then: (Location?) -> Unit) {
        if (!hasLocation(c)) { then(null); return }
        val client = LocationServices.getFusedLocationProviderClient(c)
        var answered = false
        fun answer(l: Location?) { if (!answered) { answered = true; then(l) } }
        val cancel = CancellationTokenSource()
        Handler(Looper.getMainLooper()).postDelayed({
            if (!answered) { cancel.cancel(); client.lastLocation.addOnCompleteListener { answer(if (it.isSuccessful) it.result else null) } }
        }, 20_000)
        try {
            client.getCurrentLocation(Priority.PRIORITY_BALANCED_POWER_ACCURACY, cancel.token)
                .addOnCompleteListener { t ->
                    val l = if (t.isSuccessful) t.result else null
                    if (l != null) answer(l) else client.lastLocation.addOnCompleteListener { answer(if (it.isSuccessful) it.result else null) }
                }
        } catch (e: SecurityException) { answer(null) }
    }

    /**
     * The zone fix (21 Nov): Android's "already inside" trigger doesn't always fire, so build 46 missed places
     * Tony was standing in when the zones were set up, and at 9pm. Any untold zone that contains [l] counts
     * as passed for [day], at the time of the fix.
     */
    fun countInside(c: Context, l: Location, day: String, why: String) {
        if (System.currentTimeMillis() - l.time > 15 * 60_000L || l.accuracy > 200f) return // too old or too rough to trust
        val store = Store(c)
        val told = store.told
        val passed = store.passed(day)
        val inside = Spots.all(c).filter { s ->
            s.id !in told && s.id !in passed && s.points.any { p -> dist(l.latitude, l.longitude, p.lat, p.lng) <= p.radius }
        }
        if (inside.isEmpty()) return
        inside.forEach { store.addPassedAt(day, it.id, l.time) }
        TestLog.add(c, "inside $why: " + inside.joinToString(", ") { it.id } + "  at %.5f, %.5f (±%.0fm)".format(java.util.Locale.UK, l.latitude, l.longitude, l.accuracy))
    }

    private fun dist(aLat: Double, aLng: Double, bLat: Double, bLng: Double): Float {
        val r = FloatArray(1); Location.distanceBetween(aLat, aLng, bLat, bLng, r); return r[0]
    }

    /**
     * Watch the nearest untold zones (Android allows 100 per app; London alone has more). One of the 100 is a
     * ring around where you are now: leave it and the nearest are picked again. Before that, any zone you're
     * already standing in is counted for today.
     */
    fun register(c: Context) {
        if (!hasLocation(c) || !hasBackground(c)) return
        here(c) { l ->
            if (l != null) countInside(c, l, Day.key(), "when zones were set")
            add(c, l)
        }
    }

    @SuppressLint("MissingPermission")
    private fun add(c: Context, l: Location?) {
        val told = Store(c).told
        data class Z(val id: String, val pt: Point, val d: Float)
        val all = Spots.all(c).filter { it.id !in told }.flatMap { s ->
            s.points.mapIndexed { i, pt -> Z("${s.id}$SEP$i", pt, if (l == null) 0f else dist(l.latitude, l.longitude, pt.lat, pt.lng)) }
        }
        val needRefresh = l != null && all.size > MAX
        val near = (if (l == null) all else all.sortedBy { it.d }).take(if (needRefresh) MAX - 1 else MAX)
        val fences = near.map { z ->
            Geofence.Builder()
                .setRequestId(z.id)
                .setCircularRegion(z.pt.lat, z.pt.lng, z.pt.radius)
                .setExpirationDuration(Geofence.NEVER_EXPIRE)
                .setTransitionTypes(Geofence.GEOFENCE_TRANSITION_ENTER)
                .build()
        }.toMutableList()
        var refreshKm = 0f
        if (needRefresh && l != null) {
            // Half way to the furthest watched zone, so you're re-centred well before you reach the edge.
            val r = (near.last().d / 2f).coerceIn(1_000f, 30_000f)
            refreshKm = r / 1000f
            fences += Geofence.Builder()
                .setRequestId(REFRESH)
                .setCircularRegion(l.latitude, l.longitude, r)
                .setExpirationDuration(Geofence.NEVER_EXPIRE)
                .setTransitionTypes(Geofence.GEOFENCE_TRANSITION_EXIT)
                .build()
        }
        val client = LocationServices.getGeofencingClient(c)
        client.removeGeofences(intent(c)).addOnCompleteListener {
            if (fences.isEmpty()) { status(c, "No zones left to watch: every fact has been told."); return@addOnCompleteListener }
            client.addGeofences(
                GeofencingRequest.Builder()
                    // Fires straight away if you're already inside one (not always: countInside covers the misses).
                    .setInitialTrigger(GeofencingRequest.INITIAL_TRIGGER_ENTER)
                    .addGeofences(fences)
                    .build(),
                intent(c),
            )
                // Test aid (18 Nov): say whether Android accepted the zones, and why not if it didn't.
                .addOnSuccessListener {
                    val places = near.map { spotId(it.id) }.distinct().size
                    status(c, "Watching $places places" + (if (needRefresh) ", the nearest of ${all.size} zones, re-picked after %.1f km.".format(java.util.Locale.UK, refreshKm) else "."))
                }
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
