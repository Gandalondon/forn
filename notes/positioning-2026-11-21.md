# Forn: release, pricing and positioning (decided 21 Nov 2026)

## Domain (21 Nov, 11:20)
- Tony bought getforn.app on Vercel (Ganda team, auto-renew on; US$9.99 first year, US$15 a year after). Same pattern as getsniff.app and gethlid.app.
- Setup on Monday, same as Hlid: holding page at the root (name, Coming soon), the full landing page at /beta until launch, email forwarding for hello@ and feedback@ through a free ImprovMX account. The landing page with the city sign-up goes live on getforn.app rather than gandalondon.com/forn, so links don't break later. gandalondon.com/forn can redirect to it.

## Release
- First release: London only (all 33 boroughs). Paid app, January, once there's enough content. Other cities later, picked by sign-up demand.
- Price: £2.99 suggested (impulse buy; Fog of World sells one-off at $30, Autio $19.99 a year). Not final.
- Outside London: the store listing says London in the name area (e.g. Forn: London's hidden history), first screenshot says London only for now, marketing aimed at London. On first open outside London: a plain message, a link to Google Play's refund, and an "I want my city" sign-up.
- Landing page gets a city field on its sign-up, so demand per city is collected before launch.
- Tony's own drives and Hlid walk areas get facts too, as a bonus for him, not part of the launch promise.

## Positioning: history, art, experience
Not a guide (you open it and browse) and not a tracker (your data on a map). A nightly piece of art about where your day went.

What's out there (store listings, 21 Nov):
- Guides: Atlas Obscura app (whole database on a map; reviews praise content, complain of slow ads and crashes).
- Live interruptions: History Near You (US only, push when near a site); Autio and Drive Stories (audio while driving, US-centred, subscriptions).
- Maps of where you've been: Fog of World ($30 one-off, people share their maps), FogMap and others leading on fully on-device privacy.
- London gap: Museum of London's Streetmuseum, Streetmuseum Londinium and Dickens: Dark London apps are unavailable.
- The closest thing to Forn, Niantic's Field Trip (passive discovery), shut in 2019.

Forn's spot: what you passed becomes the art. Delayed to 9pm (no nagging while out), at most five finds, rings as the output, nothing leaves the phone. Nobody does this, and nobody does it for London.

Lines to test: Your day, in history. / Live your day. At 9pm, find out what you walked over. / Every day leaves a ring.

Implications: rings lead in the listing and landing page, facts second; privacy in one line up front.

## Deeper research (21 Nov, 11:15)
- Fog of World (iOS): "Unlock the real world!", calls itself a real-life exploring game. $30 one-off, 4.8 from 3.1K ratings; one reviewer says expensive but worth it versus subscription rivals. Praise: makes you explore new streets, even at home; years of reliability; data carries to a new phone. Complaints: battery (background GPS), tracking stops unless the app is opened now and then, hard to edit wrong tracks. Collects no data, no accounts.
  - For Forn: (1) battery: Forn uses geofences, not constant GPS; say so ("barely touches your battery") once it's measured. (2) Reliability is a review killer: the 20 Nov zone bug (finds missed after an update) must be fixed before launch. (3) Never lose your rings: a backup or carry-over to a new phone matters to people who keep a record for years.
- History Near You (iOS, US): the closest concept to Forn (push notification when near a historical site, a collection of places you've been near, 160,000 sites). 3.4 stars from only 9 ratings. Lesson: the raw idea of "ping me near history" isn't enough on its own. Forn's difference is the execution: a few chosen finds, written well, at 9pm, turned into art.
- Autio: 4.8 from 3.6K ratings, subscriptions accepted (people pay for good location stories).
- Google Play background location (policy, 21 Nov): only allowed when it gives a significant benefit and is core to the app; must be approved through the Permissions Declaration Form in Play Console, or updates can be blocked and the app removed; applies to every release track, closed tests included. Needs a separate in-app prominent disclosure before the permission prompt, a privacy policy in the app and on the listing, and a short video (YouTube or Drive) showing the app opening, the flow to the disclosure and the consent. Play pushes minimum scope (coarse rather than fine, foreground rather than background).
  - For Forn: background location is genuinely core (it's the whole app), so the case is strong. To build before submitting: the disclosure screen (one plain screen before the system prompt: what's used, why, nothing leaves the phone), the privacy policy link in-app (How it works already has Privacy) and the video. Check whether coarse location is enough for the zones (most are 250m+), which would strengthen the case.
- Still to do: how Fog of World and Autio present their store screenshots, when Forn's listing is written.

## Landing page (agreed 21 Nov, build Monday locally on his Mac, review in Chrome)
- Keep the simple single-page design (FORN full screen, steps, hard cuts, no phone mock-ups).
- New ending, option 1: the last step zooms into a ball and a real fact card fills the screen, exactly as at 9pm (e.g. the Roman legs under Southwark's Alfred). Then one line, Coming soon to London, and the sign-up with a city field.
- Added 21 Nov 11:21 (Tony):
  - The "keeps the things you saw" step shows a few real fact cards (2 or 3, stacked plain like the app's card stack: solid white, no fade, scale or bounce), taken from the reviewed facts.
  - The small footer line (copyright, privacy) appears only on the last step, not on every step. So the opening FORN wordmark runs truly edge to edge. Privacy stays reachable on the last step (the store listing needs a privacy URL anyway).
- Lives on getforn.app/beta (holding page at the root until launch).
- Parked: a day drawing into a ring (option 2); postcode lookup showing a fact near you (option 3, after launch).
