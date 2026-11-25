# Forn handover

### Latest: Tue 24 Nov 2026, 23:45

### Next session starts here (24 Nov, 23:45)
- Trailer v2 built (branch rings-grow): one continuous camera move, tools/trailer/film.html + film.py (python3 tools/trailer/film.py h stills 2.5 12 ... for stills; python3 tools/trailer/film.py h <black-veil.mp3> for the video, music laid under at -16 LUFS). Words cut on Black Veil's hits: You pass history every day. 0.5s, Forn notices it for you. 4.13s (balls 5.06, 5.52, 5.99), At 9pm, see what you missed. 7.36s, cards land 11.05, 14.28, 18.44 (2s each, flip left of the ball if they would cover another), Every day adds a ring. 21.66s (rings arrive, camera pulls back), Grow yours. 24.43s, end card 25.82s. Constant slow turn (0.13 rad/s), sine glides, past balls fade behind the words.
- v3 (Tony 23:47): today's balls placed on the right of the ring while words are up (no fading); after At 9pm the ring glides to the middle and the camera keeps turning (clockwise, 0.3 rad/s); each card rises above the ring from its ball as it reaches the front (11.05, 14.28, 18.44); hard cut Grow yours. to the end card at 25.82s. Re-rendered, sent 23:55.
- Dropped: The rest is dust, for now. (no room in 30s); Coming soon to London. (Tony 23:39: the app is out when the trailer is).
- Render: marketing/forn-trailer-16x9.mp4 (not in git, sent in chat 23:45). Waiting for Tony's notes. Then 9:16 (film.html needs a portrait layout: words top, rings below). Uploads don't carry over: ask Tony to re-attach Black Veil.
- 25 Nov 00:44 data export (Drive, Forn data, saved outside the repo): phone is still on build 64; the re-pick loop fix is in build 65 (22 Nov 23:16), so the 4-minute loop is still running (397 re-picks in 21 hours). Tony to update in Obtainium; check the next export for "ignored" lines. Otherwise fine: hounslow-baseline passed 23 Nov 21:33 (after the 9pm line, so it counted for 24 Nov) and was told at 21:07 on the 24th.
- Tony 00:46: he didn't pass Hounslow Heath (nearest circle 51.4263, -0.3662, by Whitton, about 9 km from SW20). The pass itself fell off the 800-line log, so no fix to check. Likely a rough network fix firing an enter, with the 4-minute re-pick loop re-arming every zone. Build 66: enters only count with a fix of 200m or better within radius + accuracy + 100m of the circle (else logged passed? ... ignored). Rule in RULES.md.
- Still open from 20:55: site preview rings-grow waiting for Tony to say live; Play store listing, then the store build.

### Earlier: next steps as of 24 Nov, 20:55
- Trailer: rebuild as one continuous camera move in the style of the approved orbit test (tools/trailer/orbit.html, orbit.py, branch rings-grow): dust drifts in, today's balls appear, glide to each find with its off-black card attached (line into the card, white place name), constant slow turn, long sine glides, pull back out to the massive rings, end card (ring, getforn.app under it, Google Play badge bottom right, trademark line bottom left, Sniff's sizes). Words only on Black Veil's beats (music: /mnt uploads are gone in a new chat; ask Tony to re-attach Black Veil, Universfield, Pixabay 386555). 16:9 first, then 9:16.
- Site preview branch rings-grow (https://forn-git-rings-grow-gandalondon.vercel.app/): wide-screen heading cap, always turning, balls appear not grow, dust keeps floating, rings arrive with their balls, balls fade behind the words. Waiting for Tony to say live. Then maybe the attached card at 9pm on the site too, if the trailer version works.
- Play: everything done except the store listing (descriptions, icon 512, feature graphic, screenshots), then the store build (target API 36, disclosure screen, no test tools, signed .aab) and internal testing.


### Update, Tue 24 Nov 19:50
- Play Console (Forn, Ganda London account): every setup task done except the store listing (needs art and copy). Nothing sent for review. Saved: privacy policy getforn.app/privacy; sign-in not needed; no ads; target audience 18+ only (minor-blocking option left off); content rating done (IARC, contact hello@getforn.app, All other app types; honest answers: realistic violence referred to, no gore; references to sexual activity without detail; alcohol and tobacco referenced rarely; educational yes; no online content). Result PEGI 3, ESRB Everyone 10+. Data safety: no data collected or shared (ONLY true once the store build drops Send my data and the test log). Government no, financial features none, health none, trader yes (inherited, no Terms URL). Category Travel and local, contact hello@getforn.app, site https://getforn.app. Price: £2.99 in the UK including VAT (set by hand; the bulk set made it £3.59), other countries converted from £2.99 before tax.
- Privacy page rebuilt (Tony, 19:38): Hlid's layout (one centred 752px column, big title, small headings, body 20/32), Instrument Sans, the app icon's ring top left linking home (and as favicon) instead of the FORN wordmark, headings at Hlid's section size (28 to 40px, Tony 19:47), only h1, h2 and body (no lede), sections and wording as gethlid.app/privacy: Who we are (made by Tony Goff-Yu, run by Goff & Associates Limited; Tony 19:52: all his apps are, unless stated otherwise), On your phone, Your location, What leaves your phone, Other services (Vercel logs, Google Play purchase), Deleting your data, Feedback, Last updated, footer identical to the landing page's bar (13/18, Regular grey, link Medium ink). Live on getforn.app/privacy (Tony said live 19:56; privacy-hlid merged to main).
- Trailer stills rendered (tools/trailer/stills/, h-*.jpg). To fix before full renders: at 9.5s the balls sit on "missed."; at 12s the card covers the heading; at 19s a ball touches "ring." and the rings crop at the bottom; dust at 4s and on the end card (26s) is very faint; Coming soon to London. is tiny at 24s. Also: the end card pulls together a filled ball, but the app icon is a ring (ask Tony which the end card should be).
- Links Medium (500) everywhere (Tony 19:56), privacy page live and RULES.md updated.
- Landing step 5 (Tony 19:58): each day's ring now grows out of today's ring, first five one by one (0.38s apart), the rest by 4s, 0.6s ease-out each; balls stay round. Branch rings-grow, preview https://forn-git-rings-grow-gandalondon.vercel.app/ (step through to Every day adds a ring). Trailer ring beat 5.4 to 6.2s (on that branch). Merge when Tony says live.
- Trailer fixes (24 Nov 20:20, branch rings-grow): wide screens cap headings at min(10.5vw, 24vh) so you missed. ends before the 9pm card (site change too, it collided on every 16:9 laptop); growing rings stay bare (no balls or dust) on step 5 and until the camera settles on step 6; trailer-only: dust specks 1.8x (window.__DUST), end card dust pulls into the app icon ring (stroke 4/38), note 28px. 16:9 rendered to marketing/forn-trailer-16x9.mp4 (not in git, sent in chat), no music. Music (Tony sent 20:22, Pixabay): Black Veil 30s (Universfield, 386555) plays whole from 0, its own fade lands on the end card; Phaseform (Sam Kamau, 563296) is 23.7s with a hard stop, so it runs into a second pass (1.5s crossfade) and fades out from 27.3s. Both loudness-normalised to -16 LUFS. Files: marketing/forn-trailer-16x9-black-veil.mp4 and -phaseform.mp4 (not in git, sent in chat). PICKED (Tony 20:26): Black Veil. Trailer changes 20:28 (branch rings-grow, video only via window.__VIDEO, __NEAR 0.72, __WIDE [-0.14,-0.06], __DUST 1.8): everything turns slowly on every step, balls just appear in their dust (no growing, dust keeps floating), rings appear one after another (growing ripple dropped, Tony: no pulsating), today's ring nearer and up-left (overlap with words is fine, Tony), end card is just the app icon ring at Sniff/Relay mark size (about 84px on 1080) with a 0.2s fade. Render: marketing/forn-trailer-16x9-black-veil.mp4. Tony: the site should get the same always-moving, balls-appear feel next (not done). 20:38 round (Tony 20:33): balls never on the words (rings and dust may overlap): today's balls at 23:00, 2:30, 6:00 so they sit right of the ring; balls ease in (0.4s opacity); 9pm keeps step 2's shot (no zoom) and the three finds land on top of each other at 0.6s (beat 3.6s); steps 5-6 the tree grows lower right, each ring with its balls, camera pulls back with it (view offset glides); rings eased in-out; end card: ring with getforn.app under it, Google Play badge bottom right, trademark line bottom left (Sniff's sizes; badge copied from sniff src/tools/trailer). 29.4s. Render: marketing/forn-trailer-16x9-black-veil.mp4. 20:43: steps 5-6 hold the close shot (huge rings, no zoom-out, Tony liked the site's massive rings), past balls fade behind the words. Tony 20:43: the video still doesn't feel polished: it's the site played on a timer (text popping in per step). Idea on the table: one continuous camera move, the fact as a 3D tooltip attached to its ball while the camera orbits it; prototype in the video first, port to the site only if it works. 20:47: site synced on rings-grow (always turning, balls appear not grow, dust keeps floating, rings arrive with their balls eased, balls fade behind the words); orbit test built: tools/trailer/orbit.html + orbit.py -> marketing/forn-orbit-test.mp4 (5s: wide to ball A, off-black card attached top right of the ball with a leader line, 0.2s fades, swing to ball B). Tony 20:51: conceptually works, too snappy. v2 (20:55): camera turns at one constant slow speed throughout, target glides are long sine in-outs (no stop-start), line runs from the ball edge into the card's bottom edge, place name white, 6.5s. APPROVED (Tony 20:55: a lot smoother, very nice). Next: rebuild the whole trailer as one continuous move (dust, balls appear, glide to each find with its card, pull back as rings grow, end card), words only on Black Veil's beats. Site to follow (Tony): always turning, balls appear and arrive with their rings. Next: 9:16 with Black Veil.
- Next: store listing (short and full description, icon 512, feature graphic, 2+ screenshots), then the store build (target API 36, disclosure screen, no test tools, signed .aab), internal testing.

### Update, Tue 24 Nov 19:30 (end of session)
- Play Console: Forn created in the Ganda London account (Chrome /u/1, tony@gandalondon.com): "Forn: London History Near You", app.getforn, English (UK), paid. Store build id via -Pstore in app/build.gradle.kts (Obtainium build keeps com.gandalondon.stepback). Setup tasks and proposed answers: notes/play-store.md.
- Privacy page live at getforn.app/privacy (pop-up removed; footer links to it). Contact everywhere is hello@getforn.app (Tony set up forwarding 24 Nov).
- Waiting on Tony: yes/no to target audience 18+ and the honest content rating (crime mentions); the price. Then fill the Play setup forms (stop before anything is sent for review).
- Still to build for the store: location disclosure screen, target API 36, store build without Send my data / Record walk / test log, signed .aab with an upload key, listing art, the declaration video script.
- Trailer: tools/trailer/ written but not rendered; render stills first. Music: Tony picking on Pixabay.
- Landing (24 Nov): longer lens (FOV 22) so balls don't stretch; city form clears the heading.

### Update, Tue 24 Nov 19:10
- Trailer (Tony asked 24 Nov 09:47): the landing page played as a linear video, 16:9 and 9:16, copy taken from site/index.html so it stays in sync with the page. End card like Hlid's: white, the app icon's black ball pulls together from dust in the middle, getforn.app at the bottom. Files: tools/trailer/ (render.py, clock.js virtual clock, video.css). Written, NOT rendered or checked yet. Next: render stills (python3 tools/trailer/render.py h stills 1 4 7.5 9.5 12 15 19 24 26 28.5), fix, then full renders to marketing/.
- Music: Tony is choosing on Pixabay Music (where Relay's came from: Jonas Blakewood synthwave, Pixabay 618632). Brief: airy, spacey, ambient electronic with a slow pulse; about 30 s tracks that build to the end card. He sends two or three, render one version per track.
- Play Console: Chrome on his Mac is signed in as goff.tony@googlemail.com, which has no developer account (opens the sign-up page; don't create one). Forn goes in the Ganda/GetSniff company account under tony@gandalondon.com (where Sniff and Relay live): switch Chrome's Google account first. Sniff's package id pattern is app.getsniff, Relay's app.getarcrelay, so Forn's is app.getforn (confirm with Tony).

### Play Store, 24 Nov (Tony, 23 Nov 23:58): get it into Play's testing tracks to check background location approval. Steps: notes/play-store.md

### Before the store release (Tony, 23 Nov)
- Rename the stepback leftovers to Forn: package id, APK file name (Stepback.apk), signing key alias. Not before: it would break his installed app and Obtainium.

### Update, Mon 23 Nov 23:50: London dust map test for the landing page (not live)
- Tony asked whether to add a styled London map. Agreed: not in the app (it turns Forn into a tracker, shows where people live, shows thin coverage); try it on the landing page.
- Test: https://claude.ai/artifact/5pBSyAAGuZTTh2H6ckDGem (private). 90,000 grey dust points in Greater London's shape (boroughs geojson from github.com/radoi90/housequest-data), the Thames left empty (hand-placed centreline), dust standing a little taller towards the centre. One example day: pinches of darker dust where places were passed (no route line) and three black balls (Enfield, St James's Park, Green Park, the landing page's three finds). No real coverage dots (they'd show Tony's SW20 cluster and the gaps).
- Files: tools/site/london-map/build_dust.py (makes the data), preview.html (the test page). Dropped by Tony (23 Nov 23:54): no map on the landing page either. Files kept, parked, in case it ever comes back.

### Update, Sun 22 Nov 23:20
- Re-pick loop bug (found in Tony's 22 Nov data export, saved outside the repo): "left the watched area" fired every 4 minutes for 24 hours at home (388 times, from 21 Nov 23:16), re-picking 100 zones each time. Fix in Fences.leftArea + Receivers: only an EXIT counts, Android's own fix must be clearly outside the remembered ring, and at most one re-pick in 10 minutes unless he's moved 2km+. Each leave is now logged with distance, ring size and fix accuracy, and a stale centring fix (30+ min old) is logged. Check the next export: the log should show "ignored" lines or real leaves, not a 4-minute loop. If the loop persists with "km from the centre" in the hundreds, the zone centre is a stale fix (Aberdeen).
- Today's ring now shows from 9pm even on an empty day (Tony agreed 23:13). Before 9pm it still waits for the first dust.
- Landing page steps re-timed (Tony): 1 You pass history = dust appears; 2 Forn notices it = the three balls pull together one after another; 3 At 9pm = zoom in, then the card. Pushed; the Site job skipped (96 of 100 Vercel deploys used). The scheduled 16:05 rerun on 23 Nov will deploy it.


### Update, Sun 22 Nov 16:15: batches 13 to 15 reviewed and shipped
- Tony reviewed all three at 16:00. 58 of 60 kept, every night good. 34 facts ship: spots.json now 218. Details: notes/review-log-3.md.
- beatles-rooftop shipped with the last sentence removed (Tony's note); trident-hey-jude held back (Confusing).
- No review pages open now. Next: Tony's three pipeline decisions (notes/faster-pipeline.md), the go bar (notes/replay-test.md), Record walk GPX. Then the first area run (5 to 10km ring).


### Update, Sun 22 Nov 16:05: Vercel deploy budget fix (as done for Hlid)
- On 22 Nov the free plan's 100 Vercel deploys a day (all projects, cancelled ones count) ran out: Forn 40, Hlid 59.
- Now: getforn.app deploys only through the Site job (.github/workflows/site.yml, copied from Hlid's), on pushes to main touching site/, or by hand (Actions, Site, Run workflow). Skips at 95 deploys in 24 hours. Repo secret VERCEL_TOKEN (forn-github, expires 22 Nov 2027).
- site/vercel.json: Git deploys for main off. Build APK ignores the Site workflow file.
- Rule added to RULES.md (Builds): [skip ci] and batched pushes; site deploys via the Site job only.
- The budget was used up until about 15:45 on 23 Nov, so the first Site run may fail with api-deployments-free-per-day: rerun it after that. Checked 23 Nov 16:06: Site job run by hand, 3 deploys in the last 24 hours, deployed forn to production (READY, aliased to getforn.app). The landing page re-timing from 22 Nov 23:15 is live.


### Update, Sun 22 Nov 13:45: all four 13:20 items done; sync with Tony at 11pm
- Three review pages waiting, any order: batch 13 (https://claude.ai/artifact/324WRsSff9kqxHBghdYAY4), batch 14 outer London (https://claude.ai/artifact/2NmRPAc1s2xnnN3gsZ9s4o), batch 15 the six held-back stories plus four (https://claude.ai/artifact/JoBwsopm2wkrKWNYMMyP8W). When he says one is done: read review-batch-N, add passing facts to spots.json, log in notes/review-log-3.md, push (builds the APK). Batch details: notes/review-log-3.md.
- Held-back locations: found for all six (sources in content/facts/sources-london-batch15.json).
- Faster pipeline plan: notes/faster-pipeline.md (area runs of about 100 facts overnight, scripted gate, Tony reviews 12 random new cards per area, ships at 0 or 1 rejects). Three decisions for Tony at the end of that file.
- tools/pipeline/lint.py: rule lint (words, line start, banned words, hedges, points, same topic within 300m).
- 11pm agenda: (1) review pages; (2) the go bar (notes/replay-test.md); (3) the three pipeline decisions; (4) a week of Record walk GPX for the replay test.


### Update, Sun 22 Nov 13:35: batch 14 drafted, replay test built (items 2 and 3 of the 13:20 list)
- Batch 13 still waiting for Tony. When he says "batch 13 done": read review-batch-13, add passing facts to spots.json, log in notes/review-log-3.md, push (builds the APK).
- Batch 14 (outer London) built and waiting too: https://claude.ai/artifact/2NmRPAc1s2xnnN3gsZ9s4o (answers in review-batch-14). 13 new facts plus 7 passed. Files: content/facts/london-outer-batch14.json, sources-london-outer-batch14.json, content/review/batch14-nights.json. Details and things to watch in notes/review-log-3.md.
- Go/no-go replay test: tools/replay/, results and proposed bar in notes/replay-test.md. Today (weeks 3 to 8): a central commuter's days out get a find 18% of the time, an outer Londoner's 26%; Tony's 29%. Simulated people, not real tracks (no London tracks exist yet; a week of Record walk GPX would make the Tony one real). Rough answer: the centre needs about 1,000 to 2,000 more facts; outer London needs its own push; Tony's country walks need Surrey content. Proposed bar (Tony to agree): 75% of central days out, 50% of outer, 5+ finds a week.
- Still open from the 13:20 list: (1) map locations for the six held-back stories; (4) the faster pipeline plan.

### Update, Sun 22 Nov 01:40: dust in the app (branch dust-app, merged to main)
- Built as decided 22 Nov: dust is what you pass. Every place passed leaves a pinch (70 round specks, as the landing page) on that day's ring by the time passed; today's ring appears with its first dust. At 9pm the app opens close on today: the uncovered pinches pull together into balls (about 1.4s), then the cards fade in. Cards just page (swipe left or tap for next, right for back, pips are buttons); past the last card, or Android back, they're seen for good and the view pulls back.
- Pick: best first, then whichever was passed longest ago (Store.firstPassed), inside the nightly mix. Unpicked places stay dust and can be uncovered when passed again.
- Removed: swipe verdicts, Store verdict functions, the bridge verdict(). First open of the new build runs Store.dropAnswers(): answered nights count as seen, v_ keys deleted. New bridge seen(day); state() now sends dust (every passed place by day and time, minus the night it was uncovered).
- How it works: Swipe and Keep replaced by the approved Dust and Balls copy. Tally: N uncovered. The rest is dust, for now. Tap a ball to read it again. Before any find: Dust from N places so far. Find out at 9pm.
- first-atm in spots.json: You used -> People used (as the landing page).
- Browser preview (branch dust-app-preview, never merge): https://forn-git-dust-app-preview-gandalondon.vercel.app/proto/app plays an example 9pm with a month of example rings; reload to replay.
- 22 Nov 08:50, name sweep: every Stepback in copy, docs, comments, theme, Gradle project and release name is now Forn (README rewritten for the current app). Kept on purpose: package id, Stepback.apk, key alias stepback, keystore file. History below still says Stepback where it was the name at the time.
- 22 Nov 08:40 to 08:45: cards show just the area (Enfield, Green Park); view eases back home after 6s untouched, double-tap goes now (builds 55, 56).
- 22 Nov 08:55, tidy: Project instructions replaced (Tony pasted them: HANDOVER.md is the master, getforn.app, dust rules). Deleted from the Project: tools/pipeline/ (copies of tools/pipeline), both patches, look-test, review batch 1 page, HANDOVER-2026-11-21.md. Branches dust-copy, footer-last, proto-dust and rings-centre are merged or dead but could not be deleted from the cloud (GitHub blocks branch deletes from these sessions); harmless, delete from the GitHub branches page or from the Mac some time. Fact and source files still live in the Project (content/facts/); moving them into the repo is still to do.
- 22 Nov 09:05, moved from the claude.ai Project into the repo, byte for byte: 20 fact and source files to content/facts/, 8 notes (review logs, GRADER, grader test, nightly mix, positioning, 20 Nov session) to notes/. Paths updated in CLAUDE.md, HANDOVER.md and the notes. Project copies deleted; the Project keeps only the batch 11 review page until its answers are in.
- 22 Nov 09:08, rule 3 revised (Tony): it was never meant to ban death outright (the coffin train fact is one of the best). Now: nothing grim. A famous person's death or murder and robberies are fine; fatal crashes, disasters, victims and ghosts are out; restaurants and "described as" quotes still out. 09:10: crime, robberies, gangs and scandals (sex scandals too) are in, nothing graphic or explicit. Earlier drops made under the old wording (e.g. putney-vale-bullet, the Savoy burning) can be looked at again.
- 22 Nov 09:11, rule 14 (Tony): film, TV and music in when they've become history (about 25+ years: where bands formed or played, famous scenes filmed); recent filming trivia out. Batch 12 leans 1960 to 2000 and uses this plus the revised rule 3 (crime, gangs, scandals in).
- 22 Nov 09:14, rule 3 again (Tony): grim but fascinating is in when it's history (Execution Dock at Wapping: pirates left hanging until three tides had washed over them). Out: recent tragedies with real victims, ghosts, gore, explicit. Film example he liked: the Old War Office on Whitehall played MI6 in 1980s Bond films (to verify with a second source).
- 22 Nov 09:20, batch 12 built (13 new modern facts plus 7 passed, four nights): https://claude.ai/artifact/5GUwCdnc9tErfTjHpZTKJ7, reviewed 09:22: 19/20 kept, all nights good, nothing too grim; 12 new facts in spots.json (184), beatles-rooftop rewritten for the next batch. Details in notes/review-log-3.md. Review page is now a reusable template: tools/review/template.html plus build.py. Target agreed for launch: about 2,500 to 3,000 London facts (161 now); test with the go/no-go replay before January; clustering by area is fine (Soho should feel different from Westminster).
- 22 Nov 10:38, batch 13 built (11 new modern facts, the Beatles rewrite, 8 passed): https://claude.ai/artifact/324WRsSff9kqxHBghdYAY4, waiting for Tony. Details in notes/review-log-3.md.
- 22 Nov 13:20, waiting on Tony for batch 13 (late Mon 23 or Tue 24 Nov). Can be done meanwhile, no feedback needed: (1) find map locations for the held-back stories (Marquee, Hatton Garden, Knightsbridge deposit robbery, Notting Hill, Heddon Street, Brink's-Mat), e.g. from Historic England list entries; (2) draft batch 14, aimed at outer London, where coverage is thinnest; (3) build the go/no-go replay test (real weeks of passes run against spots.json: how many outings get a find); (4) plan the faster pipeline (sampled reviews) to reach about 2,500 to 3,000 London facts.
- Known: passes after 9pm (and before noon the next day) don't show until today's ring rolls over at noon.


### Update, Sat 21 Nov 23:58: getforn.app is live
- Tony's call: no holding page. The Forn page as it was on gandalondon.com/forn (today still on the outside) is the home page of getforn.app. Kept out of search (meta noindex plus an X-Robots-Tag header in site/vercel.json) until launch.
- Lives in this repo: site/ (index.html, three.js, instrument-sans.ttf, vercel.json). Vercel project "forn" (gandalondon team, prj_7wmQ0qd9AfxyaC1LoBbpTXGgu2Ou), root directory site, deploys on every push to main. www.getforn.app redirects to getforn.app.
- build.yml now ignores site/** and *.md, so site and doc pushes don't make a new APK.
- Vercel connector is connected and authorised for the gandalondon team, so domain, DNS and deploys can be done from the cloud.
- 22 Nov 00:01: gandalondon.com/forn now redirects (308) to getforn.app; the old copy in the ganda repo is removed (ganda commit 9d06050). Credit line and Privacy only on the last step (FORN edge to edge): live 22 Nov 00:05. ImprovMX: TBC by Tony.
- 22 Nov 00:20, branch rings-centre (preview sent to Tony, not live): today in the centre with clock-face balls; rings clear of the words on wide screens; 9pm step shows three real kept finds (Waterloo coffin train, Leadenhall basilica, the king's white bear) as a plain card stack with pips, swipe or tap, rings glide to each ball; Grow yours is now just the wide disc (drag to turn); new last step zooms into an old ball, Coming to London., the Alfred Roman legs card and a city field (Tell me opens an email to tony@gandalondon.com, subject Forn in <city>; Tony: Ganda address for now). Checked at 390 and 1440 wide. Open: on phones At 9pm, find out what you passed. breaks onto five lines; suggested At 9pm, see what you passed.
- 22 Nov 00:30, rings-centre updated (Tony: facts same length so the box doesn't change size, mix the eras): 9pm cards are first-atm (1967), holborn-power (1882), foyles-mein-kampf (1940), all about 150 characters, card height locked to the tallest; ending card is bomber-command-roof (1944/1997). Heading now Find out / at 9pm. (two lines on phone and desktop). Hyphenated words never break in cards.
- 22 Nov 00:40, rings-centre updated (Tony: no "you" in facts, never two "the world's first", Find out at 9pm. too reduced): heading At 9pm, / see what / you missed. (three lines everywhere; phone headings now 15vw so it fits); 9pm cards first-atm (You used -> People used), duck-island-bombs (1894), bomber-command-roof (1944/1997); ending card foyles-mein-kampf. Card text uses text-wrap: pretty (balance gives up past six lines and left a lone word).
- 22 Nov 00:50, rings-centre: Grow yours. has Coming soon to London. and Try it early (mailto) back; last step is Want it in / your city? with the city field and Tell me under the heading (card dropped: a London fact under "your city" mixed messages, and the 9pm step already shows cards); footer only there. Card labels are just the place (Enfield, St James's Park, Green Park).
- 22 Nov 00:53: rings-centre merged and live on getforn.app.
- 22 Nov 01:00, open question (Tony: swipe left/Not for me feels arbitrary): alternative B, no choice, balls = the told finds, dust = every place passed that didn't make that night's five (the parked 19 Nov idea). Prototype on branch proto-dust only (site/proto/dust.html, never merge), comparing A and B over a week, month, 6 months and a year on a simulated London routine (45-zone commute, lunch patch, weekend clusters, top 5 told a night). Finding: B front-loads dust (the first week of a new route is a fog, 184 puffs against 35 balls) and then thins as routes run dry, so dust in B is a record of new ground. Undecided.
- 22 Nov 01:06, DECIDED (Tony): dust means history you passed but haven't heard yet. No keep/Not for me choice: balls are the finds told at 9pm, dust is every place passed that didn't make that night's five (the five-a-night limit, not a judgement; only reviewed facts ship, so every place is good). Dust isn't final: a dusty place can be told on a later, quieter day. Pick rule to add: best place first, then whichever was passed longest ago, so old dust gets its turn. Dust per place smaller (a pinch, not a full burst). Not built yet: prototype update, then the app (cards just page, no swipe verdict; stored answers no longer needed), RULES.md, and the landing page step Keep it, or let it go. needs new copy.
- 22 Nov 01:15, refined (Tony): dust IS what you pass; you uncover places from it (not "turns to dust"). Landing page live on getforn.app 22 Nov 01:18: 1 You pass history every day. (empty ring) / 2 Forn notices it for you. (pinches of dust appear round today's ring) / 3 At 9pm, see what you missed. (three pinches pull together into balls, cards) / 4 The rest / is dust, / for now. / 5 rings with dust pinches in the past / 6 Grow yours. Privacy card no longer mentions answers.
- 22 Nov 01:17, Tony on the look: it works because dust is tiny balls, so a place you pass is a cloud of small balls and an uncovered find is one big readable ball pulled out of the mess. Keep that relationship: same round shape, only scale and gathering change.
- App How it works copy, approved- App How it works copy, approved, ship WITH the app change (replaces Swipe and Keep): Dust: Every place you pass leaves dust on that day's ring: history you haven't uncovered yet. Lots of dust means you walked through lots of history. / Balls: Each night Forn uncovers up to five places, and they become black balls. Tap one to read it again. Pass the dusty places again to uncover more. One ring for each day, today in the middle. (Go about your day unchanged.)
- Still to do:- Still to do:- Still to do:- Still to do: (3) ImprovMX for hello@ and feedback@: Tony adds getforn.app in ImprovMX, then Claude adds the MX and SPF records through Vercel. (4) The agreed page changes (real fact cards, footer only on the last step, city sign-up).
- Content: batch 11 reviewed 22 Nov 09:02: 20/20 kept, all four nights good, so it ships: the 8 new facts plus the Kew rewrite are in spots.json (172 spots). Tony wants more modern facts (1970s, 80s, 90s) dotted among the old ones; next batches lean 1960 to 2000 (notes/review-log-3.md). Fact files and notes are in this repo: content/facts/ and notes/. The batch 11 review page in the Project can now be archived.

### Update, Sat 21 Nov 23:50: GitHub first (read this first)
- Tony now works GitHub first so he can work away from the Mac; the Mac is a fallback. This repo's HANDOVER.md is the master handover. The Stepback Google Doc is retired: no need to copy into it.
- "Needs the Mac" items no longer wait: landing page changes go through the ganda repo (forn branch) with a Vercel preview link for Tony to check on his phone. getforn.app setup needs the domain registrar and Vercel dashboards: do it in Tony's Chrome when it's on, otherwise give him the one or two settings to change.
- Network: Tony added historicengland.org.uk (and Hlid's sites) to the allowed sites; applies to new chats. The homepage blocks automated visits, so look for Historic England's open data download address and ask Tony to allow it too. Wikipedia works.

### Sat 21 Nov 2026, 19:05

This section mirrors claude/HANDOVER-2026-11-21.md in the claude.ai Forn Project (the review logs, fact files and review pages live there). Older history follows below it.

The master handover for the next Forn session. Pushed on 21 Nov evening from the cloud (Mac off): the icon change (b3ce54d) and Monday's items 1 to 3 (fc93a08, build green). The repo's HANDOVER.md now carries this file at the top. The Stepback handover Google Doc is NOT updated yet: the Drive tools can't edit doc text, so copy this file into it when the Mac is on.

### Update, Sat 21 Nov 19:05: Monday items 1 to 3 done early (commit fc93a08, Build APK green)
- spots.json: 163 spots (the 21 test spots plus 142 passed London and SW20 facts), every one with year and topic. Built from the latest reviewed text of each card (review pages for batches 1 to 10), points from the Project fact files. Left out: the dropped ids, kew-pagoda-dragons (waiting on batch 11), batch 11's new facts (waiting on review), and two SW20 facts never reviewed that break rule 3: putney-vale-bullet (a death) and nelson-merton (a mistress). The 21 test spots got years and topics by hand. The Project's fact files are unchanged; spots.json is now the shipped set.
- Nightly mix in Night.pick, as specced in notes/nightly-mix.md. Era comes from year inside the app (Spot.era).
- Zone fix (Fences.kt): when zones are set (every app open, boot, after 9pm) and again at 9pm, the app asks for a location fix (fresh, else last known; ignored if older than 15 min or worse than 200m) and counts any untold zone you're standing in as passed, at the fix time. The 9pm receiver waits for this (goAsync).
- New because London has more than 100 zones: the app watches the 99 nearest untold zones plus one exit ring centred where you are (half the distance to the furthest watched zone, 1 to 30km). Leaving the ring re-picks the nearest. Status line in Testing: "Watching N places, the nearest of M zones, re-picked after X km."
- RULES.md: zones, mix, year/topic fields and topic list, the 13 writing rules, the night review process.
- tools/pipeline/: gather, filter, check (bracket bug fixed: titles keep their brackets), dyk, raw, with a README. Caches and geo data are gitignored.
- To check on the phone: update through Obtainium, open the app, How it works > Testing should say Watching ... places. Tonight's 9pm (or tomorrow's) is the first real test of the mix and the inside count. Ask for a Send my data export after a day out.
- 19:15 fix (7ea32cd, build green): Tony's app said "Zones not working: Maximum package geofence allowance reached (code 10)". Cause: two zone set-ups overlapped (opening the app runs one, and with a fix arriving at different times they picked different nearest-100 sets), so Android saw more than 100. Fences.register now runs one set-up at a time and re-runs once if asked mid set-up. Check How it works > Testing says Watching ... places after updating.
- 19:20 to 19:37: How it works icon now 14 x 20 with a 1.5 stroke (lines inset 4, last line 2 shorter), matching the standard Material back arrow; same in Hlid (commits 986ed3e, 6e9e4dc). Back arrow stays Material. Chips stay 1px.
- Still to do from Monday's list: getforn.app setup and landing page changes (needs the Mac and Chrome), and copying this handover into the Stepback Google Doc (Drive tools can't edit doc text).

### Update, Sat 21 Nov 18:50
- Tony: swap the How it works icon for Hlid's notes-page icon (rect 5.5,2 13x20 rx3 plus three lines, 2px round stroke on a 24 grid), shown at 28px in ink. Done in claude/patches/notes-icon.patch (index.html notes icon; About credits Material Symbols for the back icon; RULES.md icon line). Decision (Tony, 18:47): back arrows stay the standard Material Symbols arrow_back in both apps, so the two apps match: same notes icon, same Material back arrow (Hlid already had both, nothing to change there). Pushed 21 Nov 18:48 (commit b3ce54d), Build APK green; the patch file is now history.

### Update, Sat 21 Nov 18:05
- Mac still off; nothing pushed. Monday list below, now with batch 11's merges added.
- Batch 11 built as four nights on its own page, "Forn Review, batch 11", https://claude.ai/artifact/E58zFFfKfg1sbrWPYd1gWR (slug 69dab327-7329-4a9d-9ca1-abdf2d8a32c6). Answers in collection review-batch-11 on that artifact: card ids hold keep/reject, night-1 to night-4 hold Good night / Flat night. Waiting for Tony.
- Line-ups, sources and what was dropped while writing: notes/review-log-3.md. New facts: content/facts/london-old-batch11.json (8 pre-1500 + the kew-pagoda-dragons rewrite), sources-london-old-batch11.json, fact-tags-batch11.json. Page source: claude/review/forn-review-batch11.html.
- After the answers: under 1 in 5 rejects and most nights good means the batch 10/11 shape ships; then the London coverage map.

### Update, Sat 21 Nov evening
- Mac was off, so nothing was pushed.
- Tony allowed british-history.ac.uk (BHO) as a source.
- Batch 9 reviewed: 15/20. Batch 10 (pre-1500 London, own page "Forn Review, batch 10", https://claude.ai/artifact/He8rUCU2stSdA9SN3AZCmx, answers in review-batch-10 on that artifact) reviewed: 19/20.
- Dropped: perry-statue, clattern-goal (both second rejects), st-helier-alphabet, becontree-no-roads, barking-abbey (removed from london-old-batch10.json).
- kew-pagoda-dragons rewritten (end line), text in review-log-2.md; now in batch 11.
- Decision (Tony, 21 Nov): he can't check every fact; facts differ per person and place. He stops reviewing every card. Reviews become nights: four nights of five finds along a realistic day, mixing eras (medieval next to 1960s/90s), about half new and half already passed. He keeps or rejects each card and rates each night good or flat. One of these per new area or roughly every 60 new facts; under 1 in 5 rejects, the unseen facts ship.
- Grader tested and NOT used as a gate: a separate blind agent agreed with Tony 27/40 and, after tuning, 24/36 (about 2 in 3; it's much stricter than him). Details: notes/grader-test-1.md. notes/GRADER.md stays as an optional editor pass (its notes catch weak endings or a missing "why"); it never drops a card on its own.
- This handover and the logs live in the Project, so content work can carry on while the Mac is asleep.

### Decisions
- Release: Forn first. A paid app in January (£2.99 suggested), London only, once there's enough content. Details, positioning, competitors, Play policy and the landing page plan: notes/positioning-2026-11-21.md.
- Domain getforn.app bought (Vercel, Ganda team). Setup Monday: holding page at the root, /beta full page, ImprovMX hello@ and feedback@, redirect gandalondon.com/forn.
- Look: keep the flat black balls. claude/patches/look-switch.patch is NOT to be pushed.
- Writing rules, confirmed by Tony 21 Nov 16:25 (put into RULES.md):
  1. The single most interesting, surprising fact about the place.
  2. Every claim in notification and card is in the source.
  3. Skip anything resting on a death, crime or sex; no restaurants or "described as" quotes.
  4. Drop anything that makes him ask "why does it matter?"
  5. The notification states the fact ("Did you know, ...").
  6. One fact per card: the card explains the notification's fact more fully; never a second fact.
  7. Name the kind of thing plainly (the band, a Camden pub, an oak tree, an English army).
  8. Don't name people who'd need explaining (Suggs).
  9. No jargon, odd phrasing ("by the sun"), old or foreign words (cyninges, cniht), or places locals wouldn't know (Ratcliff). Round numbers.
  10. Give the cause if the source has it.
  11. Aim for 35 words or under.
  12. Reviews in batches of 20; an area ships under 1 in 5 rejects. (21 Nov: now reviewed as nights, see above.)
  13. Every fact keeps its source text.
  14. (21 Nov, from batch 9) A fact that needs local or background knowledge to land is out. A card rejected twice is dropped, not rewritten again.
- Nightly mix (agreed, not built): highest score first, then minus 1.5 per already-picked find in the same era and per same topic; up to 5. Spec and test: notes/nightly-mix.md. Tags for all facts: content/facts/fact-tags.json (tag new facts as they're written; batch 10 and 11 tags are in fact-tags-batch10.json and fact-tags-batch11.json, merge at the push).

### Review state (answers in collections review-batch-N)
- "Forn Review" artifact, https://claude.ai/artifact/2ZHGiKjzVxXHSBZ72Hmuvp: batches up to 9.
- "Forn Review, batch 10", https://claude.ai/artifact/He8rUCU2stSdA9SN3AZCmx: batch 10.
- "Forn Review, batch 11", https://claude.ai/artifact/E58zFFfKfg1sbrWPYd1gWR: batch 11, the first night-format review. A page per batch from now on.
- SW20/Merton: passed (london-1: 20/20); one-fact rewrites passed in batch 9 except st-helier-alphabet and perry-statue (dropped).
- London DYK: batch 3 19/20, batch 4 13/20, batch 5 3/6, batch 6 17/20, batch 7 20/20, batch 9 spares mostly kept.
- London place names: batch 8 16/20; all 4 rewrites kept in batch 9.
- Older London: batch 10 19/20. Batch 11 waiting.
- Logs: notes/review-log.md (batches 5 to 8), notes/review-log-2.md (batches 8 to 10, with results), notes/review-log-3.md (batch 11 onwards), notes/session-2026-11-20.md (everything up to batch 4, data check, pipeline), notes/grader-test-1.md (grader tests).

### Where the facts are (Project, content/facts/)
- sw20-merton-draft.json (40) plus sw20-merton-onefact.json (9 replacement fact texts; merge at the push).
- london-dyk-draft.json (batch 3), london-dyk-batch4.json, london-dyk-batch6.json, london-names-batch8.json, london-old-batch10.json (19), london-old-batch11.json (8 new + kew rewrite). Use the current fact text; dropped ids: cavendish-time, great-turnstile-cattle, perry-statue, clattern-goal, st-helier-alphabet, becontree-no-roads, barking-abbey.
- Batch 9 tweaks that live only on the page and in review-log-2.md: boulogne-mouth (new line and card), minchenden-oak (line says "oak tree"). kew-pagoda-dragons' new card text is now in london-old-batch11.json; replace the old text in london-dyk-batch4.json at the push.
- Sources: sources-sw20-merton.json, sources-london.json, sources-london-batch4.json, sources-london-batch6.json, sources-london-names.json, sources-london-old-batch10.json, sources-london-old-batch11.json (BHO isn't reachable from the shell; WebFetch reaches it, so the text is quoted passages, not whole pages).
- Hooks still to mine: dyk-london-hooks.json (376). Portlethen: portlethen-draft.json (Tony's trips only).
- Pipeline scripts: tools/pipeline/ (gather, filter, check, dyk, raw). raw.py uses Wikipedia's action=raw route, which isn't rate-limited.

### Monday, Mac on
1. Done 21 Nov (fc93a08): facts into spots.json, rules, pipeline scripts, HANDOVER.md, zone fix, nightly mix. Still open: this handover into the Google Doc; merging fact-tags-batch10/11 into the Project's fact-tags.json is moot now spots.json holds year and topic (batch 11's tags go in with its facts once they pass).
2. getforn.app setup and the landing page changes (build locally, review in Chrome).
3. After batch 11's answers: add the passing batch 11 facts and the Kew rewrite to spots.json and push.

### Agreed, not built yet
- Landing page changes (real fact cards on "keeps the things you saw", footer line only at the bottom); getforn.app holding page and /beta; Play background location declaration (December); go/no-go replay test before January.
- Still open from 19 Nov: bigger ball tap area; stop zones re-registering on every open; landing page rings with today in the centre.
- Content next: batch 11 answers, then the London coverage map, then Surrey Hills and his drive routes.
- Optional edits flagged by the grader on passed cards: norway-tree (say it's a wartime thank-you, if the source has it), leaning-tower-rotherhithe (card never says why it leans), crooked-billet-phone (card repeats the line). Check sources before changing.
- check.py bug: strips brackets from source titles.


---

## Earlier history (to 19 Nov)


Name: the app is now Forn (Old Norse for ancient), chosen 18 Nov over Hring (said aloud it sounds like herring), Jord (the J), Askr and Munin. App name and in-app copy changed in build 12; the GitHub repo was renamed to Gandalondon/forn on 18 Nov (21:25); the package id, APK name and key alias stay stepback for good, so updates install over the top.

Master handover for Stepback. The content pipeline plan (sources, stages, review loop with Tony, order) is PIPELINE.md. The current rulebook (data, facts, picks, rings, look) is RULES.md: read it first. Mirrors the Google Doc "Stepback handover" in Drive > Claude. Rules: "App idea rules", in the same folder.

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
- 18 Nov, 19:05, landing page update (live on gandalondon.com/forn, still noindex): rings run full bleed under the words on phones and desktop (Tony 19:30: no white box, no fade, overlap is fine). No disc at the start: steps 0 and 1 show only today's empty ring, the three finds pop in on step 2, step 5 (Every day adds a ring.) stays near today's edge and the past rings appear one by one going back in time (19:20 change: Tony preferred this to growing from the centre); only step 6 zooms out, step 6 is now Grow yours. with Coming soon to Android. as a 19px note, then Try it early; it zooms out to the whole disc.
- 18 Nov 20:00, Scotland build: removed Try it out (example finds, span, kept, busy, empty days) and Tell me now from How it works, and the "Passed today" list in Testing, so 9pm stays a surprise. Testing now only shows fence status and Record walk. Native tellNow bridge still exists but nothing calls it. Empty-day "no ring" option judged not to work (Tony): rings for empty days stay full.
- 18 Nov 20:55, build after Scotland build: Show six months button in How it works > Testing (for showing Tony's dad). Example finds (182 days, half kept) drawn around the real ones, in memory only, never saved; the same button reads Back to my rings; closing the app also turns it off. Example balls can't be opened. Next session: start the pipeline pilot (PIPELINE.md) when Tony is back from Scotland.
- 18 Nov 21:00, landing page (after Scotland): rings shimmered when zoomed out (moire: dotted day rings closer than a pixel). Fix: level of detail, day rings fade under 8px apart, then Mondays; bands thinner than a device pixel hide and leave their hairline. The app got the same fix in the next build (21:20). Footer name and Privacy now Medium (500) in ink. Card swapped to the Necropolis Railway: For 87 years, a train from Waterloo took coffins to a Surrey cemetery, each with a first, second or third class ticket. (Waterloo station, 10:42). Tony wants whoa facts, not merely amusing ones: a useful bar for the pipeline.
- 18 Nov 23:55: all body text black (--ink-soft now #1A1A1A). Tony likes the balls bleeding off screen, so the bottom line (tally) stays plain ink so it bleeds into the black where a ball sits under it (Tony wants that, 19 Nov; a flip-to-grey blend was tried and dropped). Dust specks are round (canvas sprite) on app and site, and in the app every speck drifts slowly via a vertex shader (cheap on phones: one shared clock uniform).
- 19 Nov 00:10, regular rings (app and site): day rings, a week ring every Monday, every 4th week ring thicker, and the year ring every 52 weeks (13 blocks of 4 weeks), counted from Monday 29 Dec 2025 so the year ring lands at New Year. Replaces calendar months, which gave 4 or 5 weeks per month and a month ring mid-week (Tony saw uneven spacing). Tony suggested 12 x 4 weeks; Claude went with 13 so a year stays a year. Text at the bottom deliberately bleeds into the black balls (forces zoom out).
- 19 Nov 00:15: dust is solid light grey (#C8C8C8, no opacity) on app and site, so overlapping specks merge into one flat grey (Tony likes same colours merging). App: two-finger drag pans across the rings (OrbitControls pan on the ground plane), clamped to the disc, so old balls far out can be reached when zoomed in.
- 19 Nov 00:25: balls overlapped on a busy day (the fixed step along today's arc wrapped round past six finds; past days used random angles). Now every day's finds are evenly spaced round its ring, the gap shrinking to fit (step = min(0.6/R, 2pi/n)); past days start at a seeded angle per day.
- 19 Nov 00:30: in the six months example, tapping a ball opens a placeholder card (An example find. Yours will hold a fact about somewhere you passed that day.) with the place and date; Tell me more is hidden for examples.
- 19 Nov 16:15: rings run like a real tree: newest ring OUTSIDE, oldest in the centre (Claude wrongly said today was in the centre on 19 Nov; it isn't). Today's ring no longer shows until tonight's finds land (todayWait), and the title names that one day (e.g. Wednesday) while it waits. New Send my data button in How it works > Testing: writes forn-data-<time>.json to Downloads/Forn (state, all stored prefs, crash notes, last 800 lines of events.log; no GPX routes) and opens the share menu, so Tony can send it for Claude to investigate.
- 19 Nov 22:15: today now in the CENTRE, older days ripple outwards (reverses the newest-outside tree order; Tony agreed it opens on the same spot and keeps today's balls tight). Before 9pm today takes no ring, so yesterday is the middle. Ball angle = time you passed the place, clock face (midnight at the top), seeded nudge of about 3.5 degrees, balls on the same ring pushed apart to at least 0.42 centre to centre (or shared evenly if a ring is full); no time = seeded angle. Example finds get commute-like times so lanes show. Drawing only: stored data untouched. The landing page's rings still use the old order.
- 19 Nov 22:30, first data export reviewed (Drive file "Forn data"): (1) bug fixed: sw20-clay was told by the v1 app before told_day existed, so toldDay fell back to Day.key() and it floated onto today's ring every day (the "extra ring" Tony saw at 16:06). Now falls back to the earliest passed_ day. (2) Only 5 zones left: the test set is 16 spots and told spots are never watched again, so the app runs dry within days: the content pipeline is the real blocker. (3) Zones re-register every time the app opens, and each re-register re-fires "passed" for zones you're inside (harmless, first time kept, but noisy). (4) 9pm worked on 19 Nov: Heathrow camp, Stanwell Cursus, Dyce, Tyrebagger, Portlethen Moss, all kept.
- 19 Nov 23:00: overlaps fixed with Tony's real data (two afternoons at the same hours, Dyce and Tyrebagger at the same second). Balls a quarter smaller (R_BALL 0.12), rings wider (STEP 0.48), gap along a ring 0.34. Clusters fan out evenly either side of their middle time (keeps order; the clock is a guide, not a dial); a fan that would wrap round shares the ring evenly.
- 19 Nov 23:10: reopened cards swipe through the tapped day's kept finds in time order without closing (right = earlier, left = later; stops at the day's last card, tap another ring to change day); dots under the card show that day's kept finds; the rings glide to each ball behind the scrim. Tony's call after "tap 10 buttons to read today's 5" felt irritating. Dust has no card, so isn't in the run.
- 19 Nov 23:05: finds without a told_day (only sw20-clay, told by the v1 app) are hidden from the rings at Tony's request; still in "told" so never repeated. Nothing deleted from the phone.
- 19 Nov 23:20: five Portlethen spots added for Tony's local walks (Findon / Finnan haddie, Port Leviathan whales legend, the vanished Portlethen castle at Mains of Portlethen, the 1639 Covenanter army on the Causey Mounth, Downies near-derelict then petitioning the planners). Sources in spots.json. Castle and Causey points are approximate (700-800m zones); Findon, Old Portlethen and Downies from Wikipedia coordinates.

## Open at end of 19 Nov session (build 46)
- NEXT: content pilot from PIPELINE.md (SW20 and London first, then Tony's 20-fact review loop). Only ~6 untold spots left near Portlethen plus a few in Surrey/London, so the app runs dry within days without it. Bar: "whoa" facts, not merely amusing.
- Tony is around Portlethen on 20 Nov: after that, ask for a Send my data export (it lands in his Drive as "Forn data") and check whether the approximate castle and Causey Mounth zones fired in sensible places.
- Not built yet: bigger tap area on balls (nearest ball within a fingertip, for the zoomed-out view); stop zones re-registering on every app open (noisy repeat "passed" log lines, harmless).
- Landing page (gandalondon.com/forn, ganda repo public/forn) still draws today on the outside; match the app (today in the centre, clock-face angles, solid grey dust is done) next time it's touched.
- Decided and kept: Not for me stays (quality signal for the pipeline plus the dust); alternative parked: dust from places passed but not told.
