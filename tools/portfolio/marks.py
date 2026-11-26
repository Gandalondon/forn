"""Forn folio: the elastic FORN, rendered by getforn.app's own fitting code at three box shapes, set on one canvas.
-> tools/portfolio/out/forn-logo.png"""
import os, threading, functools, http.server, socketserver
from playwright.sync_api import sync_playwright
from PIL import Image
HERE=os.path.dirname(os.path.abspath(__file__)); SITE=os.path.abspath(HERE+'/../../site'); OUT=HERE+'/out'
h=functools.partial(http.server.SimpleHTTPRequestHandler,directory=SITE); h.log_message=lambda *a:None
s=socketserver.TCPServer(('127.0.0.1',0),h); threading.Thread(target=s.serve_forever,daemon=True).start()
BOXES=[(260,960),(960,960),(1800,280)]  # tall, square, wide (css px of the word itself)
W,H,GAP=3560,1716,150
shots=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome')
    for i,(w,hh) in enumerate(BOXES):
        pg=b.new_page(viewport={'width':w,'height':hh})
        pg.goto(f'http://127.0.0.1:{s.server_address[1]}/index.html')
        pg.add_style_tag(content='.mark{padding:0!important} canvas{display:none!important} .bar,.step{display:none!important}')
        pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(3500); pg.evaluate('window.dispatchEvent(new Event("resize"))'); pg.wait_for_timeout(500)
        f=f'/tmp/mark-{i}.png'; pg.screenshot(path=f); shots.append(Image.open(f).convert('RGB')); pg.close()
    b.close()
tot=sum(i.width for i in shots)+GAP*(len(shots)-1); x=(W-tot)//2; base=(H+max(i.height for i in shots))//2
c=Image.new('RGB',(W,H),'white')
for i in shots: c.paste(i,(x,base-i.height)); x+=i.width+GAP
c.save(OUT+'/forn-logo.png'); print(c.size)
