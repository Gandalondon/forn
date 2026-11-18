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
     * Tonight's finds: up to five of the most interesting places passed today, by score, never told before.
     * Answers don't steer what you're told (decided 18 Nov): Interesting or Not for me only decides
     * ball or dust in the rings, so the picture keeps both.
     */
    fun pick(c: Context, day: String): List<Spot> {
        val told = Store(c).told
        return Store(c).passed(day)
            .filter { it !in told }
            .mapNotNull { Spots.byId(c, it) }
            .sortedByDescending { it.score }
            .take(5)
    }

    fun run(c: Context) {
        val now = LocalDateTime.now()
        // If the alarm slipped past midnight, it still belongs to yesterday.
        val date = if (now.hour < 12) LocalDate.now().minusDays(1) else LocalDate.now()
        val day = Day.endingOn(date)
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
