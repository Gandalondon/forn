"""How many London facts before most days get a find? Real spots plus n synthetic ones."""
import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import replay
real = json.load(open("app/src/main/assets/spots.json"))
print("extra   " + "  ".join(f"{p[:28]:>28}" for p in replay.WEEKS))
for n in (map(int, sys.argv[1:]) if sys.argv[1:] else [0, 1000, 2000, 3000]):
    spots = [dict(s) for s in real] + replay.synthetic(n)
    replay._cache.clear()
    r = replay.run(spots, seeds=20)
    cells = []
    for p, w in r.items():
        t = w[2:]
        cells.append(f"{sum(a for a,_,_ in t)/len(t):.0%} days, {replay.TRIPS[p]:.0%} trips, {sum(b for _,b,_ in t)/len(t):.1f}/wk")
    print(f"{n:>5}   " + "  ".join(f"{c:>28}" for c in cells))
