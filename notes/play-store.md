# Play Store: steps for 24 Nov (draft, confirm with Tony)

Goal: get Forn into Play's testing tracks early, mainly to find out whether background location gets approved. Nothing public.

## Decide first (can't be undone in Play)
1. Package id. Permanent once uploaded, so rename now, not later. Sniff is app.getsniff, Relay app.getarcrelay, Hlid app.gethlid, so Forn: app.getforn (Tony agreed 24 Nov). Done in app/build.gradle.kts: the store build passes -Pstore; the Obtainium build keeps com.gandalondon.stepback. The store build installs beside his Obtainium one; his current app keeps its data.
   Also rename Stepback.apk and the signing key alias. Play App Signing holds the store key; we upload with an upload key (new keystore, secrets in GitHub).
2. Paid or free. A free app can never become paid later. Forn is planned as paid, so set a price from the first upload (needs the payments profile; Sniff already has one).
3. Account: Ganda London organisation account (Play Console /u/1, tony@gandalondon.com; Sniff in production, Relay in open testing, Hlid draft) (Tony, 24 Nov), so no 12-tester closed test needed.

## Build changes before the first upload
- Target API 36 (we're on 35): Play's current requirement for new apps.
- Prominent disclosure screen (doesn't exist yet): a full screen before the background location prompt saying Forn uses location in the background to notice old places you pass, even when the app is closed, and nothing leaves the phone. Then the system prompts. Required for the background location form.
- Privacy policy at a real URL (getforn.app/privacy), linked in the app and the listing. Today it's a pop-up card on the landing page.
- Release build without the test tools: Record walk (foreground service, location type) and the test log screens. Dropping the foreground service avoids a second declaration.
- App bundle (.aab) from the build workflow, signed with the upload key.

## In Play Console
1. Create the app: name Forn, default language English (UK), app, paid.
2. App content: privacy policy URL, ads (none), app access (no login), content rating questionnaire, target audience (18+ or 13+), data safety (location collected, kept on device, not shared; Send my data goes to his Drive, so check if that counts for test builds only).
3. Sensitive permissions: Location permissions declaration. Core feature: at 9pm, tells you about historic places you passed that day, which needs location while the app is closed. Video (YouTube unlisted): open the app, the disclosure screen, the system prompt, allow all the time, then a 9pm notification after passing a place. Record it on his Pixel.
4. Store listing (draft, can be rough for testing): short description, full description, icon 512, feature graphic 1024x500, 2+ phone screenshots.
5. Internal testing track: upload the .aab, add Tony as tester. Then closed testing to trigger the location review.

## What needs Tony
- Package id and paid or free (step 1 and 2 above).
- Play Console access: he signs in, or I drive it in Chrome on his Mac.
- Recording the disclosure video on his phone (I'll script it, about 60 seconds).

## Progress, 24 Nov 19:12
- App created in Play Console (Ganda London account): "Forn: London History Near You" (30-character limit; "Around You" was 31), package app.getforn, English (UK), App, Paid. Tony ticked the two declarations himself. Console URL: play.google.com/console/u/1/developers/7361770906699679946/app/4975200459827088602/app-dashboard
- Dashboard tasks: privacy policy, sign-in details, ads, content rating, target audience, data safety, government apps, financial features, health, trader status, category and contact details, store listing, price (merchant account already done via Sniff).

## Proposed answers (for Tony to OK before entering)
- Sign-in: none needed. Ads: none. Government apps: no. Financial features: none. Health: none.
- Trader status: trader, same details as Sniff (the account is already declared).
- Target audience: 18+ only (paid, background location; keeps it clear of the families policy).
- Content rating: no violence, sex, gambling, drugs or user content; text facts mention historic crimes (murders, robberies) without detail, so answer the crime/violence references honestly (expect PEGI 12 or so).
- Data safety: no data collected or shared. Location never leaves the phone; nothing is sent anywhere. Only true if the store build drops Send my data and the test log (planned anyway).
- Privacy policy: done 24 Nov, getforn.app/privacy (its own page; the landing page's Privacy link goes there, the pop-up is gone).
- Category: Travel & Local. Contact email: needs a public address (hello@getforn.app needs forwarding set up; or use tony@gandalondon.com for now). Tony to choose.
- Price: Tony to decide (merchant account exists).
