# Forn folio: How it works from the top, stopping after Tell me more so no line is cut at the bottom.
import sys, os
sys.argv=[sys.argv[0],'x']
HERE=os.path.dirname(os.path.abspath(__file__))
exec(open(HERE+'/../listing/capture.py').read().split("if __name__ == '__main__':")[0])
port=serve()
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
    pg=b.new_page(viewport={'width':412,'height':892},device_scale_factor=2.5); pg.add_init_script(BRIDGE)
    pg.goto(f'http://127.0.0.1:{port}/app/src/main/assets/web/index.html'); pg.wait_for_timeout(3000)
    for _ in range(3): pg.mouse.click(206,300); pg.wait_for_timeout(700)
    pg.wait_for_timeout(2000)
    pg.evaluate("document.getElementById('how').click()"); pg.wait_for_timeout(800)
    pg.evaluate("""(()=>{const s=document.getElementById('sheet');const h=[...s.querySelectorAll('h3')].find(x=>x.textContent.trim()==='Privacy');
      let n=h.closest('section')||h; let x=n; while(x){ if(x.style) x.style.visibility='hidden'; x=x.nextElementSibling; } s.scrollTop=0; })()""")
    pg.wait_for_timeout(400); pg.screenshot(path='/tmp/scr/4-how.png'); b.close()
