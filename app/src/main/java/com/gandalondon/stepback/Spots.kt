package com.gandalondon.stepback

import android.content.Context
import org.json.JSONArray
import java.time.LocalDate
import java.time.LocalDateTime

data class Point(val lat: Double, val lng: Double, val radius: Float)

data class Spot(
    val id: String,
    val kind: String,
    val score: Int,
    val place: String,
    val points: List<Point>,
    val line: String,
    val fact: String,
    val source: String,
)

object Spots {
    @Volatile private var cache: List<Spot>? = null

    fun all(c: Context): List<Spot> = cache ?: load(c).also { cache = it }

    fun byId(c: Context, id: String): Spot? = all(c).firstOrNull { it.id == id }

    private fun load(c: Context): List<Spot> {
        val text = c.assets.open("spots.json").bufferedReader().use { it.readText() }
        val arr = JSONArray(text)
        return (0 until arr.length()).map { i ->
            val o = arr.getJSONObject(i)
            val pts = o.getJSONArray("points")
            Spot(
                id = o.getString("id"),
                kind = o.getString("kind"),
                score = o.getInt("score"),
                place = o.getString("place"),
                points = (0 until pts.length()).map { j ->
                    val p = pts.getJSONArray(j)
                    Point(p.getDouble(0), p.getDouble(1), p.getDouble(2).toFloat())
                },
                line = o.getString("line"),
                fact = o.getString("fact"),
                source = o.getString("source"),
            )
        }
    }
}

/** A Stepback day runs 9pm to 9pm, so anything passed after tonight's line counts towards tomorrow's. */
object Day {
    const val HOUR = 21
    fun key(now: LocalDateTime = LocalDateTime.now()): String =
        (if (now.hour >= HOUR) now.toLocalDate().plusDays(1) else now.toLocalDate()).toString()

    /** Key for the day whose line goes out at 9pm on [date]. */
    fun endingOn(date: LocalDate): String = date.toString()
}
