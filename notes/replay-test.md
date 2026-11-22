# Go/no-go replay test (built 22 Nov 2026)

Turns "is it ready?" into a number. Scripts: tools/replay/ (routes.py, replay.py, howmany.py). Runs in about a second (howmany about a minute).

## How it works
- Three made-up but realistic people, eight weeks each, 50 random runs: Tony (SW20, dog walks, errands, one train into town a week, a country walk and a London day out at weekends); a commuter (Clapham to Moorgate on the Northern line, lunch walks, weekends in Brixton, Camden, the South Bank); an outer Londoner (Bromley, drives locally, Croydon, Chislehurst, Eltham, Victoria now and then).
- Routes are straight lines between waypoints, sampled every 40m. A zone fires when within its radius, as in the app. Tube legs count as underground: zones don't fire there.
- Each night: up to five by the nightly mix; told places drop out; unpicked ones stay dust.
- Weeks 1 and 2 are the honeymoon (the home patch is new). The number that matters is weeks 3 to 8: how many days get a find, and how many days out beyond the routine get one.
- Real tracks: there are none for London yet (the two Forn data exports are Aberdeen, and hold zone hits, not routes). A week of Record walk GPX from Tony would replace the Tony persona with the real thing.

## Results, 22 Nov (184 spots shipped; 208 with batches 13 and 14)
| Weeks 3 to 8 | Days with a find | Days out with a find | Finds a week |
|---|---|---|---|
| Tony | 23% | 29% | 6.8 |
| Commuter | 6% | 14% | 1.3 |
| Outer (Bromley) | 5% | 22% | 1.7 |
With batches 13 and 14: Tony 23/29%/7.0, commuter 9/18%/1.7, Bromley 6/26%/1.8.

## How many facts? (howmany.py: real spots plus N made up, half clustered on the centre, half spread across Greater London)
| Extra facts | Tony | Commuter | Bromley |
|---|---|---|---|
| 0 | 23% days, 29% days out, 6.7/wk | 6%, 15%, 1.3 | 5%, 22%, 1.7 |
| 1,000 | 32%, 40%, 9.7 | 24%, 79%, 6.2 | 10%, 43%, 3.2 |
| 2,000 | 36%, 45%, 11.0 | 32%, 91%, 10.1 | 12%, 50%, 3.7 |
| 3,000 | 40%, 50%, 12.6 | 40%, 96%, 12.6 | 14%, 58%, 4.2 |

## What it says
- Daily routines run dry whatever we add (by design): no fact count gets a commuter's office days above about 40%. Days out are the measure that moves.
- The centre gets there around 1,000 to 2,000 more facts: about 8 in 10 of a commuter's days out get a find, 6 to 10 finds a week.
- Outer London lags at every size, because history and the made-up spread both cluster in the centre. It needs its own coverage push, not just more facts.
- Tony's own numbers cap at about half his days out, because his country walks are in Surrey, outside London. Surrey Hills content matters for him, not for London buyers.

## Proposed go bar (for Tony to agree)
In weeks 3 to 8: at least 75% of a central commuter's days out and 50% of an outer Londoner's get a find, with 5+ finds a week for both. Today: 18% and 26%. Re-run after every batch: python3 tools/replay/replay.py app/src/main/assets/spots.json
