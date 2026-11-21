"""Stage 4 helper: flag every number and proper noun in a written fact that its source text doesn't contain.

Usage: python3 -I check.py written/area.json data/area.json [more data files]
This is the mechanical half of the check. Claude then rereads each flagged line against the source itself.
"""
import json, re, sys

facts = json.load(open(sys.argv[1]))
pages = {}
for f in sys.argv[2:]:
    for e in json.load(open(f)):
        pages[e["title"]] = (e.get("text") or "") + " " + (e.get("intro") or "")

STOP = {"Did", "The", "A", "An", "It", "It's", "In", "For", "One", "When", "Its", "London's", "Nobody", "Two", "This"}
for f in facts:
    # Source titles are kept whole: brackets are part of real titles, e.g. "Ophelia (Millais)" (bug fixed 21 Nov).
    titles = [t.strip() for t in re.sub(r"^Wikipedia:\s*", "", f["source"]).split(";")]
    text = " ".join(pages.get(t, "") for t in titles)
    if not text.strip():
        print(f"{f['id']}: SOURCE TEXT NOT FOUND for {titles}")
        continue
    tokens = re.findall(r"\b\d[\d,]*\b|\b[A-Z][a-zA-Z'’]+\b", f["fact"])
    missing = sorted({t for t in tokens if t not in STOP and t.replace(",", "") not in text.replace(",", "")})
    print(f"{f['id']}: {'ok' if not missing else 'CHECK ' + ', '.join(missing)}")
