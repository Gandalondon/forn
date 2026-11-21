"""Harvest Wikipedia "Did you know" hooks whose bolded article has coordinates inside Greater London.

Usage: python3 -I dyk.py out.json [max_seconds]
Walks Wikipedia:Did you know archive/YYYY/Month newest first. Caches every request (shares gather.py's cache).
Saves progress after every month, so it can be stopped and resumed.
Needs geo/london_boroughs.geojson beside it (Greater London's 33 boroughs; not in git).
"""
import json, os, re, sys, time
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, "gather.py")).read().replace("\nmain()\n", "\n")  # reuse get() without running gather
g = {"__file__": os.path.join(here, "gather.py")}
exec(compile(src, "gather.py", "exec"), g)
get, API = g["get"], g["API"]

out = sys.argv[1]
MAX = float(sys.argv[2]) if len(sys.argv) > 2 else 7200
t0 = time.time()

# Greater London boundary (33 boroughs).
polys = []
for f in json.load(open(os.path.join(here, "geo", "london_boroughs.geojson")))["features"]:
    gm = f["geometry"]
    rings = [gm["coordinates"][0]] if gm["type"] == "Polygon" else [p[0] for p in gm["coordinates"]]
    polys += rings


def inside(lat, lng):
    if not (51.28 < lat < 51.70 and -0.52 < lng < 0.34):
        return False
    for ring in polys:
        c = False
        j = len(ring) - 1
        for i in range(len(ring)):
            xi, yi = ring[i][0], ring[i][1]
            xj, yj = ring[j][0], ring[j][1]
            if (yi > lat) != (yj > lat) and lng < (xj - xi) * (lat - yi) / (yj - yi) + xi:
                c = not c
            j = i
        if c:
            return True
    return False


MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]
BOLD = re.compile(r"'''+\s*\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")

state = json.load(open(out)) if os.path.exists(out) else {"done": [], "hooks": [], "checked": 0}
done = set(state["done"])
months = [(y, m) for y in range(2026, 2003, -1) for m in range(11, -1, -1) if not (y == 2026 and m > 10) and not (y == 2004 and m < 1)]
for y, m in months:
    name = f"Wikipedia:Did you know archive/{y}/{MONTHS[m]}"
    if name in done:
        continue
    if time.time() - t0 > MAX:
        print("time cap reached", file=sys.stderr)
        break
    try:
        d = get(API, {"action": "parse", "page": name, "prop": "wikitext", "format": "json", "formatversion": 2})
    except Exception as e:
        print(name, "failed", e, file=sys.stderr)
        break
    text = d.get("parse", {}).get("wikitext", "")
    hooks = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("*") or "..." not in line[:12]:
            continue
        arts = [a.strip().replace("_", " ") for a in BOLD.findall(line)]
        if arts:
            hooks.append((line, arts))
    titles = sorted({a[0].upper() + a[1:] for _, al in hooks for a in al if a})
    coords = {}
    for k in range(0, len(titles), 50):
        chunk = titles[k:k + 50]
        r = get(API, {"action": "query", "titles": "|".join(chunk), "prop": "coordinates", "coprimary": "primary",
                      "redirects": 1, "format": "json", "formatversion": 2})
        q = r.get("query", {})
        alias = {}
        for n in q.get("normalized", []):
            alias[n["to"]] = alias.get(n["from"], n["from"])
        for rd in q.get("redirects", []):
            alias[rd["to"]] = alias.get(rd["from"], rd["from"])
        for p in q.get("pages", []):
            if p.get("coordinates"):
                c = p["coordinates"][0]
                coords[p["title"]] = (c["lat"], c["lon"])
                src = p["title"]
                seen = set()
                while src in alias and src not in seen:
                    seen.add(src); src = alias[src]
                    coords[src] = (c["lat"], c["lon"], p["title"])
    n0 = len(state["hooks"])
    for line, arts in hooks:
        for a in arts:
            key = a[0].upper() + a[1:]
            c = coords.get(key)
            if c and inside(c[0], c[1]):
                hook = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", line.lstrip("* "))
                hook = re.sub(r"'{2,}", "", hook)
                hook = re.sub(r"\{\{([^}]*)\}\}", lambda mm: "" if mm.group(1).lower().startswith(("main page image", "-")) else mm.group(1).split("|")[-1], hook)
                hook = re.sub(r"\s+", " ", hook).strip()
                state["hooks"].append({"hook": hook, "article": c[2] if len(c) > 2 else key, "lat": c[0], "lng": c[1],
                                       "archive": f"{y}/{MONTHS[m]}", "raw": line})
    state["checked"] += len(hooks)
    state["done"].append(name)
    json.dump(state, open(out, "w"), indent=1)
    print(name, "hooks", len(hooks), "london", len(state["hooks"]) - n0, "total", len(state["hooks"]),
          f"{int(time.time() - t0)}s", file=sys.stderr, flush=True)
