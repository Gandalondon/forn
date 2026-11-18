# Stepback

Live your day. Find out tonight.

Stepback quietly notes the interesting places you pass. At 9pm, one line about the best of them. Tap it for the fact, then Interesting or Not for me.

This is the v1 test: does a normal day produce a good 9pm line? It knows a hand-picked set of spots (home, the Heathrow run, Aberdeen and Portlethen, a few walks), in `app/src/main/assets/spots.json`.

## Install on the Pixel

Add this repo to Obtainium (`https://github.com/Gandalondon/forn`), like Relay and Hlid. It picks up `Stepback.apk` from each release.

On first open: Allow location, then Allow all the time, then the 9pm line.

## How it works

- Android geofences around each spot. When you cross one, Stepback notes the spot id for today. No GPS track, no internet permission: nothing leaves the phone.
- At 9pm (give or take a few minutes) it picks the best spot passed that day and posts one line. Quiet day, no ping. Each fact once.
- Interesting and Not for me are private taps. They tilt future picks towards or away from that type of fact (Roman, prehistory, geology...). Types fade, never vanish.
- A day runs 9pm to 9pm, so a place passed at 10pm counts towards tomorrow.

## Signing

Same as Rinse: `SIGNING_KEYSTORE_B64` and `SIGNING_PASSWORD` repo secrets, key alias `stepback`. Without them, each build uses a one-off key and needs a reinstall.
