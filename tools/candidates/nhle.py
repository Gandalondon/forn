"""Historic England NHLE: listed building points and scheduled monuments in Greater London.
Source: services-eu1.arcgis.com (Historic England Open Data Hub). OGL v3."""
import json, sys, time, urllib.request, urllib.parse
from common import *
B = "https://services-eu1.arcgis.com/ZOdPfBS3aqqDYPUQ/arcgis/rest/services/National_Heritage_List_for_England_NHLE_v02_VIEW/FeatureServer"
def fetch(layer, fields):
    out, off = [], 0
    global last
    while True:
        q = {"where": "1=1", "geometry": f"{BBOX[1]},{BBOX[0]},{BBOX[3]},{BBOX[2]}", "geometryType": "esriGeometryEnvelope",
             "inSR": 4326, "spatialRel": "esriSpatialRelIntersects", "outFields": fields, "outSR": 4326,
             "returnGeometry": "true", **({"returnCentroid": "true"} if layer == 6 else {}), "f": "json", "resultOffset": off, "resultRecordCount": 2000}
        d = json.load(urllib.request.urlopen(B + f"/{layer}/query?" + urllib.parse.urlencode(q), timeout=120))
        if "error" in d: raise SystemExit(d)
        fs = d.get("features", []); out += fs; off += len(fs)
        print(layer, off, file=sys.stderr)
        if not fs or not d.get("exceededTransferLimit"): return out
def pt(f):
    g = f.get("centroid") or f.get("geometry") or {}
    if "x" in g: return g["y"], g["x"]
    if "points" in g: p = g["points"][0]; return p[1], p[0]
    if "rings" in g: r = g["rings"][0]; return sum(p[1] for p in r) / len(r), sum(p[0] for p in r) / len(r)
def yr(ms): return time.gmtime(ms / 1000).tm_year if ms else None
for layer, fields, fname, kind in [(0, "ListEntry,Name,Grade,ListDate", "nhle-listed.json", "listed"),
                                   (6, "ListEntry,Name,SchedDate", "nhle-scheduled.json", "scheduled")]:
    rows, skipped = [], 0
    for f in fetch(layer, fields):
        a = f["attributes"]; p = pt(f)
        if not p: continue
        lat, lon = round(p[0], 5), round(p[1], 5); bo = borough(lat, lon)
        if not bo: continue
        if shipped_near(lat, lon, a["Name"]): skipped += 1; continue
        r = {"id": a["ListEntry"], "name": a["Name"], "lat": lat, "lon": lon, "borough": bo}
        if kind == "listed": r["grade"] = a.get("Grade")
        r["listed"] = yr(a.get("ListDate") or a.get("SchedDate"))
        rows.append(r)
    save(fname, rows, {"source": "Historic England, National Heritage List for England (NHLE)", "layer": kind,
         "licence": "OGL v3.0", "attribution": "Contains public sector information licensed under the Open Government Licence v3.0.",
         "url": "https://historicengland.org.uk/listing/the-list/list-entry/{id}", "skipped_as_shipped": skipped,
         "note": "listed = year first listed or scheduled, not the building's date"})
