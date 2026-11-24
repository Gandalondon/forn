# Play Store: steps for 24 Nov (draft, confirm with Tony)

Goal: get Forn into Play's testing tracks early, mainly to find out whether background location gets approved. Nothing public.

## Decide first (can't be undone in Play)
1. Package id. Permanent once uploaded, so rename now, not later: com.gandalondon.stepback becomes the store id (e.g. com.gandalondon.forn, or match Relay and Sniff's pattern). The store build installs beside his Obtainium one; his current app keeps its data.
   Also rename Stepback.apk and the signing key alias. Play App Signing holds the store key; we upload with an upload key (new keystore, secrets in GitHub).
2. Paid or free. A free app can never become paid later. Forn is planned as paid, so set a price from the first upload (needs the payments profile; Sniff already has one).
3. Account: company (organisation) account (Tony, 24 Nov), so no 12-tester closed test needed.

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
