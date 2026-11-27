"""Wikidata SPARQL helpers shared by wikidata.py and wikidata_types.py."""
import json, sys, urllib.request, urllib.parse
from common import *
EP = "https://query.wikidata.org/sparql"
def q(s):
    r = urllib.request.Request(EP + "?" + urllib.parse.urlencode({"query": s, "format": "json"}), headers={"User-Agent": "Forn-data-dig/1.0 (hello@getforn.app)"})
    return json.load(urllib.request.urlopen(r, timeout=300))["results"]["bindings"]
BOX = f'SERVICE wikibase:box {{ ?item wdt:P625 ?c. bd:serviceParam wikibase:cornerSouthWest "Point({BBOX[1]} {BBOX[0]})"^^geo:wktLiteral. bd:serviceParam wikibase:cornerNorthEast "Point({BBOX[3]} {BBOX[2]})"^^geo:wktLiteral. }}'
def ll(c):
    lon, lat = c.replace("Point(", "").rstrip(")").split()[:2]; return round(float(lat), 5), round(float(lon), 5)
