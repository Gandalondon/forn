"""Forn trailer: plays the real landing page (site/index.html) on a virtual clock, one step per beat,
then the end card (the app icon's ball pulls together from dust, getforn.app at the bottom, like Hlid's).
The words come from the page itself, so copy changes there carry into the video: just re-run this.

  python3 tools/trailer/render.py h            -> marketing/forn-trailer-16x9.mp4
  python3 tools/trailer/render.py v            -> marketing/forn-trailer-9x16.mp4
  python3 tools/trailer/render.py h stills 3 10.5 27   -> tools/trailer/stills/*.jpg
"""
import sys, os, base64, subprocess, threading, functools, http.server, socketserver
from playwright.sync_api import sync_playwright
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(D + '/../..'); SITE = ROOT + '/site'
FPS = 30
# Beats (s): FORN, You pass history (dust), Forn notices it (balls), At 9pm (zoom, then the card),
# The rest is dust, Every day adds a ring, Grow yours, then the end card. Hard cuts between.
BEATS = [2.2, 3.0, 3.4, 3.6, 3.0, 6.2, 3.4]  # ring beat 6.2: rings appear one after another (24 Nov)
END = 4.6
FMT = {'h': dict(vw=1280, vh=720, dsf=1.5, ball=56, uf=27, ub=43, name='forn-trailer-16x9'),   # 1920 x 1080
       'v': dict(vw=360, vh=640, dsf=3, ball=28, uf=14, ub=40, name='forn-trailer-9x16')}      # 1080 x 1920

END_JS = r"""
(() => {
  // End card (24 Nov, Tony): the app icon's ring at the size of the Sniff and Relay end-card marks (84 px on a 1080 frame)
  // with getforn.app under it; Google Play badge bottom right and the trademark line bottom left, as Sniff's
  // (badge 84 px tall, 80 px from the right, 64 from the bottom; line 18 px, 80 px from the left). One quick 0.2 s fade.
  const o = document.createElement('div'); o.id = 'endcard'; o.style.setProperty('--k', K);
  o.innerHTML = '<div class="lock"><svg class="ring" viewBox="35 35 38 38"><circle cx="54" cy="54" r="17" fill="none" stroke="#1A1A1A" stroke-width="4"/></svg><div class="url">getforn.app</div></div>'
    + '<img class="badge" src="data:image/png;base64,BADGE" alt="Get it on Google Play"><div class="legal">Google Play and the Google Play logo are trademarks of Google LLC.</div>';
  document.body.appendChild(o);
  window.__end = t => { o.style.display = 'block'; o.style.opacity = Math.min(1, t / 0.2); };
})();
"""

def serve():
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=SITE)
    h.log_message = lambda *a: None
    s = socketserver.TCPServer(('127.0.0.1', 0), h); threading.Thread(target=s.serve_forever, daemon=True).start()
    return s.server_address[1]

def main():
    f = FMT[sys.argv[1]]; stills = sys.argv[2:3] == ['stills']; probe = sys.argv[2:3] == ['probe']
    port = serve()
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--use-gl=swiftshader', '--enable-webgl', '--ignore-gpu-blocklist'])
        pg = b.new_page(viewport={'width': f['vw'], 'height': f['vh']}, device_scale_factor=f['dsf'])
        pg.add_init_script(path=D + '/clock.js')
        pg.add_init_script('window.__VIDEO = true; window.__TODAY = ' + os.environ.get('FORN_TODAY', '[23, 2.5, 6]') + '; window.__DUST = 1.8; window.__NEAR = 0.72; window.__WIDE = [-0.14, -0.06]')  # 24 Nov: bigger dust; today's ring nearer, up and left (overlap is fine)
        pg.goto(f'http://127.0.0.1:{port}/index.html')
        pg.add_style_tag(path=D + '/video.css')
        badge = base64.b64encode(open(D + '/google-play-badge.png', 'rb').read()).decode()
        pg.evaluate(f"(() => {{ const K={1 / f['dsf']}; {END_JS.replace('BADGE', badge)} }})()")
        pg.evaluate('document.fonts.ready')
        for _ in range(10): pg.evaluate('__tick(100)')   # settle: fonts, fit the mark, first frames
        starts = [sum(BATS) for BATS in [BEATS[:i] for i in range(len(BEATS))]]; total = sum(BEATS) + END
        T = 0.0
        def advance_to(t):
            nonlocal T
            pg.evaluate(f'__tick({(t - T) * 1000})'); T = t
        # 9pm (24 Nov, Tony): the finds land on top of each other, a glimpse, not something to stop and read.
        events = [(starts[3] + 2.3, '__find(1)'), (starts[3] + 2.9, '__find(2)')]
        def at(t):  # step changes happen exactly at beat starts
            marks = sorted([(s0, None) for s0 in starts[1:]] + events)
            for s0, js in marks:
                if T < s0 <= t:
                    advance_to(s0)
                    if js: pg.evaluate(js)
                    else: pg.keyboard.press('ArrowDown')
            advance_to(t)
            if t >= sum(BEATS): pg.evaluate(f'__end({t - sum(BEATS)})')
        if probe:   # where today's balls land on screen at each time (to keep them off the words)
            for s in sorted(float(v) for v in sys.argv[3:]):
                at(s); print(s, pg.evaluate('window.__xy ? __xy() : null'))
        elif stills:
            os.makedirs(D + '/stills', exist_ok=True)
            for s in sorted(float(v) for v in sys.argv[3:]):
                at(s); pg.screenshot(path=f"{D}/stills/{sys.argv[1]}-{s}.jpg", type='jpeg', quality=90)
        else:
            out = ROOT + '/marketing'; os.makedirs(out, exist_ok=True); tmp = f"{out}/{f['name']}.tmp.mp4"
            ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'mjpeg', '-i', '-',
                                   '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', tmp], stdin=subprocess.PIPE)
            for i in range(int(round(total * FPS))):
                at(i / FPS); ff.stdin.write(pg.screenshot(type='jpeg', quality=93))
                if i % 150 == 0: print(f'{i / FPS:.1f}s', flush=True)
            ff.stdin.close(); assert ff.wait() == 0; os.replace(tmp, f"{out}/{f['name']}.mp4"); print('done', f"{out}/{f['name']}.mp4")
        b.close()

main()
