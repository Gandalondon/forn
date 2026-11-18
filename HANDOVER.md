# Stepback handover

Master handover for Stepback. Mirrors the Google Doc "Stepback handover" in Drive > Claude. Rules: "App idea rules", in the same folder.

## State (Wed 18 Nov 2026, morning)

- Data check: done, passed (below).
- v1 test app: built green. Install through Obtainium. Screens and a clickable prototype are on the canvas artifact Stepback screens (boards 1 to 9).
- Signing secrets NOT set yet, so each build has a one-off key: an update means uninstall then reinstall, which wipes what it found. Don't push app changes before Thursday's flight unless it's broken (use [skip ci] for docs). Set SIGNING_KEYSTORE_B64 and SIGNING_PASSWORD after the test; the keystore made on 18 Nov lives only in that chat's workspace, so make a new one if it's gone.
- Name: Stepback for now. Tony likes Munin (memory; Odin's raven that flies out by day and reports back in the evening). TBC after the test. If it's Munin, the narrow-lanes driving app needs a new name. Renaming the repo is fine (GitHub redirects; re-add in Obtainium).
- Goal: APK on Tony's Pixel through Obtainium before the flight on Thursday 19 Nov.

## v1 test (what's in)

- Geofences around hand-picked spots (`app/src/main/assets/spots.json`). Crossing one logs the spot id and the time first passed. No GPS track, and no internet permission.
- 9pm (inexact alarm, a few minutes either side): best spot passed that day, one notification. Quiet day, no ping. Each fact once. The day runs 9pm to 9pm.
- Tap opens one fact screen: big fact top-aligned (so it can grow), place name small under it (never above: eyebrow), two equal buttons at the bottom: Interesting and Not for me (private; tap again to undo). Changed 18 Nov from a single Well I never, which Tony found too on the nose.
- Before the first fact, the app shows Go about your day. Find out tonight. plus a count of places passed so far today (a test aid).
- Urbanist bundled (400, 600). Always black (off black #1A1A1A, as in Hugin and Rinse), decided 18 Nov; no light mode.
- Logo (18 Nov, from the 2016 concept on Medium): STEP plus a mirrored BACK, now in Urbanist SemiBold caps; app icon is a thin ring on a black tile. On the canvas, board 9. To sense-check.
- Out until the loop is proven: 3D strata, Take me back, Tell me more, swipe stack, font comparison, logo.

## Data check results (18 Nov)

Well I never: Heathrow (an Iron Age village and temple under the north runway; the T5 Stanwell Cursus), Aberdeen airport (the Dyce Pictish stones; Tyrebagger stone circle), Portlethen (a ring cairn moved 175m for an industrial estate in 1995), Leadenhall (the Roman basilica), Chanctonbury (two Roman temples under the beeches), Cannon Hill (named for canons, not cannons), SW20 (London Clay, a warm sea with crocodiles; works once).
Fine: random residential road (geology only). Brown sign: Ranmore (St Barnabas).

Findings:
- The suburbs pass only on geology, and only once. After about a week at home it goes quiet: it's a weekly app that pings on days you move around. Watch this in the test.
- A 100m geofence misses landscape facts seen from a car or plane. v1 uses 0.4 to 3.5km radii, and the copy says near, under or passed.
- The open data (Historic England NHLE, HES Canmore, both OGL) is register text. Lines still need writing, so v1 is hand-curated. Scaling this is the real open problem.

## Direction change, 18 Nov (after the v1 build)

- Evening flow: 9pm notification (one line), tap it, then up to five cards from the day (never padded; a home day may be one card), picked by interest with at most one per type and spread across the day. Each card shows the fact, then place and time under it.
- Cards: white, rounded, inset on a black stage. Swipe right for Interesting, left for Not for me, plus the two buttons (Not for me left, Interesting right). Sniff-style snackbar after each: Thanks. More like this. / Fewer like this., with Undo, 4 seconds.
- The strata is the payoff after every session, an art-installation feel: today's layers drop in and settle, then it slowly turns. Pinch, zoom, rotate; text surfaces from the layers as you zoom in (Tony to send a game reference: zooming into a DNA strand where text comes out). Silent; sound maybe later as an option.
- Strata encoding: newest on top, hairline gap between days; thickness and brightness from your answer (Interesting thick and bright, no answer middle, Not for me thin and faint); texture by type (lines for Roman, medieval and buildings, dots for prehistory, rings for Pictish, grain for geology, pebbles for landscape); a bright cluster marks where on a simplified UK footprint each was found (no streets or names).
- Visual payoff has two directions, both kept: (1) the strata block (Stepback prototype, https://claude.ai/artifact/UtGTrfpegNVjiLqVrod4SE); (2) the strand (Stepback prototype 2, https://claude.ai/artifact/WRmYVaQDUwxYGZJeW44Vrk). The strand is from Tony's game reference (a life-path DNA strand with branching scenes and text panels): time runs left to right along a slowly turning double helix of dust; Interesting finds are black dots ringed in white (the Stepback ring) that you tap to bring the card back; Not for me and unanswered are small grey dots you can't tap; names surface as you zoom in.
- Onboarding stays plain black; grey text is a snowy near-white.
- Browser prototype: artifact Stepback prototype (https://claude.ai/artifact/UtGTrfpegNVjiLqVrod4SE), with After 1 day, 1 week and 1 month toggles. Week and month use example data.
- The phone build stays the v1 single fact for the test; the new flow goes into the app after Thursday.

## Ideas from Tony, 18 Nov

- Log the time of each pass ("what was I doing at 9:30?"). Built: stored, not shown.
- The strata view places each find where it was found, on a very simplified modern map (no street names or buildings), pinch, zoom and 3D. Spot coordinates are enough; no tracking needed. For after the test.
- Facts are tagged by type (Roman, prehistory, Pictish, geology and so on). Built: Interesting adds 1.5 to that type, Not for me takes 2 off, no answer takes 0.5 off. Types fade, they never vanish, so a great Roman fact can still win on a quiet day. Any data pulled in later needs the same type tags.
- Strata view (later): every fact told stays in the block. Interest shows as weight: tapped types are dark and dense, ignored ones are light and thin. Height stays time (newest on top), so interest never moves a layer.
- Daily or weekly alerts: held. It's a setting, and settings were ruled out. Let the test show the natural frequency first.

## Build and install

- GitHub Actions (`.github/workflows/build.yml`, copied from Rinse) builds `Stepback.apk` into a release on each push to main. Obtainium watches the repo.
- Signing: repo secrets `SIGNING_KEYSTORE_B64` and `SIGNING_PASSWORD`, key alias `stepback`. The keystore was generated 18 Nov and must be kept with the project (not in git).

## Next

1. Create the repo, push, set the secrets, and check that the first build goes green.
2. Install through Obtainium and grant location (all the time) and notifications. At home today the SW20 fence should fire at once, and tonight's 9pm line should be the London Clay.
3. Thursday: Heathrow, Aberdeen and Portlethen. The 9pm line in Portlethen is the real test.
4. After the test: font comparison (Urbanist, Manrope, Outfit), screens, and the 3D strata prototype in the browser.
