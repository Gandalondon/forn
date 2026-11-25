# Run by capture.py (pg = the phone page). Moments for the Play screenshots, all from the real app page.
pg.wait_for_timeout(4000); pg.screenshot(path=f'{OUT}/1-card.png')                      # 9pm: tonight's first find
for _ in range(3): pg.mouse.click(206, 300); pg.wait_for_timeout(700)                    # page through tonight's three
pg.wait_for_timeout(9000); pg.screenshot(path=f'{OUT}/2-rings.png')                      # pulled back to the month
pg.evaluate("controls.autoRotate = false; camera.position.sub(controls.target).multiplyScalar(0.45).add(controls.target); controls.update()")
pg.wait_for_timeout(1200); pg.screenshot(path=f'{OUT}/2b-close.png')
f = pg.evaluate("(() => { const k = keptInOrder().filter(f => f.d > 3 && f.fact.length < 190); const f = k[3] || k[0]; showPeek(f, true); return f.id; })()")
pg.wait_for_timeout(2500); pg.screenshot(path=f'{OUT}/3-peek.png'); print('peek', f)
pg.evaluate("document.getElementById('peekClose').click()"); pg.wait_for_timeout(800)
pg.evaluate("document.getElementById('how').click()"); pg.wait_for_timeout(800); pg.screenshot(path=f'{OUT}/4-how.png')
