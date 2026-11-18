# Forn rules

The app is called Forn (Old Norse for ancient), from 18 Nov. The repo, package id (com.gandalondon.stepback) and APK file keep the Stepback name so updates keep installing over the top.

How Stepback works: what it knows, what it tells you, and how it looks. Decisions and history live in HANDOVER.md. This file is the current rulebook: update it whenever a rule changes.

## The idea

Go about your day. Stepback quietly notes the old places you pass. In the evening it tells you the best of them. What you keep builds into tree rings of everything you've learned.

## Noticing places

- Each place (a "spot") has one or more circles around it (a geofence). Crossing into one logs the spot and the time first passed. Nothing else is recorded: no GPS track.
- No internet permission. Nothing leaves the phone.
- Circles match how a place is experienced: about 250 to 600m for something you'd walk past, 1 to 3.5km for landscape seen from a car, train or plane. The copy says near, under or passed, never "here".
- A fact that has been told drops its circle.
- Android allows 100 circles per app.

## What you're told

- A Stepback day runs 9pm to 9pm. Anything passed after tonight's line counts towards tomorrow's.
- The pick is the most interesting place passed that day, by score, among those never told before. Each fact is told once, ever.
- Answers never steer the pick (decided 18 Nov). Interesting or Not for me only decides ball or dust in the rings. Otherwise the dust would die out as the app learned your taste.
- Quiet day, no notification. Never padded.
- Up to five finds each evening, most interesting first, never padded; a home day may be one card. The notification is the best one's line ("And 2 more."). The cards wait on top of the rings until answered; until noon, last night's finds still count as today's ring.
- Repeat routes run dry by design: walk to the post office twice and the second day only pings if there's something new. Stepback is weekly-ish, busier on days you move around.

## The facts (spots.json)

Each spot has:

- id: short, unique, kebab-case.
- kind: the type of thing. One of geology, prehistory, roman, pictish, medieval, building, landscape. Add a kind only if none fits.
- score: 1 to 10, how surprising it is. 9 is a "well I never", 7 a good fact, 4 or below rarely worth telling.
- place: shown small under the fact, never above it (that would be an eyebrow).
- points: [lat, lng, radius in metres], one or more.
- line: the notification, one sentence starting "Did you know, ".
- fact: the card. Two or three short sentences, plain and specific, written for someone who has never heard of it. Lead with the surprise.
- source: where it was checked. Every fact is checked against a published source before it goes in; nothing from memory.

Next additions: an age for the thing itself (for the rings later) and the time passed, which is already stored.

## Answers

- Swipe right or tap Interesting: the find stays as a black ball.
- Swipe left or tap Not for me: it bursts into dust.
- No answer: stays as a ball.
- Answers are private and stored on the phone.

## The rings (the 3D view)

- The app is the 3D view. It opens on it, with tonight's cards on top under a dim scrim. Swipe them away and the rings are all that's left.
- Tree rings, flat: one ring per day, today the outer ring, the past at the core. Distance from the centre is the only rule for time; angle means nothing.
- The tree grows, it never squeezes: rings stay the same distance apart forever, so years become a bigger tree. Pinch out for the whole, in for a day.
- Ring weights: day a dotted hairline, Monday a step heavier, the 1st of the month heavier, 1 January darkest. Each is one solid band. A Monday within two days of a month ring stays a day ring.
- Kept finds are flat black balls, no outline, no highlight. Not for me bursts into grey dust where its ball sat.
- Tap a ball: its card comes back with the date and time.
- On open: start on today's finds, play the bursts, then pull back to the whole; the slow spin starts after.
- Zoom stops before a ball fills the screen. The title and text sit over the rings with no panel.
- Parked: tree trunk (height as the age of the thing), solar system, onion, stepped cone.

## Look

- White app. Off black #1A1A1A, never pure black.
- One font: Instrument Sans. Facts and titles SemiBold, body Regular.
- Icons: Material Symbols Rounded, one weight. Info icon top right opens How it works, a full page with a back arrow (Relay's pattern), sections 24px apart.
- Cards: white, rounded, a plain stack: the next card sits underneath, no fade, scale or bounce. Progress dots under the card.
- App icon: a white ring on off black, 38 across in the 108 grid, stroke 4, centred, sized like Rinse and Hlid.

## Setup

One ask per screen, each with its own headline:

1. Go about your day. Find out tonight. Allow location.
2. Now pick Allow all the time.
3. One quiet moment at 9pm. Allow notifications. (Once Android stops asking, the button opens the app's settings.)
4. Enjoy your day. With the count of places passed.

## Test aids (remove before anyone else uses it)

- On the How it works page, a Testing section: places passed today with times, Tell me now (runs tonight's finds early) and Record walk (GPX track and zone log to Downloads/Forn).
- Crash recorder: shows the last crash on the next open.

## Builds

- Every push to main builds Stepback.apk into a GitHub release. Obtainium watches the repo.
- Signed with the permanent key (repo secrets SIGNING_KEYSTORE_B64 and SIGNING_PASSWORD; keystore kept on Tony's Mac, never in git), so updates install over the top.
- Docs-only pushes use [skip ci].
