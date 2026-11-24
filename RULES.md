# Forn rules

The app is called Forn (Old Norse for ancient), from 18 Nov. The GitHub repo is Gandalondon/forn (renamed 18 Nov). The package id (com.gandalondon.stepback), APK file and signing key alias keep the Stepback name so updates keep installing over the top: never change them.

How Forn works: what it knows, what it tells you, and how it looks. Decisions and history live in HANDOVER.md. This file is the current rulebook: update it whenever a rule changes.

## The idea

Go about your day. Forn quietly notes the old places you pass: each one leaves dust on that day's ring. At 9pm it uncovers the best of them, and their dust pulls together into black balls. Over time it builds into tree rings of where you've been and what you've learned.

## Noticing places

- Each place (a "spot") has one or more circles around it (a geofence). Crossing into one logs the spot and the time first passed. Nothing else is recorded: no GPS track.
- No internet permission. Nothing leaves the phone.
- Circles match how a place is experienced: about 250 to 600m for something you'd walk past, 1 to 3.5km for landscape seen from a car, train or plane. The copy says near, under or passed, never "here".
- A fact that has been told drops its circle.
- Android allows 100 circles per app, and London alone has more. So the app watches the 99 nearest untold circles plus one ring around where you are; leave that ring (half the distance to the furthest watched circle, 1 to 30km) and it picks the nearest again (21 Nov).
- Already inside counts (zone fix, 21 Nov): when the circles are set up, and again at 9pm, any untold circle you're standing in counts as passed, at the time of that fix. Android's own "already inside" trigger doesn't always fire, which is how build 46 missed places.

## What you're told

- A Forn day runs 9pm to 9pm. Anything passed after tonight's line counts towards tomorrow's.
- The pick is the nightly mix (agreed 21 Nov): among places passed that day and never told before, the highest score first; each next pick loses 1.5 for every find already picked from the same era and 1.5 for every one with the same topic. Interest still leads (a 9 from a picked era beats a 7 from a new one), but a night spreads across time. Each fact is told once, ever.
- Ties go to whichever place was passed longest ago (22 Nov), so old dust gets its turn.
- Unpicked places stay dust. Dust isn't final: pass a dusty place again on a later, quieter day and it can be uncovered then. Not being picked is the five-a-night limit, never a judgement (only reviewed facts ship).
- No personalisation and no answers (22 Nov): the app never asks whether you liked a find.
- Quiet day, no notification. Never padded.
- Up to five finds each evening, most interesting first, never padded; a home day may be one card. The notification is the best one's line ("And 2 more."). The cards wait on top of the rings until paged through; until noon, last night's finds still count as today's ring.
- Repeat routes run dry by design: walk to the post office twice and the second day only pings if there's something new. Forn is weekly-ish, busier on days you move around.

## The facts (spots.json)

Each spot has:

- id: short, unique, kebab-case.
- kind: the type of thing. One of geology, prehistory, roman, pictish, medieval, building, landscape. Add a kind only if none fits.
- score: 1 to 10, how surprising it is. 9 is a "well I never", 7 a good fact, 4 or below rarely worth telling.
- place: shown small under the fact, never above it (that would be an eyebrow). Cards show only the area (22 Nov): the part after the last comma, without a house number (Barclays, Enfield shows as Enfield; 145 Piccadilly as Piccadilly). Tell me more still uses the full place.
- points: [lat, lng, radius in metres], one or more.
- line: the notification, one sentence starting "Did you know, ".
- fact: the card. Two or three short sentences, plain and specific, written for someone who has never heard of it. Lead with the surprise.
- source: where it was checked. Every fact is checked against a published source before it goes in; nothing from memory.
- year: when the thing in the fact happened (rough is fine; negative for BC). Era comes from it: prehistory (before 43), roman, saxon (410), medieval (1066), tudor (1485), stuart (1603), georgian (1714), victorian (1837), early-20c (1901), late-20c (1945), 21c (2000).
- topic: one word from war, transport, music, film, comedy, sport, royals, people, politics, law, science, invention, design, buildings, art, books, religion, names, traditions, everyday, work, shops, animals, nature, secrets, ancient, crime (added 22 Nov).

## Writing rules (confirmed by Tony, 21 Nov)

1. The single most interesting, surprising fact about the place. Aim for whoa, not merely amusing.
2. Every claim in the notification and the card is in the source.
3. History, not horror (revised 22 Nov). Crime, robberies, gangs, scandals (sex scandals included), executions, a famous person's death or murder are all in: grim but fascinating is fine when it's history (Execution Dock, the coffin trains). Out: recent tragedies with real victims (fatal crashes, disasters, terror attacks), ghosts of victims, gore and anything explicit. Still out: restaurants and "described as" quotes.
4. Drop anything that makes you ask "why does it matter?"
5. The notification states the fact ("Did you know, ...").
6. One fact per card: the card explains the notification's fact more fully; never a second fact.
7. Name the kind of thing plainly (the band, a Camden pub, an oak tree, an English army).
8. Don't name people who'd need explaining.
9. No jargon, odd phrasing, old or foreign words, or places locals wouldn't know. Round numbers.
10. Give the cause if the source has it.
11. Aim for 35 words or under.
12. A fact that needs local or background knowledge to land is out. A card rejected twice is dropped, not rewritten again.
13. Every fact keeps its source text (in the content pipeline's files).
14. Film, TV and music count when they've become history (22 Nov): where a band formed or played its first gig, a famous scene filmed on a street you'd walk past, from about 25 years ago or more (the 1989 Batman, not the 2022 one). Recent filming trivia is out. Aim for a modern mix: some 1960s to 1990s finds dotted among the older ones.

## Reviews (21 Nov)

- Tony can't check every fact. Reviews are nights: four nights of five finds along a realistic day, mixing eras, about half new and half already passed. He keeps or rejects each card and rates each night good or flat.
- One review per new area or roughly every 60 new facts. Under 1 in 5 rejects and the area's unseen facts ship.
- A blind grader agent agreed with Tony only about 2 in 3, so it's an optional editor pass, never a gate.

## Cards (22 Nov)

- No keep or Not for me. Tonight's cards just page: swipe left or tap for the next, swipe right for the one before, or tap a pip. Past the last card (or Android's back) they're done and don't come back.
- No answers are stored. Answers from before 22 Nov were removed on the first open of the new build (a night already answered counts as seen).

## The rings (the 3D view)

- The app is the 3D view. At 9pm it opens close on today's ring: the uncovered places' dust pulls together into balls, then tonight's cards fade in on top under a dim scrim. Page through them and it pulls back to the whole.
- Tree rings, flat: one ring per day, today in the centre, older days rippling outwards (19 Nov). Distance from the centre is the only rule for time. Angle is the time of day you passed the place, like a clock face (midnight at the top), with a small nudge so nothing lines up.
- The tree grows, it never squeezes: rings stay the same distance apart forever, so years become a bigger tree. Pinch out for the whole, in for a day.
- Ring weights: day a dotted hairline, Monday a step heavier, the 1st of the month heavier, 1 January darkest. Each is one solid band. A Monday within two days of a month ring stays a day ring.
- Dust is what you pass (22 Nov): every place passed leaves a small pinch of round grey specks (70) on that day's ring, by the time you passed it. Today's ring appears with its first dust. Lots of dust means you walked through lots of history.
- Balls are what you've uncovered: flat black, no outline, no highlight. At 9pm an uncovered place's pinch pulls together into its ball. Where a place was uncovered, its dust on that day became the ball; its dust on earlier days stays.
- Dust and balls are one round shape at two scales: a place you pass is a cloud of tiny balls, an uncovered find is one big readable ball pulled out of the mess. Only scale and gathering change.
- Tap a ball: its card comes back with the date and time, and a Tell me more button. That opens Android's share menu with a ready-made question about the place ("Tell me more about X in the UK. I learned that: ... What else is worth knowing about it, and about what's nearby?"), for an AI app, a search or notes. No setup, no AI connection, no internet permission. Only on reopened cards, so the evening stays quick.
- Any other open: the whole, with the slow spin.
- Back home (22 Nov): no centre button. After 6 seconds untouched, the view eases back to the whole disc and the slow spin carries on; never while a card or How it works is open. Double-tap the rings to go back at once.
- Zoom stops before a ball fills the screen. The title and text sit over the rings with no panel.
- Parked: tree trunk (height as the age of the thing), solar system, onion, stepped cone.

## Look

- White app. Off black #1A1A1A, never pure black. No colour: colour by period (modern, medieval, Roman, prehistoric, geology) was considered on 18 Nov and parked, as it answers no question anyone asks and there's no filter.
- One font: Instrument Sans. Facts and titles SemiBold, body Regular, links Medium (500) everywhere, app and site (Tony, 24 Nov).
- Icons: drawn on a 24 grid, 1.5 round-capped stroke (matches the Material back arrow's weight; set 21 Nov, same in Hlid), shown at 28px in ink (21 Nov: Hlid's notes-page icon replaced the Material info icon so both apps match; the back arrow stays the standard Material Symbols arrow, same as Hlid). The notes icon top right opens How it works, a full page with a back arrow (Relay's pattern), sections 24px apart.
- Cards: white, rounded, a plain stack: the next card sits underneath, no fade, scale or bounce. Progress dots under the card.
- App icon: an off-black ring on white, 38 across in the 108 grid, stroke 4, centred, sized like Rinse and Hlid.

## Brand (18 Nov)

- Two marks, never locked up together. The ring is the fixed symbol: app icon, notification, favicon. The word FORN is elastic: Instrument Sans, one weight, off-black or white, always filling whatever space it's given edge to edge, square, wide or tall. It's never wrong for being narrow or wide.
- Width before stretch: narrow or widen the letters with the font's width axis first, then stretch the rest, so tall versions look designed, not broken.
- Never inside a containing shape: the space it fills is its shape.
- Past a limit (very tall and thin, or a tiny strip) it gives way to the ring.
- The story: everyone's rings differ, and the word takes the shape of wherever it lives. Precedent: the Whitney Museum's responsive W.

## How it works copy (approved 22 Nov)

- Dust: Every place you pass leaves dust on that day's ring: history you haven't uncovered yet. Lots of dust means you walked through lots of history.
- Balls: Each night Forn uncovers up to five places, and they become black balls. Tap one to read it again. Pass the dusty places again to uncover more. One ring for each day, today in the middle.

## Setup

One ask per screen, each with its own headline:

1. Go about your day. Find out tonight. Allow location.
2. Now pick Allow all the time.
3. One quiet moment at 9pm. Allow notifications. (Once Android stops asking, the button opens the app's settings.)
4. Enjoy your day. With the count of places passed.

## Test aids (remove before anyone else uses it)

- On the How it works page, a Testing section: zone status, Record walk (GPX track and zone log to Downloads/Forn), Show six months (example finds and dust, in memory only) and Send my data.
- Crash recorder: shows the last crash on the next open.

## Builds

- Every push to main builds a release named Forn and its build number, with the APK file still called Stepback.apk (see the top of this file). Obtainium watches the repo.
- Signed with the permanent key (repo secrets SIGNING_KEYSTORE_B64 and SIGNING_PASSWORD; keystore kept on Tony's Mac, never in git), so updates install over the top.
- Docs-only pushes use [skip ci].
- Vercel deploy budget (22 Nov): the free plan allows 100 deploys a day across ALL Tony's projects, and cancelled or skipped builds count. Prefer [skip ci] and batch pushes to main (one push for a session's content and notes, not one per file).
- The site (getforn.app) deploys only through the Site job (.github/workflows/site.yml): on pushes to main that touch site/, or run by hand. It stops at 95 deploys in 24 hours. Vercel's own Git deploys for main are off (site/vercel.json). Preview branches still deploy on every push, so use them sparingly.
