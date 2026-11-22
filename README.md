# Forn

Go about your day. Find out tonight.

Forn quietly notes the old places you pass. Each one leaves dust on that day's ring. At 9pm it uncovers up to five of them, and their dust pulls together into black balls. One ring for each day, today in the middle.

The rulebook is RULES.md, the latest state is HANDOVER.md, and the content pipeline is PIPELINE.md. The facts are in `app/src/main/assets/spots.json`. The landing page (getforn.app) is in `site/`.

## Install on the Pixel

Add this repo to Obtainium (`https://github.com/Gandalondon/forn`), like Relay and Hlid. Each push to main makes a release called Forn with its build number.

On first open: Allow location, then Allow all the time, then notifications for 9pm.

## How it works

- Android geofences around each place. Crossing one notes the place and the time. No GPS track, no internet permission: nothing leaves the phone.
- At 9pm it picks up to five places passed that day: best first, then whichever was passed longest ago. Quiet day, no ping. Each fact once.
- Tonight's cards just page through. Tap a ball any time to read it again.
- A day runs 9pm to 9pm, so a place passed at 10pm counts towards tomorrow.

## Kept as Stepback on purpose

The package id (`com.gandalondon.stepback`), the APK file name (`Stepback.apk`) and the signing key alias (`stepback`) keep the old name so updates install over the top. Never change them.

## Signing

Same as Rinse: `SIGNING_KEYSTORE_B64` and `SIGNING_PASSWORD` repo secrets, key alias `stepback`. Without them, each build uses a one-off key and needs a reinstall.
