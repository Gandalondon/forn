# Forn

Forn is Tony's Android app that tells him at 9pm about old places he passed that day, collected on flat tree rings.

## Every session

- Read HANDOVER.md (latest section at the top), then RULES.md, before doing anything.
- Work GitHub first; Tony's Mac is a fallback.
- Run only one session at a time on Forn.
- Before a session ends, update HANDOVER.md with decisions, current state, where files are, and anything agreed but not built yet.

## Where things are

- App: app/ (Kotlin plus the rings page in app/src/main/assets/web). Every push to main builds a release Tony installs through Obtainium.
- Landing page: getforn.app, in site/ (Vercel, unindexed).
- Content pipeline: PIPELINE.md and tools/pipeline. Fact drafts and their source text: content/facts/ (spots.json is the shipped set, built from them).
- Notes: notes/ (review logs, grader, nightly mix, positioning, session notes).
- The claude.ai Forn Project holds only the open review page (batch 11), whose answers are saved on its artifact.
- Kept as stepback on purpose: package id, APK file name (Stepback.apk) and signing key alias. Don't change them now (Tony's installed app would lose its data and Obtainium updates). Before the Play Store release, rename all three to Forn (Tony, 23 Nov): the store app is a fresh install anyway.

## Forn rules

- Up to five finds a night, best first, then whichever was passed longest ago. No personalisation and no answers.
- Every place passed leaves dust on that day's ring; at 9pm the uncovered places' dust pulls together into flat black balls.
- Today in the centre, older days ripple outwards, each ball placed by the time he passed it.
- Black and white only. Off-black, never pure black.
- Instrument Sans for everything, all body text black.
- FORN in capitals as the wordmark, stretching to fill its box, no logo lockup.
- Hard cuts, no text animation. No fake notifications in prototypes.
