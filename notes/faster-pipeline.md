# Faster pipeline: reaching 2,500 to 3,000 London facts (plan, 22 Nov 2026, not agreed yet)

## The problem
- Now: 184 shipped, about 12 new facts per review page, one page per Tony review. 2,500 that way is about 190 pages. Not happening by January.
- Writing isn't the bottleneck: one session wrote 23 checked facts (batches 14 and 15) in under an hour. Tony's review time is.

## The idea: write by area, review a sample
1. Area runs. Claude writes a whole area at once: 80 to 120 facts per run (a borough, or a cluster of two or three outer ones), in a scheduled session overnight. Same rules, same source text kept.
2. Automatic gate before Tony sees anything (all free, all scripted, tools/pipeline):
   - check.py: every number and name in line and card is in the source sentences.
   - lint (to build): 35 words or under, line starts "Did you know, ", no "you", no "described as", no hedges the source doesn't have, banned words list (rule 9), no second "the world's first" on one page.
   - points: inside Greater London, not on top of an existing spot with the same topic (300m), coordinates from Wikipedia or Wikidata (bulk SPARQL works from the workspace), approximate ones flagged.
   - duplicates: same story already shipped (title and key-name match).
   - blind grader (notes/GRADER.md) as an editor pass only: rewrites weak endings, never drops.
3. Sampled review. Per area, one page as now (four nights of five), but with 12 random new cards from the area plus 8 passed. Rule: 0 or 1 reject of the 12 new and the whole area ships. 2 or more and Claude finds the pattern, fixes it across the area, and samples again (new cards).
   - Why 12 and 1: an area that's truly 1 in 20 bad passes 9 times in 10; 1 in 5 bad passes only about 1 time in 4; 3 in 10 bad passes 1 time in 10. Close to today's "under 1 in 5" bar, at a tenth of the review effort per fact.
4. Ship straight after a pass: the area's facts go into spots.json, push, APK.

## Volumes
- About 25 area runs of 100 gets to 2,500. Two runs a night is under two weeks of nights.
- Tony: about 25 pages of 20 cards (about 5 minutes each), plus re-samples. Roughly two hours in total.

## Order of areas: let the replay test choose
- After each run, re-run tools/replay/replay.py. Next area is whichever adds most to the go bar (notes/replay-test.md): central first (biggest jump for commuters), then outer boroughs ring by ring, then Tony's Surrey.
- Coverage map (to build): spots per square km over Greater London, so gaps are visible.

## Sources per run (in order)
- Wikipedia geotagged articles in the area (gather.py, filter.py), raw text via raw.py.
- DYK hooks (content/facts/dyk-london-hooks.json, 376 still to mine).
- Historic England list entries for locations and dates (open data download still to be allowed).
- British History Online for anything pre-1700 (WebFetch only).

## Decisions for Tony
1. Agree sampled review (12 new cards, ship at 0 or 1 rejects)?
2. Agree scheduled overnight area runs (nothing ships without a passed sample)?
3. Agree the go bar in notes/replay-test.md?
