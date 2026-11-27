"""Shared bits for the candidate pulls: Greater London borough lookup, spots.json dedupe, compact save."""
import json, math, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(ROOT, "content", "candidates")
BBOX = (51.28, -0.52, 51.70, 0.34)  # S, W, N, E around Greater London
_b = json.load(open(os.path.join(HERE, "london_boroughs.geojson")))
BOROUGHS = []
for f in _b["features"]:
    g = f["geometry"]; polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
    rings = [p[0] for p in polys]
    xs = [x for r in rings for x, y in r]; ys = [y for r in rings for x, y in r]
    BOROUGHS.append((f["properties"]["name"], rings, (min(xs), min(ys), max(xs), max(ys))))

def _inside(x, y, ring):
    c = False; j = len(ring) - 1
    for i in range(len(ring)):
        xi, yi = ring[i][:2]; xj, yj = ring[j][:2]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi + 1e-15) + xi: c = not c
        j = i
    return c

def borough(lat, lon):
    for name, rings, (a, b, c, d) in BOROUGHS:
        if a <= lon <= c and b <= lat <= d and any(_inside(lon, lat, r) for r in rings): return name
    return None

def dist(a, b):
    dy = (a[0] - b[0]) * 111320; dx = (a[1] - b[1]) * 111320 * math.cos(math.radians(a[0]))
    return math.hypot(dx, dy)

SPOTS = json.load(open(os.path.join(ROOT, "app", "src", "main", "assets", "spots.json")))
def _words(s): return {w.strip(".,'’()").lower() for w in (s or "").split() if len(w) > 3}
def shipped_near(lat, lon, name, m=100):
    """Same place within 100m and the same story (shared name words) as a shipped spot."""
    nw = _words(name)
    for s in SPOTS:
        for p in s.get("points", []):
            if dist((lat, lon), p[:2]) <= m:
                sw = _words(s.get("fact", "") + " " + s.get("line", "") + " " + s.get("place", ""))
                if not nw or len(nw & sw) >= max(1, min(2, len(nw))): return s["id"]
    return None

def save(name, rows, meta):
    path = os.path.join(OUT, name)
    with open(path, "w") as f:
        f.write('{"meta":' + json.dumps(meta, ensure_ascii=False) + ',\n"rows":[\n')
        f.write(",\n".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in rows))
        f.write("\n]}\n")
    print(name, len(rows))
