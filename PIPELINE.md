# Forn content pipeline

Plan agreed 18 Nov 2026. Goal: facts for anyone, anywhere in Great Britain, built by Claude on Tony's Max plan (sessions and background tasks, no separate AI bill), checked by Tony through small random samples.

## The test that decides everything

Do most facts make you go "well I never", and are they true? Everything below exists to answer that cheaply before going wide.

## Sources (all open, all credited)

- Place-name origins: county place-name surveys, Wikipedia etymology sections, Key to English Place-Names (Nottingham). The richest seam, works in the countryside.
- Wikipedia: geotagged articles. Anecdotes and local history. Text is rewritten, never copied; source linked.
- Historic England NHLE and Historic Environment Scotland (Canmore): open government licence. Used for location and dates, rarely for the story.
- Local history societies, council heritage pages, Hidden London: the best stories; used where they exist.
- BGS geology: one or two deep-time facts per area (the SW20 sea).

Nothing from memory. Every fact keeps the source it was checked against.

## Stages

1. Gather: pull every candidate with a location in the area (place names, geotagged articles, listed sites, roads, rivers).
2. Filter with free rules: drop the dull majority (listed houses with no story, duplicates, anything with no date or angle). Expect most candidates to go.
3. Write: one surprising line per spot, by the rules in RULES.md (the fact first, plain words, one idea, the twist named).
4. Check: a second, separate pass reads the source again and confirms every claim in the line. Anything not confirmed is dropped, not softened.
5. Score: 1 to 10 for surprise, as now. Fence radius by kind (250m station, up to 3.5km for a landscape seen from a car).
6. Ship: region packs (spots-london.json and so on). The app keeps the nearest 100 as fences (Android's limit) and swaps them as you move.

## The review loop (Tony)

- Batches of 20, picked at random from a finished area. A simple review page: read the card, keep or reject. An HTML page, one card at a time (as in the app, with place and source under it). Keep is one tap. Reject is multi-select (decided 18 Nov): any of Dull, Wrong, Confusing, Too long, Knew it, plus an optional note (most useful on Wrong), then Next. Twenty cards, then a done screen; answers come back to Claude.
- Takes about five minutes. Tony never sees the whole set.
- After each batch Claude looks for the pattern behind the rejects: by source, kind, score, length, how it was written (e.g. "rejects are all listed buildings scored 6" or "anything over 30 words"). Then changes the filter or the writing rules, and rewrites the affected spots across the area, not just the 20.
- Aim: under 1 reject in 5 before an area ships. Track the reject rate per batch so the trend is visible.

## Order

1. Now: Tony tests the 16 hand-written spots (Raynes Park, Aberdeen area) over a few days off. Nothing needed from him.
2. Pilot: SW20 plus Merton, and one rural area (Portlethen or the Surrey Hills), a few hundred spots. Build the review page. First batch of 20 for Tony.
3. If the pilot lands: Greater London, borough by borough, then the south-east, then outwards. A region ships in the app as soon as it passes review.
4. Scotland via Canmore and Scottish place-names alongside, since Tony goes up there.

## Open questions

- How dense is enough? Raynes Park ran out in a day. Target to test: a new fact for most short trips in London.
- Repeats on the daily commute: each fact is told once, ever, so a regular route empties. Fine for London; watch it in the countryside.
- Licence wording in About once Wikipedia text is the source of rewritten facts (credit, link).
