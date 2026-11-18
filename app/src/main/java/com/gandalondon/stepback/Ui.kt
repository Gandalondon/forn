package com.gandalondon.stepback

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.systemBarsPadding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.Font
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.LineBreak
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

// Same off black as Hugin and Rinse. Monochrome; follows the system's light or dark.
val Ink = Color(0xFF1A1A1A)
val Paper = Color(0xFFFFFFFF)

data class Palette(val bg: Color, val fg: Color, val muted: Color)

val DarkPalette = Palette(Ink, Paper, Color(0xFFA8A8A8))
val LightPalette = Palette(Paper, Ink, Color(0xFF6B6B6B))

@Composable
fun palette() = if (isSystemInDarkTheme()) DarkPalette else LightPalette

// Urbanist (SIL Open Font License), bundled.
val Urbanist = FontFamily(
    Font(R.font.urbanist_regular, FontWeight.Normal),
    Font(R.font.urbanist_semibold, FontWeight.SemiBold),
)

object Type {
    val Fact = TextStyle(
        fontFamily = Urbanist, fontSize = 34.sp, lineHeight = 40.sp,
        fontWeight = FontWeight.SemiBold, letterSpacing = 0.2.sp,
        lineBreak = LineBreak.Heading, // balanced lines, no widows
    )
    val Body = TextStyle(
        fontFamily = Urbanist, fontSize = 17.sp, lineHeight = 24.sp,
        letterSpacing = 0.sp, lineBreak = LineBreak.Paragraph,
    )
    val Button = Body.copy(fontWeight = FontWeight.SemiBold)
}

/** Big text at the bottom, quiet text under it, one button. Every screen is this. */
@Composable
fun Page(big: String, small: String?, button: String?, filled: Boolean = false, onClick: () -> Unit = {}) {
    val p = palette()
    Column(
        Modifier.fillMaxSize().background(p.bg).systemBarsPadding()
            .padding(start = 24.dp, end = 24.dp, top = 32.dp, bottom = 24.dp),
    ) {
        Spacer(Modifier.weight(1f))
        Text(big, style = Type.Fact, color = p.fg)
        if (small != null) {
            Spacer(Modifier.height(16.dp))
            Text(small, style = Type.Body, color = p.muted)
        }
        if (button != null) {
            Spacer(Modifier.height(48.dp))
            Pill(button, p, filled, onClick)
        }
    }
}

@Composable
private fun Pill(label: String, p: Palette, filled: Boolean, onClick: () -> Unit) {
    val shape = RoundedCornerShape(50)
    Box(
        Modifier.fillMaxWidth().height(64.dp).clip(shape)
            .then(if (filled) Modifier.background(p.fg) else Modifier.border(1.dp, p.fg, shape))
            .clickable(onClick = onClick),
        contentAlignment = Alignment.Center,
    ) {
        Text(label, style = Type.Button, color = if (filled) p.bg else p.fg)
    }
}
