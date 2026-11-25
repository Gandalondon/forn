"""Forn Play listing: capture real app screens (app/src/main/assets/web/index.html) in a phone-sized browser (25 Nov).
The page gets a stand-in for the Android bridge holding a believable history built from the shipped facts (spots.json):
tonight's three finds, then a couple of months of rings. Every card shown is a real fact from the app.
  python3 tools/listing/capture.py probe        -> frames every 1.5 s, to pick moments
  python3 tools/listing/capture.py              -> tools/listing/screens/*.png
"""
import sys, os, json, random, datetime as D, threading, functools, http.server, socketserver
from playwright.sync_api import sync_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(HERE + '/../..'); OUT = HERE + '/screens'
spots = json.load(open(ROOT + '/app/src/main/assets/spots.json')); spots = spots if isinstance(spots, list) else spots['spots']
by = {s['id']: s for s in spots}
TONIGHT = ['first-atm', 'duck-island-bombs', 'bomber-command-roof']  # the landing page's three, all real London facts
TONIGHT = [i for i in TONIGHT if i in by] or [s['id'] for s in sorted(spots, key=lambda s: -s.get('score', 0))[:3]]
today = D.date(2026, 11, 25); key = lambda d: (today - D.timedelta(days=d)).isoformat()
def at(d, h): t = D.datetime.combine(today - D.timedelta(days=d), D.time(int(h), int(h % 1 * 60))); return int(t.timestamp() * 1000)
r = random.Random(7); pool = [s for s in spots if s['id'] not in TONIGHT]; r.shuffle(pool)
hour = lambda: r.choice([8 + r.random() * 1.2, 17.5 + r.random() * 1.5, 12.5 + r.random(), 7 + r.random() * 15])
finds = [dict(id=i, fact=by[i]['fact'], place=by[i]['place'], day=key(0), at=at(0, h)) for i, h in zip(TONIGHT, [8.6, 13.1, 17.9])]
dust = [dict(id=f'd0-{i}', day=key(0), at=at(0, h)) for i, h in enumerate([7.6, 9.4, 11.6, 15.4, 16.5, 19.6, 20.4])]
for d in range(1, 26):
    if r.random() < 0.3: continue
    for _ in range(r.choice([0, 1, 1, 2, 2, 3])):
        if not pool: break
        s = pool.pop(); finds.append(dict(id=s['id'], fact=s['fact'], place=s['place'], day=key(d), at=at(d, hour())))
    for i in range(r.randint(0, 4)): dust.append(dict(id=f'd{d}-{i}', day=key(d), at=at(d, hour())))
STATE = dict(today=key(0), finds=finds, dust=dust, cards=TONIGHT, recording=False, saved='', fences='')
BRIDGE = """window.Forn = (() => { const S = %s; let seen = false;
  return { state: () => JSON.stringify(Object.assign({}, S, { cards: seen ? [] : S.cards })), seen: () => { seen = true; },
    tellNow: () => {}, record: () => '', share: () => {}, build: () => 0 }; })();""" % json.dumps(STATE)
def serve():
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT); h.log_message = lambda *a: None
    s = socketserver.TCPServer(('127.0.0.1', 0), h); threading.Thread(target=s.serve_forever, daemon=True).start(); return s.server_address[1]
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); port = serve()
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--use-gl=swiftshader', '--enable-webgl', '--ignore-gpu-blocklist'])
        pg = b.new_page(viewport={'width': 412, 'height': 892}, device_scale_factor=2.5)
        pg.add_init_script(BRIDGE)
        pg.goto(f'http://127.0.0.1:{port}/app/src/main/assets/web/index.html'); pg.evaluate('document.fonts.ready')
        if sys.argv[1:2] == ['probe']:
            for i in range(12): pg.wait_for_timeout(1500); pg.screenshot(path=f'{OUT}/probe-{i:02d}.png')
        else:
            exec(open(HERE + '/shots.py').read())
        b.close()
