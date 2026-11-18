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
    fun toldDay(id: String): String = p.getString("told_day_$id", null) ?: Day.key()

    fun tell(id: String, day: String = Day.key()) {
        p.edit()
            .putString("told_day_$id", day)
            .putStringSet("told", told + id)
            .putString("history", (listOf(id) + history.filter { it != id }).joinToString(","))
            .apply()
    }

    /** Private verdict per fact: Interesting or Not for me. Tap again to undo. */
    fun verdict(id: String): String? = p.getString("v_$id", null)

    fun setVerdict(id: String, v: String) {
        p.edit().apply { if (verdict(id) == v) remove("v_$id") else putString("v_$id", v) }.apply()
    }

    /** Set an answer outright (swipes); null clears it. */
    fun putVerdict(id: String, v: String?) {
        p.edit().apply { if (v == null) remove("v_$id") else putString("v_$id", v) }.apply()
    }

    fun withVerdict(v: String): List<String> = history.filter { verdict(it) == v }

    companion object {
        const val YES = "yes"
        const val NO = "no"
    }
}
