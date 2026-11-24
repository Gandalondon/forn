"""Forn trailer: plays the real landing page (site/index.html) on a virtual clock, one step per beat,
then the end card (the app icon's ball pulls together from dust, getforn.app at the bottom, like Hlid's).
The words come from the page itself, so copy changes there carry into the video: just re-run this.

  python3 tools/trailer/render.py h            -> marketing/forn-trailer-16x9.mp4
  python3 tools/trailer/render.py v            -> marketing/forn-trailer-9x16.mp4
  python3 tools/trailer/render.py h stills 3 10.5 27   -> tools/trailer/stills/*.jpg
"""
import sys, os, subprocess, threading, functools, http.server, socketserver
from playwright.sync_api import sync_playwright
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(D + '/../..'); SITE = ROOT + '/site'
FPS = 30
# Beats (s): FORN, You pass history (dust), Forn notices it (balls), At 9pm (zoom, then the card),
# The rest is dust, Every day adds a ring, Grow yours, then the end card. Hard cuts between.
BEATS = [2.2, 3.0, 3.4, 5.0, 3.0, 5.4, 3.4]
END = 4.6
FMT = {'h': dict(vw=1280, vh=720, dsf=1.5, ball=150, uf=27, ub=43, name='forn-trailer-16x9'),   # 1920 x 1080
       'v': dict(vw=360, vh=640, dsf=3, ball=100, uf=14, ub=40, name='forn-trailer-9x16')}      # 1080 x 1920

END_JS = r"""
(() => {
  const o = document.createElement('div'); o.id = 'endcard';
  o.style.setProperty('--uf', UF + 'px'); o.style.setProperty('--ub', UB + 'px');
  o.innerHTML = '<canvas></canvas><div class="url">getforn.app</div>'; document.body.appendChild(o);
  const c = o.querySelector('canvas'), x = c.getContext('2d'), dpr = devicePixelRatio;
  c.width = innerWidth * dpr; c.height = innerHeight * dpr; x.scale(dpr, dpr);
  const cx = innerWidth / 2, cy = innerHeight / 2, R = BALL / 2;
  let s = 7; const r = () => (s = (s * 16807) % 2147483647) / 2147483647;
  const P = Array.from({ length: 700 }, () => { const a = r() * 6.283, d = R * (1.4 + r() * 2.6), a2 = r() * 6.283, d2 = R * Math.sqrt(r()) * 0.9;
    return { x0: cx + Math.cos(a) * d, y0: cy + Math.sin(a) * d * 0.9, x1: cx + Math.cos(a2) * d2, y1: cy + Math.sin(a2) * d2, w: 0.08 + r() * 0.25 }; });
  const E = t => t * t * (3 - 2 * t), cl = v => Math.max(0, Math.min(1, v));
  window.__end = t => {   // t: seconds into the end card
    o.style.display = 'block'; x.clearRect(0, 0, innerWidth, innerHeight);
    const g = cl((t - 0.35) / 1.1);
    P.forEach(p => { const k = E(cl((g - p.w) / (1 - p.w))); if (k > 0.98) return;
      x.fillStyle = k < 0.5 ? '#C8C8C8' : '#8A8A8A'; x.beginPath();
      x.arc(p.x0 + (p.x1 - p.x0) * k, p.y0 + (p.y1 - p.y0) * k, 1.2, 0, 7); x.fill(); });
    const b = E(cl((g - 0.45) / 0.55));
    if (b > 0) { x.fillStyle = '#1A1A1A'; x.beginPath(); x.arc(cx, cy, R * b, 0, 7); x.fill(); }
  };
})();
"""

def serve():
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=SITE)
    h.log_message = lambda *a: None
    s = socketserver.TCPServer(('127.0.0.1', 0), h); threading.Thread(target=s.serve_forever, daemon=True).start()
    return s.server_address[1]

def main():
    f = FMT[sys.argv[1]]; stills = sys.argv[2:3] == ['stills']
    port = serve()
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--use-gl=swiftshader', '--enable-webgl', '--ignore-gpu-blocklist'])
        pg = b.new_page(viewport={'width': f['vw'], 'height': f['vh']}, device_scale_factor=f['dsf'])
        pg.add_init_script(path=D + '/clock.js')
        pg.goto(f'http://127.0.0.1:{port}/index.html')
        pg.add_style_tag(path=D + '/video.css')
        pg.evaluate(f"(() => {{ const BALL={f['ball']}, UF={f['uf']}, UB={f['ub']}; {END_JS} }})()")
        pg.evaluate('document.fonts.ready')
        for _ in range(10): pg.evaluate('__tick(100)')   # settle: fonts, fit the mark, first frames
        starts = [sum(BATS) for BATS in [BEATS[:i] for i in range(len(BEATS))]]; total = sum(BEATS) + END
        T = 0.0
        def advance_to(t):
            nonlocal T
            pg.evaluate(f'__tick({(t - T) * 1000})'); T = t
        def at(t):  # step changes happen exactly at beat starts
            for i, s0 in enumerate(starts[1:], 1):
                if T < s0 <= t:
                    advance_to(s0)
                    pg.keyboard.press('ArrowDown')
            advance_to(t)
            if t >= sum(BEATS): pg.evaluate(f'__end({t - sum(BEATS)})')
        if stills:
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
