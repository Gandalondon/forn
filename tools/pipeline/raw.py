"""Fetch whole Wikipedia articles as rough plain text through the action=raw route (not rate-limited like the API).

Usage: put one title per line in titles.txt, then python3 -I raw.py. Results build up in raw.json (resumable).
"""
import json, re, sys, time, urllib.parse, urllib.request, os
UA = "FornPilot/0.1 (personal research project)"
out = json.load(open('raw.json')) if os.path.exists('raw.json') else {}
for t in [l.strip() for l in open('titles.txt') if l.strip()]:
    if t in out: continue
    url = "https://en.wikipedia.org/w/index.php?" + urllib.parse.urlencode({"title": t, "action": "raw", "redirect": "yes"})
    for i in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=40) as r:
                w = r.read().decode(); break
        except Exception as e:
            w = None; time.sleep(10)
    if w is None: print(t, "FAILED", flush=True); continue
    m = re.match(r"#REDIRECT\s*\[\[([^\]#|]+)", w, re.I)
    if m:
        url = "https://en.wikipedia.org/w/index.php?" + urllib.parse.urlencode({"title": m.group(1), "action": "raw"})
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=40) as r: w = r.read().decode()
    # rough plain text: drop refs, templates, files; keep link text
    x = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?</ref>", "", w, flags=re.S)
    for _ in range(4): x = re.sub(r"\{\{[^{}]*\}\}", "", x)
    x = re.sub(r"\[\[(?:File|Image):[^\]]*\]\]", "", x)
    x = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", x)
    x = re.sub(r"'{2,}", "", x); x = re.sub(r"<[^>]+>", "", x)
    out[t] = x.strip()
    print(t, len(x), flush=True)
    json.dump(out, open('raw.json', 'w'), indent=1, ensure_ascii=False)
    time.sleep(1)
