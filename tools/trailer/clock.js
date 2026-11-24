// Virtual clock for frame-by-frame rendering: time only moves when render.py calls __tick(dt).
(() => {
  let T = 0; const START = Date.parse('2026-11-24T09:00:00Z'); let raf = [], timers = [], id = 1;
  performance.now = () => T; Date.now = () => START + T;
  window.requestAnimationFrame = cb => { raf.push(cb); return raf.length; };
  window.cancelAnimationFrame = () => {};
  window.setTimeout = (cb, ms, ...a) => { const i = id++; timers.push({ i, at: T + (ms || 0), cb, a }); return i; };
  window.clearTimeout = i => { timers = timers.filter(x => x.i !== i); };
  window.setInterval = (cb, ms, ...a) => { const i = id++; const f = () => { cb(...a); timers.push({ i, at: T + ms, cb: f, a: [] }); }; timers.push({ i, at: T + ms, cb: f, a: [] }); return i; };
  window.clearInterval = window.clearTimeout;
  window.__tick = dt => {
    T += dt;
    for (;;) { timers.sort((a, b) => a.at - b.at); if (!timers.length || timers[0].at > T) break; const x = timers.shift(); try { x.cb(...x.a); } catch (e) { console.error(e); } }
    const cbs = raf; raf = []; cbs.forEach(cb => { try { cb(T); } catch (e) { console.error(e); } });
  };
})();
