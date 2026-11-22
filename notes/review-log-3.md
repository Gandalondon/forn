# Forn review log, part 3 (continues notes/review-log-2.md)

## Batch 11 (built 21 Nov 18:00): four nights, reviewed 22 Nov 09:02
- New format (Tony, 21 Nov): four nights of five finds along a realistic day, cards in nightly-mix pick order, keep/reject per card plus Good night / Flat night per night. Cards don't show which are new or already passed (avoids bias).
- Page: "Forn Review, batch 11", slug 69dab327-7329-4a9d-9ca1-abdf2d8a32c6, https://claude.ai/artifact/E58zFFfKfg1sbrWPYd1gWR. Answers in collection review-batch-11 on THAT artifact: card ids hold verdicts, night-1 to night-4 hold the ratings. Source copy: claude/review/forn-review-batch11.html.
- Nights:
  1. Tue 24 Nov, home day (dog walk on the Common, Kingston errand, Tooting): kingston-crowned (new), john-innes-compost, caesars-camp, torch-motspur, tooting-bec (new).
  2. Wed 25 Nov, train into town: chapter-house-commons (new), holborn-power, franklin-chess, sky-pool, aldgate-chaucer (new).
  3. Sat 28 Nov, Greenwich: blackheath-emperor (new), first-tube-baby, greenwich-oak-prison, peter-the-great, greenwich-castle-observatory (new).
  4. Sun 29 Nov, Kew and Syon, home over Putney Bridge and the A3: syon-nuns (new), battle-of-brentford, tutankhamun-putney, kew-pagoda-dragons (rewrite), fulham-palace (new).
- 8 new pre-1500 + kew rewrite + 11 passed. New facts: content/facts/london-old-batch11.json; sources: sources-london-old-batch11.json; tags: fact-tags-batch11.json (merge at the push).
- 7 of 8 new from BHO (VCH Surrey 2, 3, 4; VCH Middlesex 1; Old and New London 2, 3, 6; Lysons 2; Memorials of London Life), some topped up with Wikipedia, English Heritage or Historic England for a present-day detail (where the stone stands now, 1973, 1386). blackheath-emperor is Wikipedia only: BHO's Eltham page doesn't mention the visit.
- Dropped while writing: merton-becket (Merton Priory already has merton-statute and the Sainsbury's hook), St Andrew Undershaft maypole (Tudor, and too close to newton-maypole), Knut's trench at Rotherhithe (BHO only says "said to have", writers dissent), Lewisham given to Ghent's abbey in 918 (same shape as tooting-bec), Hampton Court's Hospitallers (the strong bit, Wolsey's lease, is Tudor).
- Things to watch in the answers: aldgate-chaucer is a second Chaucer card (tabard-mp passed in batch 10); Sunday has two Saxon finds (battle-of-brentford, fulham-palace), which is what a real Kew day would give; chapter-house-commons start year differs by source (1352 or 1377), so the card says "for 170 years, until 1547".
- Every card is 35 words or under. Checked at 375px: intro, card, reject reasons, night rating, done screen; no script errors.

### Batch 11 results (Tony, 22 Nov 08:59 to 09:02)
- 20 of 20 kept, 0 rejects. All four nights rated Good night. Under 1 in 5 rejects, so the shape ships.
- The 8 new pre-1500 facts and the kew-pagoda-dragons rewrite went into spots.json (172 spots). Kew's kind is building.
- Tony: it read well and was interesting, but over four nights in a row a lot of it was old (1700s, 1800s, medieval). He wants more modern facts dotted through: 1970s, 80s, 90s.
- Partly the batch's own doing: all 8 new facts were pre-1500 on purpose (the older-London push), so the nights leaned old. Of the 172 spots, the late-20c and 21c share is what to grow next.
- Direction for the next batches: write more 1960 to 2000 facts (music, TV and film, design, buildings, transport, everyday life) so the nightly mix has modern finds to spread in. Mix rule unchanged for now.

## Batch 12 (built 22 Nov 09:20): modern London, four nights, reviewed 22 Nov 09:22
- Page: "Forn Review, batch 12", slug 228ded2a-b4d1-4ddc-a9ef-9dc45c3981d8, https://claude.ai/artifact/5GUwCdnc9tErfTjHpZTKJ7. Answers in collection review-batch-12 on that artifact. Built from tools/review/template.html with tools/review/build.py; nights data in content/review/batch12-nights.json. New reject reason: Too grim (tests the revised rule 3).
- First batch under the revised rule 3 (history, not horror: crime, gangs, executions in) and rule 14 (film, TV, music once they've become history). Asked for by Tony after batch 11 felt old.
- 13 new: beatles-rooftop, hendrix-handel, werewolf-piccadilly, bond-war-office, execution-dock, city-bonds, baker-street-robbery, abbey-road-crossing, stones-sutton, floyd-pig, krays-esmeralda, marley-collingham, batman-acton. Facts: content/facts/london-modern-batch12.json; source sentences: sources-london-modern-batch12.json. All from Wikipedia (raw article text); bond-war-office also bondlocations.com and jamesbondlifestyle.com (from a web search).
- 7 passed mixed in: whitehall-bath-screen, fann-street-sans, whittington-longhouse, leaning-tower-rotherhithe, first-heart-transplant, lords-pavilion-women, primrose-hill-tunnel.
- Nights: Mon West End (4 new), Wed City to Wapping (2 new), Fri Marylebone and St John's Wood (2 new), Sun driving Sutton to Acton (5 new, all 1960 to 1990 on purpose, to see if an all-modern night still feels like Forn).
- New topic: crime (added to RULES.md). Every card 35 words or under; every number and name checked against the source sentences (292 is 291.9 rounded).
- Found but held back: Heddon Street (Bowie's Ziggy Stardust cover, 1972) and Brink's-Mat (Heathrow, 1983): sources had no usable coordinates. Tramp nightclub (Keith Moon) dropped: the article doesn't support the chandelier story.
- After the answers: passing facts go into spots.json.

### Batch 12 results (Tony, 22 Nov 09:20 to 09:22)
- 19 of 20 kept (5% rejects), all four nights Good, including the all-modern Sunday. Nothing marked Too grim: Execution Dock, the Krays and the robberies all passed, so the revised rule 3 holds.
- Rejected: beatles-rooftop, Confusing: "The Beatles definitely played in public again, so maybe the wording is a bit confusing here." The source says it was the final public performance of their career, but "They never played in public again" reads as if none of them ever did (solo careers). Rewritten to say it was the band's last public performance; line now says "as a band". Goes into the next batch for a second look.
- The 12 other new facts are in spots.json (184 spots).
- Direction holds: modern, crime, film and music land as well as the old history. Next: more of the same mix, plus the held-back Heddon Street and Brink's-Mat once there are reliable locations.

## Batch 13 (built 22 Nov 10:38): more modern London, four nights, NOT yet reviewed
- Page: "Forn Review, batch 13", slug 10582ebe-b835-458c-96bf-65baba8afa25, https://claude.ai/artifact/324WRsSff9kqxHBghdYAY4. Answers in review-batch-13 on that artifact. Nights data: content/review/batch13-nights.json.
- 11 new (content/facts/london-modern-batch13.json, sources in sources-london-modern-batch13.json, all Wikipedia raw text): trident-hey-jude, hendrix-ronnie-scotts, carnaby-time, markov-umbrella, blind-beggar, spaghetti-house-siege, biba-kensington, withnail-west-house, punk-100-club, live-aid-wembley, clockwork-thamesmead.
- 1 rewrite: beatles-rooftop ("the band's last public performance"; text in london-modern-batch12.json).
- 8 passed: soho-charles-fountain, mithras-returned, syds-coffee-stall, widows-son-buns, python-basil-street, belgravia-fatberg, bowie-blackheath, sun-in-the-sands.
- Tests the edge of rule 3 on purpose: blind-beggar (a famous gangland murder) and markov-umbrella (a Cold War assassination). Too grim is a reject reason.
- Every card 35 words or under; names and numbers checked against the source sentences.
- Held back, no coordinates in the sources: Marquee Club (Stones' first gig 1962), Hatton Garden burglary (2015), Knightsbridge Security Deposit robbery (1987), Notting Hill (1999 film), Heddon Street, Brink's-Mat. The Blind Beggar also has William Booth's first sermon (Salvation Army, 1865); one fact per spot, so it's a spare.

## Batch 14 (built 22 Nov 13:27): outer London, four nights, NOT yet reviewed
- Page: "Forn Review, batch 14", slug 0b232203-51a8-4a7b-8ed1-a052f8048a24, https://claude.ai/artifact/2NmRPAc1s2xnnN3gsZ9s4o. Answers in review-batch-14 on that artifact. Nights data: content/review/batch14-nights.json. Built while batch 13 waits; review either first.
- Aimed at outer London, where the app is thinnest (go/no-go replay, notes/replay-test.md). 13 new (content/facts/london-outer-batch14.json, source sentences in sources-london-outer-batch14.json, all Wikipedia raw text, coordinates from the articles): croydon-mayday, crystal-palace-dinner, chislehurst-bowie, down-house-origin, lesnes-becket, red-house-wallpaper, upminster-sound, walthamstow-first-flight, enfield-bren-sten, nonsuch-debts, eel-pie-stones, hounslow-baseline, uxbridge-so-few.
- 7 passed: eltham-barn, gants-hill-moscow, ilford-dickin, first-atm, minchenden-oak, grendels-gate, ruislip-tower.
- Nights: Sat south-east by car (Croydon, Crystal Palace, Chislehurst, Downe, Eltham; 4 new); Sun east (Abbey Wood, Bexleyheath, Upminster, Gants Hill, Ilford; 3 new); Wed north (Walthamstow, Enfield Lock, Enfield, Southgate, Barnet; 2 new); Sat west (Ruislip, Uxbridge, Hounslow Heath, Twickenham, Cheam; 4 new).
- Every card 35 words or under; every name and number in the source sentences.
- Watch: upminster-sound's point is approximate (the church article has no coordinates; placed on St Laurence's, Corbets Tey Road, 400m zone). hounslow-baseline has three zones along the 1784 line (Hampton end, middle, King's Arbour end). enfield-bren-sten names Brno (rule 9?). lesnes-becket says "may have been", as the source does. Spares: Chislehurst's wartime shelter (15,000 people, a penny each), Croydon's first air traffic control tower (1920), Ealing Studios (oldest working film studio; no coordinates found).

## Batch 15 (built 22 Nov 13:38): the six held-back stories plus four, four nights, NOT yet reviewed
- Page: "Forn Review, batch 15", slug 901e5102-0198-4b86-a112-a28ba4869c8b, https://claude.ai/artifact/JoBwsopm2wkrKWNYMMyP8W. Answers in review-batch-15. Nights data: content/review/batch15-nights.json.
- 10 new (content/facts/london-batch15.json; sources-london-batch15.json holds the source sentences AND where each point came from): marquee-stones-first, heddon-ziggy, hatton-garden-lift, poe-stoke-newington, knightsbridge-deposit, notting-hill-door, electric-avenue, marlowe-deptford, brinks-mat-gold, ealing-studios.
- Held-back locations found: Marquee at 165 Oxford Street (Londonist, Wetherspoon history; Wikipedia's coordinates are the later Wardour Street club); Heddon Street from the Historic England entry for Heddon House; Hatton Garden from Wikidata; Cheval Place approximate from neighbouring listed buildings; Brink's-Mat from the trading estate's postcode TW4 6HB (Unit 7 is listed under it); Notting Hill approximate, a 300m zone covering 280 Westbourne Park Road and 142 Portobello Road.
- 10 passed: hendrix-handel, python-basil-street, krays-esmeralda, marley-collingham, name-brixton, peter-the-great, greenwich-oak-prison, heathrow-camp, battle-of-brentford, name-ealing.
- Nights: Tue West End, Holborn, Stoke Newington (4 new); Thu Knightsbridge to Notting Hill (2 new); Sat Brixton, Deptford, Greenwich (2 new); Mon Heathrow pick-up home via Brentford and Ealing (2 new).
- Watch: Hatton Garden is 2015, the most recent crime yet (no one hurt). Marlowe is a famous person's death (rule 3 allows). The Notting Hill card says "Hugh Grant's house" (the source says Will's house, played by Grant).
- New: tools/pipeline/lint.py (rule lint). Flags on batches 13 to 15: lesnes-becket's hedge (the source hedges too); hendrix-ronnie-scotts and spaghetti-house-siege share a topic within 300m of shipped spots (Soho is dense; fine).
