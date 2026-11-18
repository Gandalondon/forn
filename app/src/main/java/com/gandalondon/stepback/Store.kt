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

    fun passedAt(day: String, id: String): Long? =
        if (p.contains("at_${day}_$id")) p.getLong("at_${day}_$id", 0) else null

    /** Facts already told. Each fact once. */
    val told: Set<String> get() = p.getStringSet("told", emptySet())!!.toSet()

    /** Newest first. */
    val history: List<String> get() = p.getString("history", "")!!.split(",").filter { it.isNotBlank() }

    fun tell(id: String) {
        p.edit()
            .putStringSet("told", told + id)
            .putString("history", (listOf(id) + history.filter { it != id }).joinToString(","))
            .apply()
    }

    /** Private Well I never taps. Not tapping is the only negative. */
    val wellINever: Set<String> get() = p.getStringSet("win", emptySet())!!.toSet()

    fun toggleWellINever(id: String) {
        val now = wellINever
        p.edit().putStringSet("win", if (id in now) now - id else now + id).apply()
    }
}
