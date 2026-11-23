/* Just Ask. review build — page behaviours not covered by the design system's bundle.js:
   Resource Library filters, contact form validation, placeholder-link notices. No dependencies. */
(function () {
  'use strict';
  var ARROW = '<svg class="ja-arrow" viewBox="0 0 13 24" aria-hidden="true"><path d="M0 11h9.17L5.6 7.41 6.99 6 13 12l-6.01 6-1.39-1.41L9.17 13H0z"></path></svg>';
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  /* ---------- Resource Library ---------- */
  function initLibrary() {
    var root = document.getElementById('ja-library');
    var R = window.JA_LIBRARY;
    if (!root || !R) return;
    var STEPS = [['diag', 'Diagnosing migraine'], ['treat', 'Treating migraine'], ['ongoing', 'Ongoing care']];
    var GROUPS = { women: 'Women’s Health', peds: 'Pediatrics', older: 'Older Adults' };
    var ACTION = { 'Quick Guide': 'View Guide', 'Guideline': 'Read Guideline', 'Tool': 'Open Tool', 'Article': 'Read Article', 'Video': 'Watch Video', 'Podcast': 'Listen' };
    var selects = root.querySelectorAll('select[data-key]');
    var results = root.querySelector('.ja-results');
    var count = root.querySelector('.ja-results-count');
    var empty = root.querySelector('.ja-empty');
    var clearBtns = root.querySelectorAll('[data-ja-clear]');
    var st = { step: 'all', group: 'all', format: 'all' };

    // Read filters from the URL (e.g. ?group=women from After the Yes cards)
    var params = new URLSearchParams(location.search);
    Array.prototype.forEach.call(selects, function (s) {
      var v = params.get(s.dataset.key);
      if (v && s.querySelector('option[value="' + v.replace(/"/g, '') + '"]')) st[s.dataset.key] = v;
      s.value = st[s.dataset.key];
    });

    function card(r) {
      var tags = '<li class="ja-tag ja-tag--format ja-tag--' + r.f.toLowerCase().replace(/\s+/g, '-') + '">' + esc(r.f) + '</li>' + (r.g ? '<li class="ja-tag">' + GROUPS[r.g] + '</li>' : '');
      return '<li><article class="ja-resource"><ul class="ja-tags" aria-label="Labels">' + tags + '</ul>' +
        '<h3 class="ja-h3 ja-resource__title">' + esc(r.t) + '</h3>' +
        (r.d ? '<p class="ja-body ja-resource__text">' + esc(r.d) + '</p>' : '') +
        '<a class="ja-button ja-button--outline ja-resource__action" href="' + esc(r.u) + '" target="_blank" rel="noopener">' + (ACTION[r.f] || 'Open') + '<span class="ja-visually-hidden">: ' + esc(r.t) + ' (opens in a new tab)</span></a></article></li>';
    }
    function render() {
      var match = R.filter(function (r) {
        return (st.step === 'all' || r.s.indexOf(st.step) > -1) && (st.group === 'all' || r.g === st.group) && (st.format === 'all' || r.f === st.format);
      });
      var html = '';
      STEPS.forEach(function (s) {
        if (st.step !== 'all' && st.step !== s[0]) return;
        // All steps: each resource listed once, under its first step. One step: everything tagged with it.
        var items = match.filter(function (r) { return st.step === 'all' ? r.s[0] === s[0] : true; });
        if (!items.length) return;
        html += '<section class="ja-results-group"><div class="ja-results-group__head"><h2 class="ja-h3">' + s[1] + '</h2><span class="ja-results-group__count">' +
          (items.length === 1 ? '1 resource' : items.length + ' resources') + '</span></div><ul class="ja-results-grid">' + items.map(card).join('') + '</ul></section>';
      });
      results.innerHTML = html;
      count.textContent = 'Showing ' + match.length + ' of ' + R.length + ' resources';
      empty.hidden = match.length !== 0;
      var active = st.step !== 'all' || st.group !== 'all' || st.format !== 'all';
      clearBtns[0].hidden = !active;
      Array.prototype.forEach.call(selects, function (s) { s.classList.toggle('is-active', st[s.dataset.key] !== 'all'); });
      // keep the URL shareable
      var q = new URLSearchParams();
      Object.keys(st).forEach(function (k) { if (st[k] !== 'all') q.set(k, st[k]); });
      var url = location.pathname + (q.toString() ? '?' + q.toString() : '');
      if (window.history && history.replaceState) history.replaceState(null, '', url);
    }
    Array.prototype.forEach.call(selects, function (s) {
      s.addEventListener('change', function () { st[s.dataset.key] = s.value; render(); });
    });
    Array.prototype.forEach.call(clearBtns, function (b) {
      b.addEventListener('click', function () {
        st = { step: 'all', group: 'all', format: 'all' };
        Array.prototype.forEach.call(selects, function (s) { s.value = 'all'; });
        render();
        selects[0].focus();
      });
    });
    root.querySelector('form').addEventListener('submit', function (e) { e.preventDefault(); });
    render();
  }

  /* ---------- Contact form: validate, then go to the Thank You page (nothing is sent) ---------- */
  function initContact() {
    var form = document.getElementById('ja-contact-form');
    if (!form) return;
    var alertBox = form.querySelector('.ja-form-alert');
    var emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
    function check(input) {
      var v = input.value.trim();
      if (!input.required) return true;
      if (!v) return false;
      if (input.type === 'email') return emailRe.test(v);
      return true;
    }
    function setError(input, on) {
      var field = input.closest('.ja-field');
      var id = input.id + '-error';
      var msg = field.querySelector('.ja-field__error');
      field.classList.toggle('is-error', on);
      input.setAttribute('aria-invalid', String(on));
      if (on && !msg) {
        msg = document.createElement('p');
        msg.className = 'ja-field__error';
        msg.id = id;
        msg.innerHTML = '<span class="ja-field__error-mark" aria-hidden="true">!</span>' + esc(input.dataset.error);
        field.appendChild(msg);
        input.setAttribute('aria-describedby', id);
      } else if (!on && msg) {
        msg.remove();
        input.removeAttribute('aria-describedby');
      }
    }
    var submitted = false;
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      submitted = true;
      var bad = [];
      Array.prototype.forEach.call(form.querySelectorAll('.ja-input'), function (input) {
        var ok = check(input);
        setError(input, !ok);
        if (!ok) bad.push(input);
      });
      if (!bad.length) { window.location.href = 'thank-you.html'; return; }
      alertBox.querySelector('.ja-form-alert__title').textContent = 'Check ' + bad.length + (bad.length === 1 ? ' field' : ' fields') + ' before sending';
      alertBox.querySelector('ul').innerHTML = bad.map(function (i) { return '<li><a href="#' + i.id + '">' + esc(i.dataset.error) + '</a></li>'; }).join('');
      alertBox.hidden = false;
      alertBox.focus();
    });
    form.addEventListener('input', function (e) {
      if (submitted && e.target.classList.contains('ja-input') && check(e.target)) setError(e.target, false);
    });
    alertBox.addEventListener('click', function (e) {
      var a = e.target.closest('a');
      if (!a) return;
      e.preventDefault();
      var t = document.querySelector(a.getAttribute('href'));
      if (t) { t.focus(); t.scrollIntoView({ block: 'center' }); }
    });
  }

  /* ---------- Placeholder links (share, social, downloads not supplied yet) ---------- */
  function initPending() {
    var toast;
    document.addEventListener('click', function (e) {
      var a = e.target.closest('[data-ja-pending]');
      if (!a) return;
      e.preventDefault();
      if (!toast) {
        toast = document.createElement('div');
        toast.className = 'ja-toast';
        toast.setAttribute('role', 'status');
        document.body.appendChild(toast);
      }
      toast.textContent = a.getAttribute('data-ja-pending') + ' isn’t connected in this review build yet.';
      toast.classList.add('is-on');
      clearTimeout(toast._t);
      toast._t = setTimeout(function () { toast.classList.remove('is-on'); }, 3200);
    });
  }

  /* ---------- External links open in a new tab ---------- */
  function initExternal() {
    Array.prototype.forEach.call(document.querySelectorAll('a[href^="http"]'), function (a) {
      if (a.hostname === location.hostname) return;
      a.target = '_blank';
      a.rel = 'noopener';
    });
  }

  function init() { initLibrary(); initContact(); initPending(); initExternal(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
