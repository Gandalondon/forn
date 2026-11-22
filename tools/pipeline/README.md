# Content pipeline scripts

Copied from the Forn Project (tools/pipeline/) on 21 Nov. The plan behind them is PIPELINE.md at the repo root; the writing rules are in RULES.md.

- gather.py: every geotagged Wikipedia article in a square, with text and Wikidata type.
- filter.py: drops the dull majority with free rules.
- check.py: flags numbers and names in a written fact that its source text doesn't contain.
- dyk.py: Wikipedia "Did you know" hooks inside Greater London (needs geo/london_boroughs.geojson).
- raw.py: whole articles as plain text via action=raw.

Caches and data stay out of git (cache/, geo/, raw.json, titles.txt).
