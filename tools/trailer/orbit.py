"""Orbit test (24 Nov): renders tools/trailer/orbit.html frame by frame to marketing/forn-orbit-test.mp4 (1920 x 1080, 30 fps).
  python3 tools/trailer/orbit.py            -> the clip
  python3 tools/trailer/orbit.py stills 1 2 -> tools/trailer/stills/orbit-*.jpg
"""
import sys, os, subprocess, threading, functools, http.server, socketserver
from playwright.sync_api import sync_playwright
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(D + '/../..'); FPS = 30; LEN = 5.0

def serve():
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT); h.log_message = lambda *a: None
    s = socketserver.TCPServer(('127.0.0.1', 0), h); threading.Thread(target=s.serve_forever, daemon=True).start(); return s.server_address[1]

port = serve()
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--use-gl=swiftshader', '--enable-webgl', '--ignore-gpu-blocklist'])
    pg = b.new_page(viewport={'width': 1280, 'height': 720}, device_scale_factor=1.5)
    pg.add_init_script(path=D + '/clock.js')
    pg.goto(f'http://127.0.0.1:{port}/tools/trailer/orbit.html'); pg.evaluate('document.fonts.ready'); pg.evaluate('__tick(0)')
    T = 0.0
    def at(t):
        global T
        pg.evaluate(f'__tick({(t - T) * 1000})'); T = t
    if sys.argv[1:2] == ['stills']:
        os.makedirs(D + '/stills', exist_ok=True)
        for s in sorted(float(v) for v in sys.argv[2:]): at(s); pg.screenshot(path=f'{D}/stills/orbit-{s}.jpg', type='jpeg', quality=90)
    else:
        out = ROOT + '/marketing'; os.makedirs(out, exist_ok=True); tmp = out + '/forn-orbit-test.tmp.mp4'
        ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'mjpeg', '-i', '-',
                               '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', tmp], stdin=subprocess.PIPE)
        for i in range(int(LEN * FPS)): at(i / FPS); ff.stdin.write(pg.screenshot(type='jpeg', quality=93))
        ff.stdin.close(); assert ff.wait() == 0; os.replace(tmp, out + '/forn-orbit-test.mp4'); print('done')
    b.close()
