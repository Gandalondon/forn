"""Rule lint for fact files (RULES.md writing rules). Free, no network.
Usage: python3 -I tools/pipeline/lint.py file.json [more.json ...]   (exit 1 if any problem)"""
import json, re, sys, math
BANNED = r"\b(you|your|described as|allegedly|reportedly|famously|iconic|legendary)\b"
HEDGE = r"\b(may have|might have|possibly|probably|said to|reputedly)\b"
LONDON = (51.28, 51.70, -0.52, 0.34)
def dist(a, b):
    return math.hypot((a[0]-b[0])*111320, (a[1]-b[1])*111320*math.cos(math.radians(a[0])))
shipped = json.load(open("app/src/main/assets/spots.json"))
bad = 0
for path in sys.argv[1:]:
    for f in json.load(open(path)):
        p = []
        w = len(f["fact"].split())
        if w > 35: p.append(f"card {w} words")
        if not f["line"].startswith("Did you know, "): p.append("line doesn't start 'Did you know, '")
        if re.search(BANNED, f["fact"], re.I): p.append("card: " + re.search(BANNED, f["fact"], re.I).group(0))
        if re.search(BANNED, f["line"][14:], re.I): p.append("line: " + re.search(BANNED, f["line"][14:], re.I).group(0))
        for t in ("fact", "line"):
            h = re.search(HEDGE, f[t], re.I)
            if h: p.append(f"{t} hedge '{h.group(0)}' (fine only if the source hedges too)")
        for k in ("year", "topic", "source", "points", "place", "score"):
            if k not in f: p.append("missing " + k)
        for z in f.get("points", []):
            if not (LONDON[0] < z[0] < LONDON[1] and LONDON[2] < z[1] < LONDON[3]): p.append("point outside Greater London box")
            for s in shipped:
                if s["id"] == f["id"]: continue
                if s.get("topic") == f.get("topic") and any(dist(z, q) < 300 for q in s["points"]):
                    p.append(f"same topic within 300m of {s['id']}")
        if any(s["id"] == f["id"] for s in shipped) and "rewrite" not in path: p.append("id already shipped")
        if p:
            bad += 1
            print(f"{path}: {f['id']}: " + "; ".join(sorted(set(p))))
print(f"{bad} with notes")
sys.exit(1 if bad else 0)
