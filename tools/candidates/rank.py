"""Flag rule 14 / rule 3 leads and rank candidates per borough by how much they'd add to the replay go bar.
route = how often the replay's people pass it (250m), weighted to the commuter and outer Londoner (the go bar),
to days out, and to outings that pass few shipped spots today. Run after the pulls: python3 tools/candidates/rank.py"""
import json, os, re, sys, math
from collections import defaultdict
from common import *
sys.path.insert(0, os.path.join(ROOT, "tools", "replay"))
import replay
from replay import WEEKS, ROUTINE, legs, samples
R14 = re.compile(r"\b(STUDIOS?|CINEMA|PICTURE (HOUSE|PALACE|THEATRE)|ODEON|GAUMONT|GRANADA|MUSIC HALL|DANCE HALL|BALLROOM|HIPPODROME|PALLADIUM|EMPIRE|COLISEUM|ALEXANDRA PALACE|ABBEY ROAD|RECORDING|JAZZ|CLUB)\b", re.I)
R3 = re.compile(r"\b(PRISON|GAOL|POLICE STATION|POLICE OFFICE|MAGISTRATES|SESSIONS HOUSE|CRIMINAL COURT|LOCK-?UP|WATCH ?HOUSE|GALLOWS|GIBBET|TYBURN|STOCKS|WHIPPING|PILLORY|EXECUTION|NEWGATE|BOW STREET|CLINK|MARSHALSEA|BRIDEWELL|HIGHWAYM[AE]N|EXECUTION DOCK)\b", re.I)
C = os.path.join(ROOT, "content", "candidates")
def load(f): return json.load(open(os.path.join(C, f)))["rows"]
cands = []
her = load("wikidata-heritage.json"); her_nhle = {r["nhle"] for r in her if r.get("nhle")}
for r in load("nhle-listed.json"):
    if str(r["id"]) in her_nhle: continue  # the Wikidata row (with its article) stands for it
    q = {"I": 3, "II*": 2}.get(r.get("grade"), 0.4)
    cands.append(dict(src="nhle-listed", ref=r["id"], name=r["name"].title(), lat=r["lat"], lon=r["lon"], borough=r["borough"], q=q, note=f"grade {r.get('grade')}"))
for r in load("nhle-scheduled.json"):
    cands.append(dict(src="nhle-scheduled", ref=r["id"], name=r["name"], lat=r["lat"], lon=r["lon"], borough=r["borough"], q=2.5, note="scheduled monument"))
for r in her:
    g = 3 if any("Grade I " in d + " " for d in r["designations"]) else 2
    cands.append(dict(src="wikidata-heritage", ref=r["qid"], name=r["name"], lat=r["lat"], lon=r["lon"], borough=r["borough"], q=g, wiki=r["wiki"], note=", ".join(r["designations"][:2])))
for r in load("wikidata-filming.json"):
    old = [w for w in r["works"] if w["year"] and w["year"] <= 2001]
    c = dict(src="wikidata-filming", ref=r["qid"], name=r["name"], lat=r["lat"], lon=r["lon"], borough=r["borough"], q=1 + min(3, len(old)), wiki=r.get("wiki"),
             note="; ".join(f"{w['title']} ({w['year']})" for w in old[:4]) or "only recent works")
    if old: c["flags"] = ["rule14"]
    cands.append(c)
for r in load("wikidata-music-crime.json"):
    t = set(r["types"]); fl = []
    if t & {"recording studio", "music venue", "nightclub", "cinema", "concert hall"}: fl.append("rule14")
    if t & {"prison", "courthouse", "execution site"}: fl.append("rule3")
    cands.append(dict(src="wikidata-music-crime", ref=r["qid"], name=r["name"], lat=r["lat"], lon=r["lon"], borough=r["borough"], q=2, wiki=r["wiki"],
                      note=", ".join(r["types"]) + (f", opened {r['year']}" if r.get("year") else "") + (f", closed {r['closed']}" if r.get("closed") else ""), flags=fl))
for c in cands:
    fl = set(c.get("flags", []))
    if R14.search(c["name"]): fl.add("rule14")
    if R3.search(c["name"]): fl.add("rule3")
    c["flags"] = sorted(fl)
# grid for fast nearness
G = 0.004
grid = defaultdict(list)
for i, c in enumerate(cands): grid[(int(c["lat"] / G), int(c["lon"] / G))].append(i)
def near(p, m=250):
    gy, gx = int(p[0] / G), int(p[1] / G)
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            for i in grid.get((gy + dy, gx + dx), ()):
                if dist(p, (cands[i]["lat"], cands[i]["lon"])) <= m: yield i
PW = {"commuter": 1.0, "outer": 1.0}
route = defaultdict(float)
for persona, (pool, week, town) in WEEKS.items():
    pw = next((v for k, v in PW.items() if k in persona.lower()), 0.3)
    for name, outing in pool.items():
        shipped = len(replay.passed(persona + name, outing, SPOTS))
        w = pw * (2 if not ROUTINE.match(name) else 1) / (1 + shipped)
        hit = set()
        for leg in legs(outing):
            for p in samples(leg): hit.update(near(p))
        for i in hit: route[i] += w
for i, c in enumerate(cands):
    c["route"] = round(route[i], 2)
    gap = min((dist((c["lat"], c["lon"]), p[:2]) for s in SPOTS for p in s["points"]), default=9e9)
    c["gap_m"] = int(gap)
    c["rank"] = round((c.pop("q") + 1.5 * len(c["flags"])) * (1 + 4 * c["route"]) * (1.3 if gap > 500 else 1), 2)
by = defaultdict(list)
for c in cands: by[c["borough"]].append(c)
out, summary = {}, []
for b, cs in by.items():
    cs.sort(key=lambda c: -c["rank"]); top = cs[:40]; out[b] = top
    summary.append((round(sum(c["route"] for c in top), 1), b, len(cs), sum(1 for c in cs if c["route"] > 0)))
summary.sort(reverse=True)
json.dump({"meta": {"how": __doc__.strip(), "areas_by_go_bar_value": [{"borough": b, "route_value_top40": v, "candidates": n, "on_replay_routes": o} for v, b, n, o in summary]},
           "areas": out}, open(os.path.join(C, "ranked.json"), "w"), ensure_ascii=False, separators=(",", ":"))
leads = sorted([c for c in cands if c["flags"]], key=lambda c: -c["rank"])
json.dump({"meta": {"note": "rule14 = music, film, TV 25+ years old; rule3 = crime, scandal, executions as history. Name and type matches: leads, check each."},
           "rule14": [c for c in leads if "rule14" in c["flags"]][:300], "rule3": [c for c in leads if "rule3" in c["flags"]][:300]},
          open(os.path.join(C, "leads.json"), "w"), ensure_ascii=False, indent=0)
print(len(cands), "candidates;", sum(1 for c in cands if "rule14" in c["flags"]), "rule14;", sum(1 for c in cands if "rule3" in c["flags"]), "rule3")
for v, b, n, o in summary[:12]: print(f"{b:28} route {v:6} cands {n:6} on routes {o}")
