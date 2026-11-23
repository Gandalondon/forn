import json, math, random, base64, struct
from shapely.geometry import shape, LineString, Point
from shapely.ops import unary_union
from shapely.prepared import prep
g = json.load(open("geo/london_boroughs.geojson"))
london = unary_union([shape(f['geometry']).buffer(0) for f in g['features']])
# Thames centreline, west to east (bridges and bends), hand-placed; widths in metres grow downstream.
T = [(-0.337,51.403),(-0.3085,51.4115),(-0.3105,51.425),(-0.3229,51.4317),(-0.3246,51.4452),(-0.3069,51.4575),(-0.3200,51.4720),
     (-0.2875,51.4875),(-0.2683,51.4724),(-0.2525,51.4720),(-0.2300,51.4880),(-0.2133,51.4666),(-0.1880,51.4650),(-0.1710,51.4820),
     (-0.1495,51.4846),(-0.1270,51.4880),(-0.1230,51.4945),(-0.1219,51.5008),(-0.1170,51.5087),(-0.1043,51.5097),(-0.0877,51.5079),
     (-0.0754,51.5055),(-0.0520,51.5010),(-0.0360,51.5080),(-0.0280,51.4990),(-0.0230,51.4860),(-0.0050,51.4850),(0.0000,51.4950),
     (0.0030,51.5030),(0.0150,51.4990),(0.0350,51.4950),(0.0600,51.4970),(0.1000,51.5100),(0.1400,51.5050),(0.1800,51.4850),(0.2200,51.4700),(0.2600,51.4650)]
LAT0 = 51.5; KX = 111.32 * math.cos(math.radians(LAT0)); KY = 111.32
def km(p): return ((p[0] + 0.1278) * KX, (p[1] - 51.5074) * KY)
river = []
for i, (a, b) in enumerate(zip(T, T[1:])):
    w = 0.22 + 0.30 * i / len(T)  # half-width km
    river.append(LineString([km(a), km(b)]).buffer(w))
river = unary_union(river)
L = unary_union([shape({'type': 'Polygon', 'coordinates': [[km(c) for c in ring] for ring in (poly.exterior.coords, *[h.coords for h in poly.interiors])]}) for poly in (london.geoms if hasattr(london, 'geoms') else [london])])
Lp, Rp = prep(L), prep(river)
minx, miny, maxx, maxy = L.bounds
rnd = random.Random(7); pts = []
N = 90000
while len(pts) < N:
    x, y = rnd.uniform(minx, maxx), rnd.uniform(miny, maxy)
    r = math.hypot(x, y)
    if rnd.random() > 0.25 + 0.75 * math.exp(-r / 9): continue  # denser towards the centre, like the city itself
    P = Point(x, y)
    if not Lp.contains(P) or Rp.contains(P): continue
    pts.append((x, y))
# edge: the boundary itself, a little denser
edge = []
for poly in (L.geoms if hasattr(L, 'geoms') else [L]):
    ring = poly.exterior; n = int(ring.length / 0.08)
    for i in range(n):
        p = ring.interpolate(i / n, normalized=True); edge.append((p.x + rnd.gauss(0, .03), p.y + rnd.gauss(0, .03)))
# places Forn knows
spots = json.load(open('app/src/main/assets/spots.json'))
places = [km((s['points'][0][1], s['points'][0][0])) for s in spots]
places = [p for p in places if Lp.contains(Point(p))]
def pack(a): return base64.b64encode(b''.join(struct.pack('<hh', int(x * 100), int(y * 100)) for x, y in a)).decode()
json.dump({'dust': pack(pts), 'edge': pack(edge), 'places': pack(places), 'bounds': [minx, miny, maxx, maxy]}, open('london-dust.json', 'w'))
print(len(pts), len(edge), len(places), [round(b, 1) for b in L.bounds])
