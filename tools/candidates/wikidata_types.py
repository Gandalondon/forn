"""Wikidata: music, film and crime place types in Greater London (recording studios, music venues, nightclubs,
cinemas, theatres, prisons, courts, execution sites), with English Wikipedia article. CC0. Leads for rules 14 and 3."""
from wdq import q, BOX, ll
from common import *
TYPES = {"Q746369": "recording studio", "Q8719053": "music venue", "Q622425": "nightclub", "Q41253": "cinema",
         "Q24354": "theatre", "Q40357": "prison", "Q1137809": "courthouse", "Q16917": "hospital", "Q3356179": "execution site",
         "Q1076486": "sports venue", "Q1060829": "concert hall", "Q57660343": "performing arts building"}
V = " ".join("wd:" + k for k in TYPES)
Q = """SELECT ?item ?itemLabel ?c ?t ?inc ?dis ?art WHERE { VALUES ?t { %s } ?item wdt:P31 ?t. %s
  ?art schema:about ?item; schema:isPartOf <https://en.wikipedia.org/>.
  OPTIONAL { ?item wdt:P571 ?i. BIND(YEAR(?i) AS ?inc) } OPTIONAL { ?item wdt:P576 ?x. BIND(YEAR(?x) AS ?dis) }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". } }""" % (V, BOX)
by = {}
for b in q(Q):
    lat, lon = ll(b["c"]["value"]); bo = borough(lat, lon)
    if not bo: continue
    k = b["item"]["value"].rsplit("/", 1)[1]
    r = by.setdefault(k, {"qid": k, "name": b.get("itemLabel", {}).get("value"), "lat": lat, "lon": lon, "borough": bo, "wiki": b["art"]["value"], "types": []})
    t = TYPES[b["t"]["value"].rsplit("/", 1)[1]]
    if t not in r["types"]: r["types"].append(t)
    if "inc" in b: r["year"] = int(b["inc"]["value"])
    if "dis" in b: r["closed"] = int(b["dis"]["value"])
rows = [r for r in by.values() if not shipped_near(r["lat"], r["lon"], r["name"])]
save("wikidata-music-crime.json", rows, {"source": "Wikidata place types (studios, venues, clubs, cinemas, theatres, prisons, courts, execution sites)", "licence": "CC0", "note": "year = opened, closed = dissolved (P576)"})
