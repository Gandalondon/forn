"""Forn folio hero: every step of getforn.app at 1728x1080, stacked into one tall still (like Hlid's homepage still).
Usage: python3 tools/portfolio/hero.py  -> tools/portfolio/out/forn-home.jpg"""
import os, threading, functools, http.server, socketserver
from playwright.sync_api import sync_playwright
from PIL import Image
HERE=os.path.dirname(os.path.abspath(__file__)); SITE=os.path.abspath(HERE+'/../../site'); OUT=HERE+'/out'; os.makedirs(OUT,exist_ok=True)
h=functools.partial(http.server.SimpleHTTPRequestHandler,directory=SITE); h.log_message=lambda *a:None
s=socketserver.TCPServer(('127.0.0.1',0),h); threading.Thread(target=s.serve_forever,daemon=True).start()
W,H=1728,1080; frames=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
    pg=b.new_page(viewport={'width':W,'height':H})
    pg.goto(f'http://127.0.0.1:{s.server_address[1]}/index.html'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(2500)
    for i in range(8):
        if i: pg.keyboard.press('ArrowRight'); pg.wait_for_timeout(4500)
        f=f'/tmp/step-{i}.png'; pg.screenshot(path=f); frames.append(f)
    b.close()
