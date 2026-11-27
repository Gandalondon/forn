# New fact sources (27 Nov 2026)

Forn is paid, so every source needs commercial use allowed. Facts are always rewritten in our words and checked against a published source (RULES.md rules 2 and 13).

| Source | What it adds | Licence | Reachable from the cloud |
|---|---|---|---|
| Historic England list (NHLE), Open Data Hub / ArcGIS API | Every listed building and scheduled monument, exact points, list-entry text and dates. The biggest pool for buildings and ancient sites | OGL v3, commercial OK with attribution | No: allow services-eu1.arcgis.com and historicengland.org.uk downloads |
| Wikidata (SPARQL) | About 24,000 heritage-listed places with coordinates in Greater London's box; 775 films with 262 London filming places; dated events (mostly sport, low value) | CC0 | Yes |
| Open Plaques | Plaques with inscriptions and points, including music, film and TV people (the source behind English Heritage plaque maps) | Public domain (PDDL) | No: allow openplaques.org |
| OpenStreetMap via Overpass | historic=* points: memorials, plaques with inscriptions, boundary stones, sites | ODbL, attribution | No: allow overpass-api.de |
| London Remembers | 7,000+ London memorials and plaques with notes (e.g. Hendrix and McCartney on Kingly Street) | Unclear: leads only, verify elsewhere | No: allow londonremembers.com |
| Old Bailey Online | Trials 1674 to 1913 | Non-commercial only: leads at most, never the source | n/a |

Use order per area run: NHLE and Wikidata for points and dates, Wikipedia for the story (as now), Open Plaques and OSM for music, film and people, London Remembers only to find leads.

## Shell test and first pull (27 Nov 2026, 00:52 to 01:05, scheduled data dig)
| Source | From the shell, 27 Nov | Pulled for Greater London |
|---|---|---|
| NHLE via services-eu1.arcgis.com (National_Heritage_List_for_England_NHLE_v02_VIEW, layers 0 listed points, 6 scheduled monuments) | Works. Paged at 2,000; listed points are multipoint (no centroid), scheduled monuments are polygons (returnCentroid) | 19,176 listed buildings (24,453 in the box, 196 skipped as shipped), 161 scheduled monuments (12 skipped) |
| Wikidata SPARQL | Works | 2,561 heritage places with an English Wikipedia article, 218 filming locations, 762 music, film and crime places (studios, venues, clubs, cinemas, theatres, prisons, courts) |
| openplaques.org | Not usable: the site answers, but every bulk and area endpoint (plaques.json, places/gb/areas/london, data.json, geojson box) returns 503 or 500, and by 00:59 even single plaques (plaques/1.json) returned 503. Their server, not our allowlist. Try again another night | Nothing. Wikidata items with an Open Plaques id in London: only 12, dropped |
| overpass-api.de | Not usable: connection reset on every request (GET and POST), three tries | Nothing |
| londonremembers.com | Blocked: the bare domain redirects to www.londonremembers.com, which the proxy refuses (403). Allow www.londonremembers.com too | Nothing |

Files: content/candidates/ (README has licences and credits), scripts tools/candidates/. Ranking for area order: content/candidates/ranked.json.
