/* Just Ask. — runtime behaviours (no dependencies). Classic script; exposes window.JustAsk.
   WordPress: enqueue in the footer with `defer`. Each init is safe to call more than once. */
(function () {
  'use strict';
  var reduce = window.matchMedia ? window.matchMedia('(prefers-reduced-motion: reduce)') : { matches: false };

  /* Hero face grid: random cells crossfade face <-> silhouette. Starts from the server-rendered
     layout (identical to Hero/hero-face-grid.webp), swaps a face and a silhouette together so the
     overall mix never drifts, pauses off-screen / hidden tab / pause button, never runs for
     prefers-reduced-motion. */
  function initFaceGrid(hero) {
    if (!hero || hero.__jaGrid) return;
    hero.__jaGrid = true;
    var cells = Array.prototype.slice.call(hero.querySelectorAll('.ja-facegrid li'));
    var btn = hero.querySelector('.ja-hero__pause');
    if (!cells.length || reduce.matches) return;
    var timer = null, visible = true, paused = false;
    function inView(el) {            // only animate cells the visitor can actually see
      var r = el.getBoundingClientRect(), h = hero.getBoundingClientRect();
      return r.right > h.left && r.left < h.right && r.bottom > h.top && r.top < h.bottom;
    }
    function pick(list, n) {
      var out = [], pool = list.slice();
      while (out.length < n && pool.length) out.push(pool.splice(Math.floor(Math.random() * pool.length), 1)[0]);
      return out;
    }
    function tick() {
      var small = window.innerWidth < 768;
      var vis = cells.filter(inView);
      var faces = vis.filter(function (c) { return c.classList.contains('is-face'); });
      var sils = vis.filter(function (c) { return c.classList.contains('is-sil'); });
      var n = small ? 1 : (Math.random() < 0.5 ? 1 : 2);   // pairs → 2–4 cells change on desktop, 2 on mobile
      pick(faces, n).forEach(function (c) { c.classList.remove('is-face'); c.classList.add('is-sil'); });
      pick(sils, n).forEach(function (c) { c.classList.remove('is-sil'); c.classList.add('is-face'); });
    }
    function run() {
      var go = visible && !paused && !document.hidden;
      var ms = parseFloat(getComputedStyle(hero).getPropertyValue('--ja-grid-interval')) || 2000;
      if (go && !timer) timer = setInterval(tick, ms);
      if (!go && timer) { clearInterval(timer); timer = null; }
    }
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (e) { visible = e[0].isIntersecting; run(); }).observe(hero);
    }
    document.addEventListener('visibilitychange', run);
    if (btn) btn.addEventListener('click', function () {
      paused = !paused;
      hero.classList.toggle('is-paused', paused);
      btn.setAttribute('aria-pressed', String(paused));
      btn.querySelector('.ja-pause-label').textContent = paused ? 'Play animation' : 'Pause animation';
      run();
    });
    hero.classList.add('is-animated');
    run();
  }

  /* Header: Menu toggle for mobile and tablet (<1024px). The panel is full height below the
     header bar and slides in from the right. While it's open: page scroll is locked, Tab stays
     inside the header (logo, toggle, menu links), Escape closes it and returns focus to the toggle.
     Crossing to desktop (>=1024px) closes it. */
  function initHeader(header) {
    if (!header || header.__jaMenu) return;
    header.__jaMenu = true;
    var btn = header.querySelector('.ja-menu-toggle');
    if (!btn) return;
    var root = document.documentElement;
    var desktop = window.matchMedia ? window.matchMedia('(min-width: 1024px)') : { matches: false };
    function isOpen() { return header.classList.contains('is-open'); }
    function place() {
      var bottom = Math.max(0, Math.round(header.getBoundingClientRect().bottom));
      header.style.setProperty('--ja-menu-top', bottom + 'px');
    }
    function set(open) {
      if (open) place();
      header.classList.toggle('is-open', open);
      btn.setAttribute('aria-expanded', String(open));
      btn.querySelector('.ja-menu-label').textContent = open ? 'Close' : 'Menu';
      root.classList.toggle('ja-menu-open', open);
      root.style.overflow = open ? 'hidden' : '';
    }
    btn.addEventListener('click', function () { set(!isOpen()); });
    document.addEventListener('keydown', function (e) {
      if (!isOpen()) return;
      if (e.key === 'Escape') { set(false); btn.focus(); return; }
      if (e.key !== 'Tab') return;
      var items = Array.prototype.filter.call(header.querySelectorAll('a[href], button'), function (el) {
        return el.offsetWidth || el.offsetHeight || el.getClientRects().length;
      });
      if (!items.length) return;
      var first = items[0], last = items[items.length - 1];
      if (!header.contains(document.activeElement)) { e.preventDefault(); first.focus(); }
      else if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
    window.addEventListener('resize', function () { if (isOpen()) place(); });
    var onDesktop = function () { if (desktop.matches && isOpen()) set(false); };
    if (desktop.addEventListener) desktop.addEventListener('change', onDesktop);
    else if (desktop.addListener) desktop.addListener(onDesktop);
  }

  /* Copy button (ClinicalQuestion "Copy the Question"). The button ships with `hidden` and is shown
     only when the browser can copy. It copies the panel's question text without the outer quote
     marks (or `data-ja-copy-text` if set). The label reads "Copied" for 2 seconds at the same width,
     and a polite live region announces it. */
  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text);
    return new Promise(function (resolve, reject) {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.setAttribute('readonly', '');
      ta.style.position = 'fixed'; ta.style.top = '0'; ta.style.left = '0'; ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      var ok = false;
      try { ok = document.execCommand('copy'); } catch (err) { ok = false; }
      document.body.removeChild(ta);
      if (ok) resolve(); else reject(new Error('copy failed'));
    });
  }
  function canCopy() {
    if (navigator.clipboard && window.isSecureContext) return true;
    return !!(document.queryCommandSupported && document.queryCommandSupported('copy'));
  }
  function initCopy(btn) {
    if (!btn || btn.__jaCopy) return;
    btn.__jaCopy = true;
    if (!canCopy()) return;            // stays hidden: nothing to offer without clipboard access
    var scope = btn.closest('.ja-question, .ja-cta') || document;   // ClinicalQuestion or CtaBand
    var label = btn.querySelector('.ja-copy-label') || btn;
    var status = scope.querySelector('.ja-copy-status');
    var original = label.textContent;
    var timer = null;
    function source() {
      if (btn.getAttribute('data-ja-copy-text')) return btn.getAttribute('data-ja-copy-text');
      var q = scope.querySelector('.ja-question__bracket, .ja-cta__question');
      return q ? q.textContent.replace(/\s+/g, ' ').trim().replace(/^["“”]+|["“”]+$/g, '').trim() : '';
    }
    btn.hidden = false;
    btn.addEventListener('click', function () {
      var text = source();
      if (!text) return;
      copyText(text).then(function () {
        btn.style.minWidth = btn.getBoundingClientRect().width + 'px';   // no width jump on the swap
        label.textContent = 'Copied';
        if (status) { status.textContent = ''; setTimeout(function () { status.textContent = 'Question copied to clipboard'; }, 50); }
        clearTimeout(timer);
        timer = setTimeout(function () {
          label.textContent = original;
          btn.style.minWidth = '';
          if (status) status.textContent = '';
        }, 2000);
      }, function () {
        if (status) status.textContent = 'Copy failed. Select the question to copy it.';
      });
    });
  }

  function initAll(root) {
    root = root || document;
    Array.prototype.forEach.call(root.querySelectorAll('.ja-hero'), initFaceGrid);
    Array.prototype.forEach.call(root.querySelectorAll('.ja-header'), initHeader);
    Array.prototype.forEach.call(root.querySelectorAll('[data-ja-copy]'), initCopy);
  }

  window.JustAsk = { initAll: initAll, initFaceGrid: initFaceGrid, initHeader: initHeader, initCopy: initCopy };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { initAll(); });
  else initAll();
})();
