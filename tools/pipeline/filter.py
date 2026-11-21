"""Stage 2: free rules. Drop the dull majority before any writing.

Usage: python3 -I filter.py in.json [in2.json ...] > shortlist.json
Prints a short report to stderr: how many went at each rule.
"""
import json, re, sys
from collections import Counter

# Things that almost never carry a "well I never": organisations, current services, admin areas.
DULL_TYPES = {
    "constituency of the House of Commons", "electoral ward", "association football club", "football club",
    "school", "secondary school", "primary school", "state school", "academy", "independent school", "college",
    "business", "company", "enterprise", "shop", "supermarket", "retail park", "shopping centre",
    "medical facility", "hospital", "general hospital", "bus station", "bus garage", "tram stop",
    "sports club", "cricket club", "rugby union club", "tennis club", "golf course", "sports venue", "stadium",
    "leisure centre", "cinema", "hotel", "restaurant", "office building", "housing estate", "London Borough",
    "local government district", "political party", "organization", "nonprofit organization", "charity",
    "radio station", "newspaper", "library", "public library", "fire station", "police station",
    "census-designated place", "electoral division",
}
DATE = re.compile(r"\b(1[0-9]{3}|[1-9][0-9]{0,2}\s?(?:BC|BCE|AD)|AD\s?[0-9]{1,4}|"
                  r"(?:[0-9]+(?:st|nd|rd|th)|first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|twelfth)[- ]century|"
                  r"million years|Neolithic|Bronze Age|Iron Age|Roman|Saxon|Domesday|medieval|Norman|Pictish|Viking)\b", re.I)


def main():
    rows = [e for f in sys.argv[1:] for e in json.load(open(f))]
    why = Counter()
    keep = []
    seen = set()
    for e in rows:
        title = e["title"]
        if title in seen:
            why["duplicate"] += 1; continue
        seen.add(title)
        types = set(e.get("types") or [])
        if types and types <= DULL_TYPES:
            why["dull type"] += 1; continue
        if re.search(r"\b(constituency|F\.C\.|School|Academy|ward\))\b", title):
            why["dull title"] += 1; continue
        text = e.get("text") or e.get("intro") or ""
        if len(text) < 1200:
            why["too little to check against"] += 1; continue
        if not DATE.search(text):
            why["no date or period"] += 1; continue
        keep.append(e)
    print(f"{len(rows)} in, {len(keep)} kept. Dropped: {dict(why)}", file=sys.stderr)
    json.dump(keep, sys.stdout, indent=1)


main()
