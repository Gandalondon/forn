"""Stage 1: gather every geotagged Wikipedia article in an area, with intro text, full plain text and Wikidata type.

Usage: python3 -I gather.py <area> <lat> <lng> <half-size km> <out.json>
Covers a square with a grid of 2km-radius geosearches (Wikipedia caps radius at 10km and 500 results per query).
"""
import hashlib, re, json, math, os, sys, time, urllib.parse, urllib.request
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
os.makedirs(CACHE, exist_ok=True)

UA = "FornPilot/0.1 (personal research project)"
API = "https://en.wikipedia.org/w/api.php"


def get(url, params=None, tries=4):
    if params:
        url += "?" + urllib.parse.urlencode(params)
    key = os.path.join(CACHE, hashlib.sha1(url.encode()).hexdigest() + ".json")
    if os.path.exists(key):
        return json.load(open(key))
    for i in range(12):
        try:
            time.sleep(0.4)  # be polite: one request at a time, a little apart
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=40) as r:
                data = json.loads(r.read())
            json.dump(data, open(key, "w"))
            return data
        except Exception as e:
            if i == 11:
                raise
            wait = 5 * (i + 1)
            if getattr(e, "code", None) == 429:
                wait = max(30, int(e.headers.get("Retry-After") or 30))
            time.sleep(wait)


def grid(lat, lng, half_km, step_km=2.5):
    dlat = 1 / 111.0
    dlng = 1 / (111.0 * math.cos(math.radians(lat)))
    n = int(half_km / step_km)
    for i in range(-n, n + 1):
        for j in range(-n, n + 1):
            yield lat + i * step_km * dlat, lng + j * step_km * dlng


def main():
    area, lat, lng, half, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
    pages = {}
    for la, ln in grid(lat, lng, half):
        d = get(API, {"action": "query", "list": "geosearch", "gscoord": f"{la}|{ln}", "gsradius": 2000,
                      "gslimit": 500, "format": "json", "gsprimary": "primary"})
        for p in d["query"]["geosearch"]:
            pages[p["pageid"]] = {"pageid": p["pageid"], "title": p["title"], "lat": p["lat"], "lng": p["lon"]}
    ids = list(pages)
    print(area, "articles:", len(ids), file=sys.stderr, flush=True)
    # Intro extract, Wikidata id, page length.
    for k in range(0, len(ids), 20):
        chunk = ids[k:k + 20]
        d = get(API, {"action": "query", "pageids": "|".join(map(str, chunk)), "prop": "extracts|pageprops|info",
                      "exintro": 1, "explaintext": 1, "ppprop": "wikibase_item", "format": "json"})
        for pid, p in d["query"]["pages"].items():
            e = pages[int(pid)]
            e["intro"] = p.get("extract", "")
            e["qid"] = p.get("pageprops", {}).get("wikibase_item")
            e["length"] = p.get("length", 0)
    # Full text, for the write and check stages (only for pages with some substance).
    for e in pages.values():
        if e.get("length", 0) < 2500:
            continue
        if re.search(r"\b(constituency|F\.C\.|School|Academy|ward\)|Library|Hospital|Centre)\b", e["title"]):
            continue
        d = get(API, {"action": "query", "pageids": e["pageid"], "prop": "extracts", "explaintext": 1, "format": "json"})
        e["text"] = d["query"]["pages"][str(e["pageid"])].get("extract", "")
    # Wikidata "instance of" labels, for the free filter.
    qids = [e["qid"] for e in pages.values() if e.get("qid")]
    types = {}
    for k in range(0, len(qids), 150):
        vals = " ".join("wd:" + q for q in qids[k:k + 150])
        q = f"""SELECT ?item ?typeLabel ?inception WHERE {{ VALUES ?item {{ {vals} }}
          OPTIONAL {{ ?item wdt:P31 ?type . }} OPTIONAL {{ ?item wdt:P571 ?inception . }}
          SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }} }}"""
        d = get("https://query.wikidata.org/sparql", {"query": q, "format": "json"})
        for b in d["results"]["bindings"]:
            qid = b["item"]["value"].rsplit("/", 1)[1]
            t = types.setdefault(qid, {"types": set(), "inception": None})
            if "typeLabel" in b:
                t["types"].add(b["typeLabel"]["value"])
            if "inception" in b and not t["inception"]:
                t["inception"] = b["inception"]["value"][:10]
    for e in pages.values():
        t = types.get(e.get("qid"), {})
        e["types"] = sorted(t.get("types", []))
        e["inception"] = t.get("inception")
        e["area"] = area
    json.dump(sorted(pages.values(), key=lambda e: e["title"]), open(out, "w"), indent=1)
    print(area, "done", len(pages), file=sys.stderr)


main()
