package com.gandalondon.stepback

import android.content.ContentValues
import android.content.Context
import android.os.Environment
import android.provider.MediaStore
import java.io.File
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

/** Test aid (18 Nov): every zone crossing, with time and where Android thought you were. Saved with the walk. */
object TestLog {
    private fun file(c: Context) = File(c.filesDir, "events.log")
    private val stamp = SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.UK)

    fun add(c: Context, line: String) = runCatching { file(c).appendText(stamp.format(Date()) + "  " + line + "\n") }

    fun read(c: Context): String = runCatching { file(c).readText() }.getOrDefault("")

    /** Writes the log to Downloads/Forn next to the GPX. Returns where it went. */
    fun export(c: Context): String = runCatching {
        val name = "forn-events-" + SimpleDateFormat("yyyy-MM-dd-HHmm", Locale.UK).format(Date()) + ".txt"
        val cv = ContentValues().apply {
            put(MediaStore.Downloads.DISPLAY_NAME, name)
            put(MediaStore.Downloads.MIME_TYPE, "text/plain")
            put(MediaStore.Downloads.RELATIVE_PATH, Environment.DIRECTORY_DOWNLOADS + "/Forn")
        }
        val uri = c.contentResolver.insert(MediaStore.Downloads.EXTERNAL_CONTENT_URI, cv)!!
        c.contentResolver.openOutputStream(uri)!!.use { it.write(read(c).toByteArray()) }
        "Downloads/Forn/$name"
    }.getOrDefault("")
}
