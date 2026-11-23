"""Shared markup helpers. Markup follows the Just Ask. design system components."""

ARROW = '<svg class="ja-arrow" viewBox="0 0 13 24" aria-hidden="true"><path d="M0 11h9.17L5.6 7.41 6.99 6 13 12l-6.01 6-1.39-1.41L9.17 13H0z"></path></svg>'
Q = "In the past month, has a headache interfered with your work, school, family, or other activities?"
Q_HL = "In the past month, has a headache interfered with your <span class=\"ja-hl\">work, school, family, or other activities?</span>"
PHOTO = "assets/img/consultation.webp"

NAV = [
    ("movement", "the-movement.html", "The Movement"),
    ("ask", "the-ask.html", "The Ask"),
    ("aty", "after-the-yes.html", "After the Yes"),
    ("patients", "patient-resources.html", "Patient Resources"),
]
FOOTER_NAV = NAV + [("library", "resource-library.html", "Resource Library"), ("contact", "contact.html", "Contact")]


def sup(n):
    return f'<sup class="ja-sup"><a href="#ref-{n}" aria-label="Reference {n}">{n}</a></sup>'


def nowrap_last(text):
    """Keep the last word with the arrow so the arrow never wraps alone."""
    words = text.rsplit(" ", 1)
    if len(words) == 1:
        return f'<span class="ja-nowrap">{text} {ARROW}</span>'
    return f'{words[0]} <span class="ja-nowrap">{words[1]} {ARROW}</span>'


def link(text, href, cls="ja-link", extra=""):
    return f'<a class="{cls}" href="{href}"{extra}>{nowrap_last(text)}</a>'


def button(text, href, cls="ja-button", extra=""):
    return f'<a class="{cls}" href="{href}"{extra}>{text}</a>'


def fpo(img_html, cls=""):
    """Wrap the shared placeholder photo in the FPO tint layer."""
    return f'<div class="ja-fpo {cls}">{img_html}<span class="ja-fpo__label" aria-hidden="true">FPO</span></div>'


def header(active=None):
    def items(mobile=False):
        out = []
        for key, href, label in NAV:
            cur = ' aria-current="page"' if key == active else ""
            out.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
        return "".join(out)
    return f'''<header class="ja-header">
  <div class="ja-container ja-header__bar">
    <a class="ja-header__logo" href="index.html"><img src="assets/img/logos/just-ask-full-color.svg" alt="Just Ask." width="190" height="38"></a>
    <nav class="ja-nav ja-label" aria-label="Primary"><ul class="ja-nav__list">{items()}</ul></nav>
    <button class="ja-menu-toggle ja-label" type="button" aria-expanded="false" aria-controls="ja-mobile-nav"><span class="ja-menu-label">Menu</span><svg class="ja-burger" viewBox="0 0 18 14" aria-hidden="true"><path d="M0 1h18M0 7h18M0 13h18"/></svg><svg class="ja-x" viewBox="0 0 18 14" aria-hidden="true"><path d="M3 0l12 14M15 0L3 14"/></svg></button>
  </div>
  <nav class="ja-mobile-nav ja-label" id="ja-mobile-nav" aria-label="Primary"><ul class="ja-container">{items(True)}</ul></nav>
</header>'''


def footer():
    items = "".join(f'<li><a href="{h}">{l}</a></li>' for _, h, l in FOOTER_NAV)
    return f'''<footer class="ja-footer">
  <div class="ja-container">
    <div class="ja-footer__top">
      <a class="ja-footer__logo" href="index.html"><img src="assets/img/logos/just-ask-full-color.svg" alt="Just Ask." width="190" height="38" loading="lazy"></a>
      <nav class="ja-footer__nav ja-label" aria-label="Footer"><ul>{items}<li><a href="https://americanheadachesociety.org/">Visit American Headache Society</a></li></ul></nav>
    </div>
    <div class="ja-footer__bottom ja-small">
      <p style="margin:0">© 2026 American Headache Society</p>
      <ul class="ja-footer__legal"><li><a href="privacy.html">Privacy Policy</a></li><li><a href="terms.html">Terms</a></li></ul>
    </div>
  </div>
</footer>'''


# ---------- sections ----------

def page_hero(eyebrow, title, intro, variant="", media=None, extra="", eyebrow_href=None):
    eb = ""
    if eyebrow:
        eb_inner = eyebrow if not eyebrow_href else eyebrow.replace(eyebrow_href[0], f'<a href="{eyebrow_href[1]}">{eyebrow_href[0]}</a>', 1)
        eb = f'<span class="ja-label ja-page-hero__eyebrow">{eb_inner}</span>'
    intro_html = f'<p class="ja-body ja-page-hero__intro">{intro}</p>' if intro else ""
    text = f'{eb}<h1 class="ja-h1">{title}</h1>{intro_html}{extra}'
    cls = "ja-page-hero" + (f" ja-page-hero--{variant}" if variant else "")
    if media:
        inner = f'<div class="ja-page-hero__grid"><div>{text}</div>{media}</div>'
    else:
        inner = text
    return f'<header class="{cls}"><span class="ja-pattern ja-page-hero__pattern" aria-hidden="true"></span><div class="ja-container">{inner}</div></header>'


def hero_photo():
    return fpo(f'<img class="ja-page-hero__img" src="{PHOTO}" alt="A clinician listens to a patient during an appointment" width="1871" height="840">', "ja-fpo--hero")


def step_nav(current):
    steps = [("diagnosing-migraine.html", "Step 1", "Diagnosing migraine"), ("treating-migraine.html", "Step 2", "Treating migraine"), ("ongoing-care.html", "Step 3", "Ongoing care")]
    cur = ' aria-current="page"'
    lis = "".join(
        f'<li><a href="{h}"{cur if i == current else ""}><span class="ja-step-nav__num">{n}</span><span class="ja-step-nav__name">{t}</span></a></li>'
        for i, (h, n, t) in enumerate(steps, 1))
    return f'<nav class="ja-step-nav" aria-label="After the Yes steps"><div class="ja-container"><ol>{lis}</ol></div></nav>'


def rule_h2(title, id_=None):
    i = f' id="{id_}"' if id_ else ""
    return f'<span class="ja-rule" aria-hidden="true"></span><h2 class="ja-h2"{i}>{title}</h2>'


def stat(value, label):
    long_ = " ja-stat__value--long" if len(value) > 7 else ""
    return f'<li class="ja-stat"><span class="ja-stat__value ja-statistic{long_}">{value}</span><span class="ja-stat__rule" aria-hidden="true"></span><p class="ja-stat__label ja-body">{label}</p></li>'


def info_card(title, body, footer_html="", inverse=False, inner=""):
    cls = "ja-info-card" + (" ja-info-card--inverse" if inverse else "")
    b = f'<p class="ja-body ja-info-card__text">{body}</p>' if body else ""
    f = f'<div class="ja-info-card__footer">{footer_html}</div>' if footer_html else ""
    return f'<li><article class="{cls}"><h3 class="ja-h3">{title}</h3>{b}{inner}{f}</article></li>'


def reslinks(*items):
    """items: (title, href, meta_label_or_None, meta_cls_or_None)"""
    lis = []
    for it in items:
        title, href = it[0], it[1]
        meta = it[2] if len(it) > 2 else None
        mcls = it[3] if len(it) > 3 else None
        m = f'<span class="ja-reslink__meta ja-reslink__meta--{mcls}">{meta}</span>' if meta else ""
        lis.append(f'<li><a class="ja-reslink" href="{href}"><span class="ja-reslink__title">{title}</span>{m}{ARROW}</a></li>')
    return f'<ul class="ja-reslinks">{"".join(lis)}</ul>'


ACTION = {"Quick Guide": "View Guide", "Guideline": "Read Guideline", "Tool": "Open Tool", "Article": "Read Article", "Video": "Watch Video", "Podcast": "Listen"}


def resource(fmt, title, text, href, action=None, group=None, style=""):
    slug = fmt.lower().replace(" ", "-")
    g = f'<li class="ja-tag">{group}</li>' if group else ""
    st = f' style="{style}"' if style else ""
    act = action or ACTION.get(fmt, "Open")
    t = f'<p class="ja-body ja-resource__text">{text}</p>' if text else ""
    return (f'<article class="ja-resource"{st}><ul class="ja-tags" aria-label="Labels"><li class="ja-tag ja-tag--format ja-tag--{slug}">{fmt}</li>{g}</ul>'
            f'<h3 class="ja-h3 ja-resource__title">{title}</h3>{t}'
            f'<a class="ja-button ja-button--outline ja-resource__action" href="{href}">{act}<span class="ja-visually-hidden">: {title}</span></a></article>')


def callout(title, body, extra=""):
    return f'<div class="ja-callout"><h3 class="ja-h3">{title}</h3><p class="ja-body ja-callout__text">{body}</p>{extra}</div>'


def pullquote(text, cite, n, variant="compact", style=""):
    st = f' style="{style}"' if style else ""
    if variant == "finding":
        q = f'<p class="ja-evidence-qualifier">{text}</p>'
    else:
        q = f'<p class="ja-body" style="font-weight: 700">{text}</p>'
    return (f'<figure class="ja-pullquote ja-pullquote--{variant}"{st}><span class="ja-pullquote__mark" aria-hidden="true">“</span>'
            f'<blockquote style="margin: 0">{q}</blockquote><figcaption class="ja-pullquote__cite">— {cite}{sup(n)}</figcaption></figure>')


def quote_band(text, cite, n, white=True):
    cls = "ja-quote ja-quote--white" if white else "ja-quote"
    return f'''<section class="{cls}" aria-label="Clinician quote">
  <div class="ja-quote__photo ja-fpo ja-fpo--band"><img src="{PHOTO}" alt="" width="1871" height="840" loading="lazy"><span class="ja-fpo__label" aria-hidden="true">FPO</span></div>
  <div class="ja-quote__inner"><figure class="ja-quote__card"><div class="ja-quote__body">
    <span class="ja-quote__mark" aria-hidden="true"><span>“</span></span>
    <blockquote class="ja-quote__text ja-quotation">{text}</blockquote>
    <figcaption class="ja-quote__cite ja-label">— {cite}{sup(n)}</figcaption>
  </div></figure></div>
</section>'''


def share_link():
    return ('<a class="ja-link ja-link--inverse ja-link--strong" href="#share" data-ja-pending="Share With a Colleague">'
            f'Share With a <span class="ja-nowrap">Colleague {ARROW}</span></a>')


def cta_band(hl, rest, body=None, buttons="", share=True, question=False, id_="cta-title"):
    b = f'<p class="ja-cta__body ja-body">{body}</p>' if body else ""
    q = f'<p class="ja-cta__question ja-question">“{Q}”</p>' if question else ""
    s = share_link() if share else ""
    status = '<p class="ja-copy-status ja-visually-hidden" role="status"></p>' if question else ""
    return f'''<section class="ja-cta ja-on-inverse" aria-labelledby="{id_}">
  <span class="ja-pattern ja-pattern--l" aria-hidden="true"></span><span class="ja-pattern ja-pattern--r" aria-hidden="true"></span>
  <div class="ja-container"><div class="ja-cta__content">
    <h2 class="ja-cta__text ja-cta-text" id="{id_}"><span class="ja-hl--sky">{hl}</span> {rest}</h2>
    {q}{b}
    <div class="ja-cta__actions"><div class="ja-cta__buttons">{buttons}</div>{s}</div>
  </div>{status}</div>
</section>'''


def copy_button(cls="ja-button"):
    return f'<button class="{cls}" type="button" data-ja-copy data-ja-copy-text="{Q}" hidden><span class="ja-copy-label">Copy the Question</span></button>'


def references(items, note="Working references — final citations and claim wording pending client review."):
    lis = "".join(f'<li id="ref-{i}">{t}</li>' for i, t in enumerate(items, 1))
    return f'<section class="ja-refs" aria-labelledby="refs-title"><div class="ja-container"><h2 class="ja-h2" id="refs-title">References</h2><p class="ja-refs__note ja-small">{note}</p><ol class="ja-refs__list ja-small">{lis}</ol></div></section>'


def pending(n):
    return ["Citation pending."] * n


def partners_logos():
    lis = "".join(f'<li class="ja-partner"><span class="ja-partner__placeholder ja-small">Logo {i}</span></li>' for i in range(1, 8))
    return f'<ul class="ja-partners__logos" aria-label="Partner organizations">{lis}</ul>'


def page_nav(back=None, nxt=None, library=True):
    """back/nxt: (href, kicker, title)"""
    b = ""
    if back:
        b = (f'<a class="ja-pagenav__next ja-pagenav__prev" href="{back[0]}">{ARROW}<span><span class="ja-pagenav__kicker">{back[1]}</span>'
             f'<span class="ja-h3 ja-pagenav__title">{back[2]}</span></span></a>')
    n = ""
    if nxt:
        n = (f'<a class="ja-pagenav__next" href="{nxt[0]}"><span><span class="ja-pagenav__kicker">{nxt[1]}</span>'
             f'<span class="ja-h3 ja-pagenav__title">{nxt[2]}</span></span>{ARROW}</a>')
    lib = f'<a class="ja-link ja-pagenav__library" href="resource-library.html">See All <span class="ja-nowrap">Resources {ARROW}</span></a>' if library else ""
    return f'<section class="ja-section"><div class="ja-container"><nav class="ja-pagenav" aria-label="Page">{b}<div class="ja-pagenav__group">{n}{lib}</div></nav></div></section>'
