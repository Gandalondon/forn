"""Forn trailer v2 (24 Nov): one continuous camera move (tools/trailer/film.html), frame by frame, 30 fps.
  python3 tools/trailer/film.py h stills 2 5 10 ...  -> tools/trailer/stills/film-h-*.jpg
  python3 tools/trailer/film.py h [music.mp3]        -> marketing/forn-trailer-16x9.mp4 (music laid under, -16 LUFS)
Beats can be overridden with FORN_BEATS='{"w1":[0.4,3.4], ...}' (JSON, merged over film.html's defaults).
"""
import sys, os, json, subprocess, threading, functools, http.server, socketserver
from playwright.sync_api import sync_playwright
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(D + '/../..'); FPS = 30
FMT = {'h': dict(vw=1280, vh=720, dsf=1.5, name='forn-trailer-16x9'), 'v': dict(vw=360, vh=640, dsf=3, name='forn-trailer-9x16')}

def serve():
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT); h.log_message = lambda *a: None
    s = socketserver.TCPServer(('127.0.0.1', 0), h); threading.Thread(target=s.serve_forever, daemon=True).start(); return s.server_address[1]

f = FMT[sys.argv[1]]; stills = sys.argv[2:3] == ['stills']; music = None if stills or len(sys.argv) < 3 else sys.argv[2]
port = serve()
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--use-gl=swiftshader', '--enable-webgl', '--ignore-gpu-blocklist'])
    pg = b.new_page(viewport={'width': f['vw'], 'height': f['vh']}, device_scale_factor=f['dsf'])
    pg.add_init_script('window.__FRAMES = true; window.__BEATS = ' + os.environ.get('FORN_BEATS', '{}'))
    pg.goto(f'http://127.0.0.1:{port}/tools/trailer/film.html'); pg.evaluate('document.fonts.ready'); pg.wait_for_load_state('networkidle')
    if stills:
        os.makedirs(D + '/stills', exist_ok=True)
        for s in sorted(float(v) for v in sys.argv[3:]):
            pg.evaluate(f'__at({s})'); pg.screenshot(path=f"{D}/stills/film-{sys.argv[1]}-{s}.jpg", type='jpeg', quality=90)
    else:
        n = int(round(pg.evaluate('__len') * FPS)); out = ROOT + '/marketing'; os.makedirs(out, exist_ok=True)
        tmp = f"{out}/{f['name']}.silent.tmp.mp4"
        ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'mjpeg', '-i', '-',
                               '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', tmp], stdin=subprocess.PIPE)
        for i in range(n):
            pg.evaluate(f'__at({i / FPS})'); ff.stdin.write(pg.screenshot(type='jpeg', quality=93))
            if i % 150 == 0: print(f'{i / FPS:.1f}s', flush=True)
        ff.stdin.close(); assert ff.wait() == 0
        final = f"{out}/{f['name']}.mp4"
        if music:
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', tmp, '-i', music, '-filter:a', 'loudnorm=I=-16:TP=-1.5:LRA=11',
                            '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', final + '.tmp.mp4'], check=True)
            os.replace(final + '.tmp.mp4', final); os.remove(tmp)
        else: os.replace(tmp, final)
        print('done', final)
    b.close()
