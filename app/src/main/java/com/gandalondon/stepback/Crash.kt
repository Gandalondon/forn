package com.gandalondon.stepback

import android.content.Context

/** Test aid: keeps the last crash so the next open can show it. Stays on the phone. */
object Crash {
    private const val KEY = "last_crash"

    fun install(c: Context) {
        val app = c.applicationContext
        val previous = Thread.getDefaultUncaughtExceptionHandler()
        if (previous is Handler) return
        Thread.setDefaultUncaughtExceptionHandler(Handler(app, previous))
    }

    fun last(c: Context): String? = prefs(c).getString(KEY, null)

    fun clear(c: Context) = prefs(c).edit().remove(KEY).apply()

    private fun prefs(c: Context) = c.getSharedPreferences("stepback_crash", Context.MODE_PRIVATE)

    private class Handler(val c: Context, val previous: Thread.UncaughtExceptionHandler?) : Thread.UncaughtExceptionHandler {
        override fun uncaughtException(t: Thread, e: Throwable) {
            runCatching {
                // commit, not apply: the process is about to die.
                prefs(c).edit().putString(KEY, e.stackTraceToString()).commit()
            }
            previous?.uncaughtException(t, e)
        }
    }
}
