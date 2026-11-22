"""Go/no-go replay: run weeks of outings against spots.json and count how many
days get a find. Mirrors the app: a zone fires once you're within its radius,
told places drop out, up to five a night by the nightly mix.
Run: python3 tools/replay/replay.py [spots.json ...]"""
import json, math, random, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from routes import TONY, COMMUTER, OUTER, UNDER

def era(y):
    for lim, name in [(43, "prehistory"), (410, "roman"), (1066, "saxon"), (1485, "medieval"), (1603, "tudor"),
                      (1714, "stuart"), (1837, "georgian"), (1901, "victorian"), (1945, "early-20c"), (2000, "late-20c")]:
        if y < lim: return name
    return "21c"

def dist(a, b):
    dy = (a[0] - b[0]) * 111320
    dx = (a[1] - b[1]) * 111320 * math.cos(math.radians(a[0]))
    return math.hypot(dx, dy)

def samples(pts, step=40):
    for a, b in zip(pts, pts[1:]):
        n = max(1, int(dist(a, b) / step))
        for i in range(n):
            t = i / n
            yield (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
    yield pts[-1]

def legs(outing):
    if outing and isinstance(outing[0], tuple) and outing[0][0] != UNDER:
        return [outing]  # a plain waypoint list
    return [l for l in outing if not (isinstance(l, tuple) and l[0] == UNDER)]

_cache = {}
def passed(name, outing, spots):
    if name not in _cache:
        hit = set()
        for leg in legs(outing):
            for p in samples(leg):
                for s in spots:
                    if s["id"] in hit: continue
                    if any(dist(p, (z[0], z[1])) <= z[2] for z in s["points"]): hit.add(s["id"])
        _cache[name] = hit
    return _cache[name]

def pick(cands):
    out = []
    cands = list(cands)
    while cands and len(out) < 5:
        best = max(cands, key=lambda s: s["score"] - 1.5 * sum(o["era"] == s["era"] for o in out)
                   - 1.5 * sum(o["topic"] == s["topic"] for o in out))
        out.append(best); cands.remove(best)
    return out

# A week of outings per persona: each day a list of choices (one picked at random per slot).
WEEKS = {
    "Tony (SW20, home)": (TONY, [
        [["dog-cannon-hill", "dog-beverley-brook", "dog-common"], ["wimbledon-town", "morden-errand", "kingston-errand", None]],
    ] * 5 + [
        [["country-ranmore", "country-box-hill"]],
        [["kew-richmond", "greenwich", "dog-common"]],
    ], {"west-end", "city", "mayfair-knightsbridge"}),  # one trip into town a week, on a random weekday
    "Commuter (Clapham to the City)": (COMMUTER, [
        [["office-barbican", "office-guildhall", "office-leadenhall", "office-moorfields"]],
    ] * 4 + [[["soho-evening", "office-guildhall"]]] + [
        [["clapham-local", "brixton-market", "battersea-park"]],
        [["southbank", "camden", "clapham-local"]],
    ], set()),
    "Outer (Bromley)": (OUTER, [
        [["bromley-local", "bromley-shops", "beckenham-park"]],
    ] * 5 + [
        [["orpington-errand", "croydon", "chislehurst-caves"]],
        [["eltham-blackheath", "victoria-westminster", "bromley-local"]],
    ], set()),
}

import re
ROUTINE = re.compile(r"^(dog-|office-|bromley-local|bromley-shops|beckenham-park|clapham-local|soho-evening)")
TRIPS = {}

def run(spots, weeks=8, seeds=50):
    for s in spots: s["era"] = era(s["year"])
    byid = {s["id"]: s for s in spots}
    res = {}
    for persona, (pool, week, town) in WEEKS.items():
        _cache.clear()
        per_week = [[0, 0, 0] for _ in range(weeks)]  # find days, finds, dust (passed but not told that night)
        trips = [0, 0]  # days out beyond the daily routine (weeks 3+), and how many got a find
        for seed in range(seeds):
            rnd = random.Random(seed)
            told = set()
            for w in range(weeks):
                town_day = rnd.randrange(5) if town else -1
                for d, slots in enumerate(week):
                    names = [rnd.choice(c) for c in slots]
                    if d == town_day: names.append(rnd.choice(sorted(town)))
                    today = set()
                    for n in names:
                        if n: today |= passed(n, pool[n], spots)
                    cands = [byid[i] for i in today - told]
                    got = pick(cands)
                    told |= {g["id"] for g in got}
                    if w >= 2 and any(n and not ROUTINE.match(n) for n in names):
                        trips[0] += 1; trips[1] += bool(got)
                    per_week[w][0] += bool(got); per_week[w][1] += len(got); per_week[w][2] += len(cands) - len(got)
        res[persona] = [(a / seeds / 7, b / seeds, c / seeds) for a, b, c in per_week]
        TRIPS[persona] = trips[1] / max(1, trips[0])
    return res

if __name__ == "__main__":
    paths = sys.argv[1:] or ["app/src/main/assets/spots.json"]
    spots = []
    for p in paths: spots += json.load(open(p))
    print(f"{len(spots)} spots")
    for persona, weeks in run(spots).items():
        print(f"\n{persona}")
        print("week  days with a find  finds  dust left")
        for i, (a, b, c) in enumerate(weeks, 1):
            print(f"{i:>4}  {a:>15.0%}  {b:>5.1f}  {c:>9.1f}")
        tail = weeks[2:]
        print(f"weeks 3 to 8, days out beyond the routine that get a find: {TRIPS[persona]:.0%}")
        print(f"weeks 3 to 8: {sum(a for a,_,_ in tail)/len(tail):.0%} of days get a find, {sum(b for _,b,_ in tail)/len(tail):.1f} finds a week")

def synthetic(n, seed=1, centre_share=0.5):
    """n made-up spots spread over Greater London: centre_share clustered round the centre
    (like real history), the rest even across the boroughs' box. For 'how many do we need?'."""
    rnd = random.Random(seed)
    out = []
    while len(out) < n:
        if rnd.random() < centre_share:
            lat, lng = rnd.gauss(51.512, 0.045), rnd.gauss(-0.11, 0.07)
        else:
            lat, lng = rnd.uniform(51.29, 51.69), rnd.uniform(-0.51, 0.33)
        if not (51.29 < lat < 51.69 and -0.51 < lng < 0.33): continue
        out.append({"id": f"syn{len(out)}", "score": rnd.choice([7, 7, 8, 8, 8, 9]), "year": rnd.choice([-200, 100, 900, 1200, 1550, 1650, 1750, 1850, 1920, 1970, 1990, 2010]),
                    "topic": rnd.choice("war transport music film sport royals people buildings names crime everyday".split()),
                    "points": [[lat, lng, rnd.choice([250, 300, 400, 500])]]})
    return out
