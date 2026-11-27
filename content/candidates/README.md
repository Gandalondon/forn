# Candidate places (raw material for area runs, 27 Nov 2026)

Not facts. Nothing here ships. Each row is a place an area run can look into, write up from a published source in our own words (RULES.md 2, 13, 16) and check as usual. Rows already in spots.json (same place within 100m and same story) are left out.

Made by tools/candidates/ (nhle.py, wikidata.py, wikidata_types.py, then rank.py). Re-run all four in that order from the repo root; about two minutes in total.

| File | Rows | What | Licence and credit |
|---|---|---|---|
| nhle-listed.json | 19,176 | Historic England listed buildings: list entry number (id), name, grade, point, borough, year first listed (not the building's date) | OGL v3.0. Credit: Contains public sector information licensed under the Open Government Licence v3.0. Entry page: historicengland.org.uk/listing/the-list/list-entry/{id} |
| nhle-scheduled.json | 161 | Scheduled monuments (polygon centres), same fields, year scheduled | As above |
| wikidata-heritage.json | 2,561 | Heritage-listed places with an English Wikipedia article: designations, NHLE number, inception year where known | Wikidata CC0. Wikipedia text is CC BY-SA: never copy wording |
| wikidata-filming.json | 218 | Filming locations with their films and TV and release years; old_works counts those from 2001 or earlier (rule 14) | Wikidata CC0 |
| wikidata-music-crime.json | 762 | Recording studios, music venues, nightclubs, cinemas, theatres, concert halls, prisons, courts, execution sites (opened and closed years) | Wikidata CC0 |
| leads.json | 536 + 120 | Best rule 14 (music, film, TV) and rule 3 (crime, prisons, courts, executions) leads, by type or name match. Leads only: check each | As their source |
| ranked.json | top 40 per borough | All candidates scored per borough, plus the boroughs ordered by how much they'd add to the replay go bar | As their source |

## ranked.json
- route: how often the replay's three people (tools/replay) pass the place within 250m. Weighted to the commuter and the outer Londoner (the go bar), doubled on days out, and divided by how many shipped spots that outing already passes, so gaps count most.
- rank: (base + 1.5 per flag) x (1 + 4 x route), x1.3 if over 500m from any shipped spot. Base: grade I 3, II* 2, II 0.4, scheduled 2.5, Wikipedia-backed heritage 2 to 3, filming 1 plus old works (max 3), music and crime types 2.
- Rows with route 0 are still good facts; they just don't move the go bar for the three test people.

## Caveats
- Some filming locations are whole districts (Battersea, Wandsworth): the point is the district centre, not a street. Find the actual street before writing.
- Rule 14 name matches include anything called Studio, Club or Empire: many are false leads.
- A listed date is when it was listed, not built. Get dates from the list entry text or Wikipedia.
- Not included: Open Plaques and OpenStreetMap (both unreachable on 27 Nov, see notes/sources.md), London Remembers (blocked; leads only anyway).
