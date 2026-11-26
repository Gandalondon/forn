"""Forn folio hero, v2 (Tony 26 Nov): a picture of how getforn.app feels, not a copy of it.
Steps 0-5 are words only (no rings, no card), At 9pm on black; Grow yours ends on the rings from above, edge to edge.
-> tools/portfolio/out/forn-home-v2.jpg"""
import os, threading, functools, http.server, socketserver
from playwright.sync_api import sync_playwright
from PIL import Image
HERE=os.path.dirname(os.path.abspath(__file__)); SRC=os.path.abspath(HERE+'/../../site'); OUT=HERE+'/out'
# Render from a temp copy with one hook line, so the camera can be set from outside (the page keeps its code in a closure).
import shutil; SITE='/tmp/forn-site-copy'; shutil.rmtree(SITE,ignore_errors=True); shutil.copytree(SRC,SITE)
_h=open(SITE+'/index.html').read(); open(SITE+'/index.html','w').write(_h.replace('<script>\n(() => {','<script>\n(() => {\nwindow.__ev = c => eval(c);',1))
h=functools.partial(http.server.SimpleHTTPRequestHandler,directory=SITE); h.log_message=lambda *a:None
s=socketserver.TCPServer(('127.0.0.1',0),h); threading.Thread(target=s.serve_forever,daemon=True).start()
W,H,LH=1728,1080,int(os.environ.get('LH','1900'))
url=f'http://127.0.0.1:{s.server_address[1]}/index.html'
frames=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
    pg=b.new_page(viewport={'width':W,'height':H})
    pg.goto(url); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(2500)
    pg.add_style_tag(content='canvas{visibility:hidden!important} .card,.pips{display:none!important} .shade{transition:none!important;background:#1A1A1A!important}')
    for i in range(6):
        if i: pg.keyboard.press('ArrowRight'); pg.wait_for_timeout(2200 if i==3 else 900)
        if i==3: pg.evaluate("document.body.classList.add('dark')"); pg.wait_for_timeout(500)
        f=f'/tmp/h2-{i}.png'; pg.screenshot(path=f); frames.append(f)
    pg.close()
    # Grow yours: a taller frame, rings from straight above, wider than the page so they run off both edges.
    pg=b.new_page(viewport={'width':W,'height':LH})
    pg.goto(url); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(2500)
    for i in range(6): pg.keyboard.press('ArrowRight'); pg.wait_for_timeout(500)
    pg.wait_for_timeout(3000)
    pg.add_style_tag(content='.step .note,.step .btn{display:none!important}')
    pg.evaluate("c => window.__ev(c)", f"""(()=>{{ const w=innerWidth,h=innerHeight; camera.aspect=w/h; camera.setViewOffset(w,h,0,-h*{os.environ.get('OFF','0.1')},w,h); camera.updateProjectionMatrix();
      const vf=THREE.MathUtils.degToRad(camera.fov)/2, hf=Math.atan(Math.tan(vf)*camera.aspect);
      to=null; spin=0; cam={{target:new THREE.Vector3(), dist:(RT+1)/(Math.tan(hf)*{os.environ.get('SPAN','1.12')}), elev:Math.PI/2-0.0001, az:0.6}}; }})()""")
    pg.wait_for_timeout(800); f='/tmp/h2-6.png'; pg.screenshot(path=f); frames.append(f); b.close()
ims=[Image.open(f).convert('RGB') for f in frames]
c=Image.new('RGB',(W,sum(i.height for i in ims)),'white'); y=0
for i in ims: c.paste(i,(0,y)); y+=i.height
c.save(OUT+'/forn-home-v2.jpg',quality=88); print(c.size)
