"""Rule lint for fact files (RULES.md writing rules). Free, no network.
Usage: python3 -I tools/pipeline/lint.py file.json [more.json ...]   (exit 1 if any problem)"""
import json, re, sys, math, glob
# Copy check (rule 16, 27 Nov): source text for every id, from all content/facts/sources-*.json files.
SRC = {}
for g in glob.glob("content/facts/sources-*.json"):
    d = json.load(open(g))
    if isinstance(d, dict):
        for k, v in d.items(): SRC[k] = " ".join(v) if isinstance(v, list) else str(v)
def toks(t): return re.findall(r"[a-z0-9']+", t.lower())
def copied(ours, src):
    """Longest run of words copied from the source, ignoring anything in quotation marks (quotes are allowed)."""
    a = toks(re.sub(r'["\u201c][^"\u201d]*["\u201d]', " ", ours)); b = " " + " ".join(toks(src)) + " "; best = 0
    for i in range(len(a)):
        for j in range(i + best + 1, len(a) + 1):
            if " " + " ".join(a[i:j]) + " " in b: best = j - i
            else: break
    return best
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
        if w > 35 or len(f["fact"]) > 150: p.append(f"card {w} words, {len(f['fact'])} characters (max 35 and 150)")
        lw, lc = len(f["line"].split()), len(f["line"])
        if lw > 20 or lc > 120: p.append(f"line {lw} words, {lc} characters (max 20 and 120)")
        src = f.get("source_text") or SRC.get(f["id"])
        if src is None: p.append("no source text saved (rule 13)")
        else:
            n = copied(f["fact"] + " " + f["line"][14:], src)
            if n >= 10: p.append(f"{n} words in a row copied from the source (max 9, quotes aside)")
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
