# Forn folio: frames of the 9pm open (dust pulling into balls), same staged history as the Play listing.
import sys, os
sys.argv=[sys.argv[0],'x']
HERE=os.path.dirname(os.path.abspath(__file__))
src=open(HERE+'/../listing/capture.py').read().split("if __name__ == '__main__':")[0]
exec(src)
OUT=HERE+'/screens'; os.makedirs(OUT,exist_ok=True); port=serve()
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
    pg=b.new_page(viewport={'width':412,'height':892},device_scale_factor=2.5); pg.add_init_script(BRIDGE)
    pg.goto(f'http://127.0.0.1:{port}/app/src/main/assets/web/index.html')
    t=0
    for ms in [60,120,180,240]:
        pg.wait_for_timeout(ms-t); t=ms; pg.screenshot(path=f'{OUT}/pull-{ms}.png')
    b.close()
