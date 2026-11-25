"""Forn Google Play listing art (25 Nov 2026), in the same format as Sniff's (android-release/play-listing in the sniff repo):
five 1080x1920 screenshots (headline, then a real app screen in a plain off-black phone) and the 1024x500 feature graphic,
plus the 512 icon. Play wants 24-bit PNG with no alpha, so everything is saved as RGB.
Screens come from capture.py (real app page, real facts). Headlines: two lines, the first at least as long as the second.
  python3 tools/listing/make_listing.py   -> marketing/play-listing/*.png
"""
import os, base64, json
from playwright.sync_api import sync_playwright
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(HERE + '/../..'); SCR = HERE + '/screens'
OUT = ROOT + '/marketing/play-listing'; os.makedirs(OUT, exist_ok=True)
FONT = ROOT + '/site/instrument-sans.ttf'; INK = '#1A1A1A'
SHOTS = [  # file name, screen, headline, alt text (Play allows 140 characters)
    ('1-live-your-day', '2b-close.png', 'Live your day.<br>Forn notices.', 'Close up on the rings: each ball is a place you passed, placed by the time you passed it, with dust for the rest'),
    ('2-at-9pm', '1-card.png', 'At 9pm, find out<br>what you passed.', "A 9pm find: the world's first cash machine opened at Barclays in Enfield in June 1967"),
    ('3-rings', '2-rings.png', 'One ring for<br>every day.', "Your rings: today in the middle, older days rippling out, black balls for places uncovered and dust for the rest"),
    ('4-read-again', '3-peek.png', 'Read any find<br>again later.', 'A find reopened from its ball: Christopher Marlowe was killed in a house in Deptford in 1593'),
    ('5-nothing-leaves', None, 'Nothing leaves<br>your phone.', 'Nothing leaves your phone, above the Forn ring'),
]
def uri(p, mime): return f'data:{mime};base64,' + base64.b64encode(open(p, 'rb').read()).decode()
CSS = f"""@font-face{{font-family:'Instrument Sans';src:url({uri(FONT, 'font/ttf')}) format('truetype');font-weight:400 700;font-stretch:75% 100%}}
*{{box-sizing:border-box}} html,body{{margin:0}}
body{{width:1080px;height:1920px;background:#FFFFFF;position:relative;overflow:hidden;font-family:'Instrument Sans',sans-serif;color:{INK}}}
h1{{position:absolute;left:48px;right:48px;top:152px;margin:0;text-align:center;font:600 88px/1.0 'Instrument Sans',sans-serif;letter-spacing:.005em;text-wrap:balance}}
.ph{{position:absolute;left:217px;top:416px;width:646px;padding:23px;border-radius:88px;background:{INK}}}
.ph img{{display:block;width:100%;border-radius:66px}}"""
RING = f'<svg viewBox="35 35 38 38" width="168" height="168"><circle cx="54" cy="54" r="17" fill="none" stroke="{INK}" stroke-width="4"/></svg>'
def shot(scr, head):
    if scr is None:
        return (f'<style>{CSS} body{{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:144px}}</style>'
                f'<h1 style="position:static;font-size:128px;line-height:.98">{head}</h1>{RING}')
    return f'<style>{CSS}</style><h1>{head}</h1><div class="ph"><img src="{uri(os.path.join(SCR, scr), "image/png")}"></div>'
# Feature graphic: FORN stretching to fill its box (the brand rule), the strapline under it in body type, on white.
# Play can crop the edges and lays a play button over the middle when there's a promo video, so keep a margin.
FEATURE = f"""<style>{CSS} body{{width:1024px;height:500px}}
.w{{position:absolute;left:64px;right:64px;top:64px;height:276px}} .w svg{{width:100%;height:100%;display:block;overflow:visible}}
.w text{{font:600 200px 'Instrument Sans';fill:{INK}}}
p{{position:absolute;left:64px;right:64px;top:380px;margin:0;text-align:center;font:400 28px/36px 'Instrument Sans';color:{INK};text-wrap:balance}}</style>
<div class="w"><svg id="s" preserveAspectRatio="none"><text id="t">FORN</text></svg></div>
<p>The history you pass every day in London, told at 9pm.</p>
<script>const t=document.getElementById('t'),b=t.getBBox(),c=document.createElement('canvas').getContext('2d');c.font="600 200px 'Instrument Sans'";
const m=c.measureText('FORN');document.getElementById('s').setAttribute('viewBox',`${{b.x}} ${{-m.actualBoundingBoxAscent}} ${{b.width}} ${{m.actualBoundingBoxAscent+m.actualBoundingBoxDescent}}`);</script>"""
ICON = f'<style>html,body{{margin:0;width:512px;height:512px;background:#FFFFFF;display:flex;align-items:center;justify-content:center}}</style>' \
       f'<svg viewBox="0 0 108 108" width="512" height="512"><circle cx="54" cy="54" r="17" fill="none" stroke="{INK}" stroke-width="4"/></svg>'
def save(pg, html, name, w, h):
    pg.set_viewport_size({'width': w, 'height': h}); pg.set_content(html); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
    tmp = f'{OUT}/{name}.tmp.png'; pg.screenshot(path=tmp); Image.open(tmp).convert('RGB').save(f'{OUT}/{name}.png'); os.remove(tmp)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page()
    for name, scr, head, alt in SHOTS: save(pg, shot(scr, head), f'forn-play-screenshot-{name}', 1080, 1920)
    save(pg, FEATURE, 'forn-play-feature-graphic', 1024, 500)
    save(pg, ICON, 'forn-play-icon', 512, 512)
    b.close()
open(f'{OUT}/forn-play-alt-text.txt', 'w').write('\n'.join(f'forn-play-screenshot-{n}.png: {a}' for n, _, _, a in SHOTS) +
    '\nforn-play-feature-graphic.png: The word FORN stretched wide, above the line The history you pass every day in London, told at 9pm\n')
print('done', OUT)
