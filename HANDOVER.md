# Stepback handover

Name: the app is now Forn (Old Norse for ancient), chosen 18 Nov over Hring (said aloud it sounds like herring), Jord (the J), Askr and Munin. App name and in-app copy changed in build 12; the GitHub repo and package id stay stepback for now (Tony may rename the repo later).

Master handover for Stepback. The current rulebook (data, facts, picks, rings, look) is RULES.md: read it first. Mirrors the Google Doc "Stepback handover" in Drive > Claude. Rules: "App idea rules", in the same folder.

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
- 18 Nov, 11:15, current direction (Stepback prototype 2): the 3D view is White. Interesting finds are plain black balls (no outline), tap to reopen the card. Not for me: the ball bursts into grey dust where it sat (on arrival for today, settled dust for older days). No grey balls, no labels, no map or time axes: each day is a loose cluster, today in the centre, older days spiral outward. Cards stay white on a black stage. Prototype shows three cards (Dyce, Tyrebagger, Portlethen) so the burst can be tested. No fake notification: the prototype lands straight on the cards.
- Fonts: Urbanist for facts and titles only; body copy, buttons and small text in Instrument Sans (Urbanist body was hard to read; same split as Hlid, which uses DM Sans for body). To confirm.
- Tony's notes on prototype 2 (18 Nov, 11:20), to build next:
  - Cards: drop the Thanks snackbar (swiping is obvious); card sits lower; progress dots move under the card. Words Not for me / Interesting to become icons (thumbs, IMDb Trivia style, or another mark; Material Symbols). Zero onboarding like Relay: a settings cog that explains how it works.
  - 3D: keep the burst (likes it, needs trying on the phone). Balls flat black, no reflection or highlight (positive and negative feel; the depth reads once you spin a month). Tally: 16px between title and line.
  - Open question: the space has no readable logic. Spinning loses which is which; a tapped ball shows a time but no date. Claude's proposal: make distance from the centre the only rule (today at the centre, each older day a shell further out, angle means nothing), which survives any rotation. On open, the camera starts close on today's cluster, plays the bursts, then pulls back to the whole. Reopened cards show the date and time (Tue 3 Nov, 10:22).
- 18 Nov, 11:55, prototype 2 updated:
  - Layout toggles: A Solar system, B Tree rings, D Stepped cone (new, beside B), C Onion. D is B's rings with each older day a step lower: an open pit, today the top rim. From above it reads as tree rings, from the side as strata (newest on top). Steps 0.55 apart, camera at about 20 degrees so both read. To compare B and D.
  - Opening shot fixed: opens on today framed with room for the bursts (it was so close the balls were blobs), today's balls evenly spaced so they never touch, and the whole is framed in the space between the icon and the tally with a margin (it was cropped at the sides and ran under the text). Animation rules unchanged: bursts, then pull back, past appears day by day, spin starts after.
  - App opens on the 3D view, not on black: today's cards sit on top under the same dim scrim as a reopened card; swipe them away and the 3D view is all that's left. While the cards are up, the view waits framed on today. Cog swapped for an info icon (Material Symbols info), black, top right: it explains how it works.
- 18 Nov, 12:10, prototype 2 again:
  - Layouts cut to two: Tree rings (flat) and Tree trunk (new). Solar system, stepped cone and onion dropped. Spans: 1 day, 1 week, 1 month, 4 years.
  - Both: distance from the centre is when you found it (today the outer ring, the past at the core), and a thick ring marks each new year, like a tree. That replaces the year toggle idea: you pinch and zoom instead.
  - Tree trunk: height is how old the thing itself is, on a log scale (10 years ago at the top, 100 million at the base): recent history on top, geology at the base. Each day is a faint upright cylinder of dust, so it reads from any angle. Every fact now needs an age for the thing (example ages in the prototype; spots.json will need the same field).
  - Card stack is plain: the next card sits underneath, solid white, no fade, scale or bounce.
  - One font: Instrument Sans everywhere, facts in SemiBold. Urbanist dropped (its lowercase t read as a cross).
  - Info opens a full How it works page with a back arrow, Relay's settings pattern. Sections 24px apart and 24px below the header. Icons are Material Symbols Rounded at one weight (400), back arrow included.
  - Icon options for the info button: canvas Stepback info icon options (https://claude.ai/artifact/PcpSx2Q2HRjvGMx7LYwXb7), boards 1 to 8: info, help, question mark, lightbulb, book, compass, history, more. Tony to pick.
- 18 Nov, 12:25, after Tony's 4-year screenshots:
  - The tree grows, it doesn't squeeze: rings stay 0.42 apart forever, so 4 years is simply a much bigger tree. The overview reads as a cross-section; zoomed in, any part reads like one month and balls are tappable. The pull-back zooms evenly (geometric), so long spans don't rush.
  - Ring weight: day a dotted hairline, Monday a step heavier, the 1st of the month heavier, 1 January darkest and thickest. Tap-a-ring-to-zoom dropped: pinch does it.
  - Zoom limit: never so close that a ball fills the screen. The tally has no panel: the rings run under the text, which Tony likes as a happy accident (white panel tried and removed, 18 Nov).
  - Trunk heights now in fixed bands, stacked like strata with no empty gaps: modern (under 500 years), medieval, Roman, prehistoric, geology. Within a band, older sits lower. If banded 1 month still doesn't click, drop the trunk and keep flat rings.
  - Info icon: Tony picked info (board 1) for now.
- 18 Nov, 12:30: the flat disc is the direction ("that crazy disc", zoom in and out). Tree trunk parked: liked as a concept, too hard to navigate; its toggle is removed, the banded code stays in the prototype. Heavier rings are now one solid band each (they had been parallel lines that split apart up close), and a Monday within two days of a month ring stays a plain day ring so heavy rings never crowd.
- Onboarding stays plain black; grey text is a snowy near-white.
- Browser prototype: artifact Stepback prototype (https://claude.ai/artifact/UtGTrfpegNVjiLqVrod4SE), with After 1 day, 1 week and 1 month toggles. Week and month use example data.
- The phone build stays the v1 single fact for the test; the new flow goes into the app after Thursday.

## Raynes Park test walk (18 Nov, afternoon)

- Build 5 (12:30) adds four Raynes Park spots for Tony's walk to the post office (1a Amity Grove): rp-never-a-park (Rayne's three farm "parks", score 8), rp-station (the 1889 guidebook joke, 8), rp-apostles (twelve roads, not named after apostles, old cricket ground, 7), beverley-brook (Beaver's Ley, Beferithi in 693, 8, 1.3km "near" fence). Facts checked against Hidden London, LAMAS vol. 34, Wikipedia/Wikishire, Merton Council.
- Build 6: app icon ring sized like Rinse and Hlid (38 across in the 108 grid), stroke 4, centred. Build 7: whole v1 app white with Instrument Sans (Urbanist removed), plus a crash recorder that shows the last crash's stack trace on the next open (test aid; remove later). With the key set, updates no longer need a reinstall, so app tweaks before the flight are fine; just keep each build working.
- Build 9: setup screens each have their own headline (Go about your day. Find out tonight. / Now pick Allow all the time. / One quiet moment at 9pm.), then Enjoy your day. with the count of places passed. The notifications button opens the app's settings once Android stops asking (it used to do nothing, which read as a hang). Prototype onboarding copy matches.
- Build 10: test aid Tell me now on the Enjoy your day screen (once something's been passed) runs tonight's 9pm line straight away, notification and all; 9pm then picks the next best. Remove after testing.
- Build 13: fixed the real cause of setup looking stuck. The screen never redrew after a permission was granted or an answer tapped (Compose skipped it because it didn't read the refresh counter), so each step only moved on after a restart. Now wrapped in key(tick).
- Build 14: test aid Record walk (copied from Hlid's TrackService): GPS track as GPX plus the zone log (every crossing with time and Android's position) saved to Downloads/Forn on the phone.
- Build 15 (18 Nov, 14:15): the app is now the rings. After setup the screen is a WebView (app/src/main/assets/web: index.html ported from prototype 2, three.js bundled with esbuild as a classic script, Instrument Sans), with a native bridge (Web.kt, window.Forn: state, verdict, tellNow, record). 9pm now tells up to five finds (most interesting first), and they're the cards next time you open; answers are stored and the finds sit in the rings by the day they were told. Tell me now and Record walk moved to a Testing section on the How it works page. Checked in Chrome with example data; on the phone it's untested until Tony's walk.
- Builds 16 to 20 (18 Nov afternoon): icon an off-black ring on white; Show me 4 months demo on the How it works page (example finds around the real ones); finds scatter round their rings (better hash; they had lined up in streaks); Tell me more on reopened finds (share menu with a ready-made question); Stop and save checks the recorded route against every zone and counts any the geofencing missed, logging whether each zone had fired (tight zones can be missed at driving speed).
- Build 21: Try it out panel on the How it works page replaces Show me 4 months: how far back (1 month, 4 months, 1 year, 4 years), kept (0 to 100%), how busy (quiet, normal, busy) and empty days (full ring, thin ring, no ring), then Show. Open question for Tony: how empty days should look. Claude's recommendation: thin rings (like a drought year in a real tree), so time stays honest and quiet spells read as tight grain. The real rings use full rings until he decides.
- Prototype 2 controls now also have Mixed / All kept / All dust scenarios, and an Onboarding run-through.
- Signing key set 18 Nov 12:42: Tony pasted SIGNING_KEYSTORE_B64 and SIGNING_PASSWORD into the repo secrets (Claude can't set secrets: the API is blocked from its sessions). Keystore (alias stepback, CN=Stepback, O=Ganda) and password files were sent to Tony in chat to keep on his Mac, never in git. Build 8 is the first signed with it (checked). After one last reinstall of build 8, every update installs over the top through Obtainium, so app tweaks no longer wipe data.
- v1 still tells one fact at 9pm (the best passed that day, never repeated). The five-card evening is the post-test build. Watch: does a short local walk give anything worth a ping, and how often will the same streets have something new?

## Ideas from Tony, 18 Nov

- Log the time of each pass ("what was I doing at 9:30?"). Built: stored, not shown.
- The strata view places each find where it was found, on a very simplified modern map (no street names or buildings), pinch, zoom and 3D. Spot coordinates are enough; no tracking needed. For after the test.
- Facts are tagged by type (Roman, prehistory, Pictish, geology and so on). Any data pulled in later needs the same type tags.
- No personalisation (decided 18 Nov, build 11): the app always picks the most interesting places by score, and answers never steer what you're told. Interesting or Not for me only decides ball or dust in the rings; otherwise the dust would die out as the app learned your taste. Answers are still stored. Supersedes the type weighting (+1.5 / -2 / -0.5) and the lighter/darker interest idea for the strata.
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

## Landing page (agreed 18 Nov, build once Tony's Mac is connected)

- The most minimal of his sites: the full-screen 3D rings are the page (no phone mock-ups), with one big, bold line of text at a time over them.
- Not a normal scroll: back and next arrows, and scroll or swipe also steps forward or back (the page takes over the scroll). Text cuts between steps, no text animation: the camera carries the motion.
- Steps act out a day: notice, 9pm, zoom into a ball and a real card opens, a ball bursts to dust, pull back to years of rings, then Forn and the download (or coming soon).
- Footer: copyright Tony and Privacy, which opens as a card like the app.
- Tone: understandable sentences, not clipped AI punchlines. First copy draft is in the 18 Nov chat (v2, plain sentences).
- Steps are real text in the page (search, screen readers); reduced motion gives plain slides; the type shows before the 3D loads. Keep balls out from behind the letters.
- No domain yet: may go up on gandalondon.com to share with a friend.
- Opening screen (18 Nov idea): the word FORN alone, filling the whole window, set in Instrument Sans inside an SVG that stretches to the viewport (no outlining needed). Use the font's width axis: condensed and stretched tall on phones, normal width stretched wide on desktop. First scroll or swipe goes into the rings. To compare: FORN in caps (a solid block; a wordmark exception to the no-caps rule) against Forn in sentence case, and maybe the O as the app's ring (probably one idea too many).
- Folio page idea (18 Nov): show the elastic wordmark in one frame that slowly morphs through real formats (app-sized square, phone screen, wide billboard, tall banner), the word refitting as it goes. No toggle, no labels. On desktop it can also refit live when the window is resized. Export the same morph as the portfolio GIF (like Relay's logo loop).

## Test results, 18 Nov afternoon (Raynes Park drive and Cannon Hill dog walk)

- Zones work. Android caught five places across a short drive (15:40 to 15:58) and a 4.1km, 71-minute dog walk (16:33 to 17:44): beverley-brook, rp-never-a-park, rp-station (even the tight 250m zone, from the car), cannon-hill, stane-street. Each fired within seconds of entering, with Android's position at 1 to 25m accuracy (one at 127m).
- The route check on Stop and save found nothing the zones had missed. Against the GPX, the Raynes Park zones the walk didn't enter were 300 to 900m away, so no near misses.
- The first recording (15:40) stopped after two seconds: the double-tap bug, fixed in build 22.
- Content lesson: two short local trips used up every local fact in one day. From tomorrow, home days are silent until new places are added. Density of facts per area is the real constraint, as the data check predicted.
- Tonight's cards: the five passed today (four score 8, Stane Street 7), unless Tell me now runs first.
- Landing page v1 built 18 Nov evening: public/forn/index.html (+ three.js, instrument-sans.ttf) on the `forn` branch of Gandalondon/ganda, with a /forn rewrite in next.config.ts. Preview: https://ganda-git-forn-gandalondon.vercel.app/forn (not live; merge to main when Tony says push). Steps: FORN filling the screen; You pass / history / every day.; Forn / notices it / for you.; At 9pm, / find out what / you passed. (camera zooms, then an 80% overlay fades in, the line turns white, the 1889 card appears); Keep it, / or let it go. (quick burst, then floating dust); Every day / adds a ring.; Coming soon / to Android. + Try it early (mailto tony@gandalondon.com). No buttons: scroll, swipe and arrow keys. 24px edges on phones, 32px on desktop. Bottom line: © 2026 Forn, a concept by Tony Goff-Yu. Privacy (opens a centred card). A temporary Sentence case / Capitals toggle top right (review aid, remove before sharing). App burst made quicker to match.
- 18 Nov 18:45: live at gandalondon.com/forn (noindex meta tag plus X-Robots-Tag header, not linked anywhere). Decided: FORN in capitals for the word, sentence case for every line; all type SemiBold (600) to match the app. Review toggle removed.
- 18 Nov, 19:05, landing page update (live on gandalondon.com/forn, still noindex): on phones the rings draw only below the tallest heading, so lines never cross the words (desktop unchanged: headings fill the screen, so rings still sit behind them; fixing it means smaller desktop headings, Tony not asked yet). No disc at the start: steps 0 and 1 show only today's empty ring, the three finds pop in on step 2, step 5 (Every day adds a ring.) closes on the centre and grows the tree ring by ring from the oldest outwards, step 6 is now Grow yours. with Coming soon to Android. as a 19px note, then Try it early; it zooms out to the whole disc.
