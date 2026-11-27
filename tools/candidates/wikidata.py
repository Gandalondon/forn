"""Wikidata: filming locations and heritage-listed places in Greater London, with English Wikipedia article. CC0."""
from wdq import *
# 1. Filming locations: works (film/TV) with a filming location that has coordinates in the box
FILM = """SELECT ?item ?itemLabel ?c ?work ?workLabel ?year ?typeLabel ?art WHERE {
  ?work wdt:P915 ?item. %s
  OPTIONAL { ?work wdt:P577 ?d. BIND(YEAR(?d) AS ?year) }
  OPTIONAL { ?work wdt:P31 ?type. }
  OPTIONAL { ?art schema:about ?item; schema:isPartOf <https://en.wikipedia.org/>. }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". } }""" % BOX
by = {}
for b in q(FILM):
    lat, lon = ll(b["c"]["value"]); bo = borough(lat, lon)
    if not bo: continue
    k = b["item"]["value"].rsplit("/", 1)[1]
    r = by.setdefault(k, {"qid": k, "name": b.get("itemLabel", {}).get("value"), "lat": lat, "lon": lon, "borough": bo, "wiki": b.get("art", {}).get("value"), "works": {}})
    w = b["workLabel"]["value"]; y = int(b["year"]["value"]) if "year" in b else None
    old = r["works"].get(w); r["works"][w] = {"year": min(y, old["year"]) if (old and old["year"] and y) else (y or (old or {}).get("year")), "type": b.get("typeLabel", {}).get("value") or (old or {}).get("type")}
rows = []
for r in by.values():
    r["works"] = [{"title": t, **v} for t, v in sorted(r["works"].items(), key=lambda x: x[1]["year"] or 9999)]
    r["old_works"] = sum(1 for w in r["works"] if w["year"] and w["year"] <= 2001)
    if shipped_near(r["lat"], r["lon"], r["name"]): continue
    rows.append(r)
rows.sort(key=lambda r: -r["old_works"])
save("wikidata-filming.json", rows, {"source": "Wikidata (P915 filming location)", "licence": "CC0", "attribution": "Wikidata, CC0 (no attribution required)", "note": "old_works = works released 2001 or earlier (rule 14: 25+ years)"})
# 2. Heritage-listed places (P1435) with English Wikipedia article
HER = """SELECT ?item ?itemLabel ?c ?desigLabel ?inc ?art ?nhle WHERE {
  ?item wdt:P1435 ?desig. %s
  ?art schema:about ?item; schema:isPartOf <https://en.wikipedia.org/>.
  OPTIONAL { ?item wdt:P571 ?i. BIND(YEAR(?i) AS ?inc) }
  OPTIONAL { ?item wdt:P1216 ?nhle. }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". } }""" % BOX
by = {}
for b in q(HER):
    lat, lon = ll(b["c"]["value"]); bo = borough(lat, lon)
    if not bo: continue
    k = b["item"]["value"].rsplit("/", 1)[1]
    r = by.setdefault(k, {"qid": k, "name": b.get("itemLabel", {}).get("value"), "lat": lat, "lon": lon, "borough": bo, "wiki": b["art"]["value"], "designations": [], "nhle": b.get("nhle", {}).get("value")})
    d = b.get("desigLabel", {}).get("value")
    if d and d not in r["designations"]: r["designations"].append(d)
    if "inc" in b and "year" not in r: r["year"] = int(b["inc"]["value"])
rows = [r for r in by.values() if not shipped_near(r["lat"], r["lon"], r["name"])]
save("wikidata-heritage.json", rows, {"source": "Wikidata (P1435 heritage designation) with English Wikipedia article", "licence": "CC0 (Wikidata); Wikipedia text is CC BY-SA, rewrite in our words", "attribution": "Wikidata, CC0", "note": "year = inception (P571) where Wikidata has it"})
# 3. Open Plaques via Wikidata (P1893) gave only 12 London rows on 27 Nov: dropped
raise SystemExit
OP = """SELECT ?item ?itemLabel ?c ?op ?art WHERE { ?item wdt:P1893 ?op. %s
  OPTIONAL { ?art schema:about ?item; schema:isPartOf <https://en.wikipedia.org/>. }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". } }""" % BOX
rows = []
for b in q(OP):
    lat, lon = ll(b["c"]["value"]); bo = borough(lat, lon)
    if not bo: continue
    rows.append({"qid": b["item"]["value"].rsplit("/", 1)[1], "name": b.get("itemLabel", {}).get("value"), "lat": lat, "lon": lon, "borough": bo, "openplaques": b["op"]["value"], "wiki": b.get("art", {}).get("value")})
save("wikidata-openplaques.json", rows, {"source": "Wikidata items with an Open Plaques plaque id (P1893)", "licence": "CC0", "note": "stand-in while openplaques.org bulk endpoints return 503"})
