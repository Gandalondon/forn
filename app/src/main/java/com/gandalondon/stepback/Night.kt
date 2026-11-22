package com.gandalondon.stepback

import android.annotation.SuppressLint
import android.app.AlarmManager
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import androidx.core.app.NotificationCompat
import androidx.core.app.NotificationManagerCompat
import java.time.LocalDate
import java.time.LocalDateTime
import java.time.ZoneId

/** One line at 9pm: the best of the day, never a list. Quiet day, no ping. */
object Night {
    private const val CHANNEL = "tonight"
    const val EXTRA_SPOT = "spot"

    fun schedule(c: Context) {
        val now = LocalDateTime.now()
        var next = now.toLocalDate().atTime(Day.HOUR, 0)
        if (!next.isAfter(now)) next = next.plusDays(1)
        val at = next.atZone(ZoneId.systemDefault()).toInstant().toEpochMilli()
        val am = c.getSystemService(AlarmManager::class.java)
        // Inexact on purpose: no special alarm permission, and a few minutes either side is fine.
        am.setAndAllowWhileIdle(AlarmManager.RTC_WAKEUP, at, alarm(c))
    }

    private fun alarm(c: Context): PendingIntent = PendingIntent.getBroadcast(
        c, 1, Intent(c, NightReceiver::class.java),
        PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE,
    )

    /**
     * Tonight's finds: up to five places passed today, never told before, picked by the nightly mix (agreed 21 Nov):
     * highest score first, then each next pick loses 1.5 for every find already picked from the same era and
     * 1.5 for every one with the same topic. Interest still leads (a 9 from a picked era beats a 7 from a new one),
     * but a night spreads across time.
     * Ties go to whichever was passed longest ago (22 Nov), so old dust gets its turn. Unpicked places stay dust:
     * pass them again on a quieter day and they can be uncovered then.
     */
    fun pick(c: Context, day: String): List<Spot> {
        val store = Store(c)
        val told = store.told
        val first = store.firstPassed()
        val left = store.passed(day)
            .filter { it !in told }
            .mapNotNull { Spots.byId(c, it) }
            .sortedWith(compareByDescending<Spot> { it.score }.thenBy { first[it.id] ?: day }.thenBy { it.id }) // best, then oldest dust, then stable
            .toMutableList()
        val picked = mutableListOf<Spot>()
        while (picked.size < 5 && left.isNotEmpty()) {
            val best = left.maxWith(compareBy<Spot> { s ->
                s.score - 1.5 * picked.count { it.era == s.era } - 1.5 * picked.count { it.topic.isNotEmpty() && it.topic == s.topic }
            }.thenBy { -left.indexOf(it) })
            picked += best; left -= best
        }
        return picked
    }

    /** At 9pm: first count any untold zone you're standing in right now (the zone fix, 21 Nov), then pick and tell. */
    fun run(c: Context, done: () -> Unit = {}) {
        val now = LocalDateTime.now()
        // If the alarm slipped past midnight, it still belongs to yesterday.
        val date = if (now.hour < 12) LocalDate.now().minusDays(1) else LocalDate.now()
        val day = Day.endingOn(date)
        Fences.here(c) { loc ->
            if (loc != null) Fences.countInside(c, loc, day, "at 9pm")
            try { tell(c, day) } finally { done() }
        }
    }

    private fun tell(c: Context, day: String) {
        val spots = pick(c, day)
        TestLog.add(c, "tonight: " + (if (spots.isEmpty()) "nothing to tell" else spots.joinToString(", ") { it.id }))
        if (spots.isNotEmpty()) {
            val store = Store(c)
            spots.asReversed().forEach { store.tell(it.id, day) } // best ends up newest
            notify(c, spots.first(), spots.size)
            Fences.register(c) // Drop the fences for facts that have been told.
        }
        schedule(c)
    }

    @SuppressLint("MissingPermission")
    private fun notify(c: Context, spot: Spot, count: Int) {
        val nm = NotificationManagerCompat.from(c)
        if (!nm.areNotificationsEnabled()) return
        c.getSystemService(NotificationManager::class.java).createNotificationChannel(
            NotificationChannel(CHANNEL, "Tonight", NotificationManager.IMPORTANCE_DEFAULT).apply {
                description = "One line at 9pm about the best place you passed today."
            }
        )
        val open = PendingIntent.getActivity(
            c, 2,
            Intent(c, MainActivity::class.java)
                .putExtra(EXTRA_SPOT, spot.id)
                .addFlags(Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP),
            PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE,
        )
        nm.notify(
            1,
            NotificationCompat.Builder(c, CHANNEL)
                .setSmallIcon(R.drawable.ic_ring)
                .setContentTitle(spot.line)
                .setStyle(NotificationCompat.BigTextStyle().bigText(spot.line + if (count > 1) " And ${count - 1} more." else ""))
                .setContentIntent(open)
                .setAutoCancel(true)
                .build(),
        )
    }
}
