package com.gandalondon.stepback

import android.content.Context
import android.content.SharedPreferences

/** Everything Stepback knows lives here, on the phone. Nothing is sent anywhere. */
class Store(c: Context) {
    private val p: SharedPreferences = c.getSharedPreferences("stepback", Context.MODE_PRIVATE)

    /** Spots passed during the day with this key. */
    fun passed(day: String): Set<String> = p.getStringSet("passed_$day", emptySet())!!.toSet()

    fun addPassed(day: String, ids: Collection<String>) {
        if (ids.isEmpty()) return
        val e = p.edit().putStringSet("passed_$day", passed(day) + ids)
        // When you first passed it, for "what was I doing at 9:30?" later. Not shown in v1.
        val now = System.currentTimeMillis()
        ids.forEach { if (!p.contains("at_${day}_$it")) e.putLong("at_${day}_$it", now) }
        e.apply()
    }

    /** A pass found afterwards from a recorded route, with the time of the first fix inside the zone. */
    fun addPassedAt(day: String, id: String, at: Long) {
        val e = p.edit().putStringSet("passed_$day", passed(day) + id)
        if (!p.contains("at_${day}_$id")) e.putLong("at_${day}_$id", at)
        e.apply()
    }

    fun passedAt(day: String, id: String): Long? =
        if (p.contains("at_${day}_$id")) p.getLong("at_${day}_$id", 0) else null

    /** Facts already told. Each fact once. */
    val told: Set<String> get() = p.getStringSet("told", emptySet())!!.toSet()

    /** Newest first. */
    val history: List<String> get() = p.getString("history", "")!!.split(",").filter { it.isNotBlank() }

    /** Which day a fact was told for (a Stepback day key). Older facts without one count as today. */
    /**
     * The evening a find was told. Finds told before told_day existed (the v1 app) have none, and used to fall back
     * to Day.key(), so they floated onto today's ring every day (19 Nov, from Tony's exported data: sw20-clay).
     * Now: the earliest day it was passed, else today. Reads only; nothing stored changes.
     */
    fun hasToldDay(id: String) = p.contains("told_day_$id")

    fun toldDay(id: String): String = p.getString("told_day_$id", null)
        ?: p.all.keys.filter { it.startsWith("passed_") && passed(it.removePrefix("passed_")).contains(id) }
            .map { it.removePrefix("passed_") }.minOrNull()
        ?: Day.key()

    fun tell(id: String, day: String = Day.key()) {
        p.edit()
            .putString("told_day_$id", day)
            .putStringSet("told", told + id)
            .putString("history", (listOf(id) + history.filter { it != id }).joinToString(","))
            .apply()
    }

    /** Every day that has places passed, oldest first. */
    fun passedDays(): List<String> = p.all.keys.filter { it.startsWith("passed_") }.map { it.removePrefix("passed_") }.sorted()

    /**
     * The day each place was first passed, for the pick's tie-break (22 Nov): best place first, then whichever was
     * passed longest ago, so old dust gets its turn.
     */
    fun firstPassed(): Map<String, String> {
        val out = HashMap<String, String>()
        passedDays().forEach { day -> passed(day).forEach { id -> if (id !in out) out[id] = day } }
        return out
    }

    /** Tonight's cards have been paged through (22 Nov: no answers, they just page). */
    fun seen(day: String) = p.getBoolean("seen_$day", false)

    fun markSeen(day: String) = p.edit().putBoolean("seen_$day", true).apply()

    /**
     * No more answers (22 Nov): every place passed is dust and every find told is a ball. Once: a night that was
     * already answered counts as seen, then the stored answers (v_ keys) are removed.
     */
    fun dropAnswers() {
        if (p.getBoolean("answers_dropped", false)) return
        val e = p.edit()
        p.all.keys.filter { it.startsWith("v_") }.forEach { k ->
            val id = k.removePrefix("v_")
            if (hasToldDay(id)) e.putBoolean("seen_${toldDay(id)}", true)
            e.remove(k)
        }
        e.putBoolean("answers_dropped", true).apply()
    }
}
