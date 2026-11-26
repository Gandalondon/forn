# Forn folio: the Your rings screen at 3x (1236 x 2676), to put on the phone in the hero photo.
import sys, os
sys.argv=[sys.argv[0],'x']
HERE=os.path.dirname(os.path.abspath(__file__))
exec(open(HERE+'/../listing/capture.py').read().split("if __name__ == '__main__':")[0])
port=serve()
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
    pg=b.new_page(viewport={'width':412,'height':892},device_scale_factor=3); pg.add_init_script(BRIDGE)
    pg.goto(f'http://127.0.0.1:{port}/app/src/main/assets/web/index.html'); pg.wait_for_timeout(4000)
    for _ in range(3): pg.mouse.click(206,300); pg.wait_for_timeout(700)
    pg.wait_for_timeout(9000); pg.screenshot(path=HERE+'/out/forn-rings-screen.png'); b.close()
