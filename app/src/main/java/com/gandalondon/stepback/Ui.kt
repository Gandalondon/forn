package com.gandalondon.stepback

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
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
import androidx.compose.ui.text.ExperimentalTextApi
import androidx.compose.ui.text.font.FontVariation
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

// Always white (18 Nov, matching the white 3D view and cards), whatever the system setting.
@Composable
fun palette() = LightPalette

// Instrument Sans (SIL Open Font License), bundled as one variable font. Urbanist dropped 18 Nov.
@OptIn(ExperimentalTextApi::class)
val Instrument = FontFamily(
    Font(R.font.instrument_sans, weight = FontWeight.Normal, variationSettings = FontVariation.Settings(FontVariation.weight(400))),
    Font(R.font.instrument_sans, weight = FontWeight.SemiBold, variationSettings = FontVariation.Settings(FontVariation.weight(600))),
)

object Type {
    val Fact = TextStyle(
        fontFamily = Instrument, fontSize = 34.sp, lineHeight = 40.sp,
        fontWeight = FontWeight.SemiBold, letterSpacing = 0.2.sp,
        lineBreak = LineBreak.Heading, // balanced lines, no widows
    )
    val Body = TextStyle(
        fontFamily = Instrument, fontSize = 17.sp, lineHeight = 24.sp,
        letterSpacing = 0.sp, lineBreak = LineBreak.Paragraph,
    )
    val Button = Body.copy(fontWeight = FontWeight.SemiBold)
}

/** One choice button. */
data class Choice(val label: String, val filled: Boolean = false, val onClick: () -> Unit)

/** Big text at the top so it can grow, quiet text under it, buttons at the bottom. Every screen is this. */
@Composable
fun Page(big: String, small: String?, vararg choices: Choice) {
    val p = palette()
    Column(
        Modifier.fillMaxSize().background(p.bg).systemBarsPadding()
            .padding(start = 24.dp, end = 24.dp, top = 48.dp, bottom = 24.dp),
    ) {
        Text(big, style = Type.Fact, color = p.fg)
        if (small != null) {
            Spacer(Modifier.height(16.dp))
            Text(small, style = Type.Body, color = p.muted)
        }
        Spacer(Modifier.weight(1f))
        if (choices.isNotEmpty()) {
            Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(16.dp)) {
                choices.forEach { c -> Pill(c.label, p, c.filled, Modifier.weight(1f), c.onClick) }
            }
        }
    }
}

@Composable
private fun Pill(label: String, p: Palette, filled: Boolean, modifier: Modifier, onClick: () -> Unit) {
    val shape = RoundedCornerShape(50)
    Box(
        modifier.height(64.dp).clip(shape)
            .then(if (filled) Modifier.background(p.fg) else Modifier.border(1.dp, p.fg, shape))
            .clickable(onClick = onClick),
        contentAlignment = Alignment.Center,
    ) {
        Text(label, style = Type.Button, color = if (filled) p.bg else p.fg)
    }
}
