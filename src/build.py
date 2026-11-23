#!/usr/bin/env python3
"""Just Ask. review site — static build.

Usage (from the repo root):  python3 src/build.py ["Just Ask"]

Reads the exported design system folder ("Just Ask/" by default), copies its fonts and
images into /assets, concatenates every component stylesheet into assets/css/site.css,
and writes one HTML file per page at the repo root. No dependencies beyond Python 3.
Cloudflare Pages: no build command, output directory = / (repo root).
"""
import os, re, shutil, sys, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DS = os.path.join(ROOT, sys.argv[1] if len(sys.argv) > 1 else "Just Ask")
SRC = os.path.join(ROOT, "src")
ASSETS = os.path.join(ROOT, "assets")

from pages import PAGES  # noqa: E402  (src/pages.py)
from parts import header, footer  # noqa: E402


def build_assets():
    for sub in ("css", "js", "fonts", "img/portraits", "img/logos"):
        os.makedirs(os.path.join(ASSETS, sub), exist_ok=True)
    # fonts
    for f in os.listdir(os.path.join(DS, "fonts")):
        shutil.copy2(os.path.join(DS, "fonts", f), os.path.join(ASSETS, "fonts", f))
    # images
    a = os.path.join(DS, "assets")
    for f in os.listdir(os.path.join(a, "Portraits")):
        if f.endswith(".webp"):
            shutil.copy2(os.path.join(a, "Portraits", f), os.path.join(ASSETS, "img/portraits", f))
    for f in os.listdir(os.path.join(a, "Logos")):
        if f.endswith(".svg"):
            shutil.copy2(os.path.join(a, "Logos", f), os.path.join(ASSETS, "img/logos", f))
    shutil.copy2(os.path.join(a, "Patterns", "brain-illustration-top.svg"), os.path.join(ASSETS, "img", "pattern-brain.svg"))
    shutil.copy2(os.path.join(a, "Photography", "consultation-clinician-patient.webp"), os.path.join(ASSETS, "img", "consultation.webp"))
    shutil.copy2(os.path.join(a, "Hero", "hero-face-grid.webp"), os.path.join(ASSETS, "img", "hero-face-grid.webp"))
    # js
    shutil.copy2(os.path.join(DS, "components", "bundle.js"), os.path.join(ASSETS, "js", "bundle.js"))
    shutil.copy2(os.path.join(SRC, "site.js"), os.path.join(ASSETS, "js", "site.js"))
    # css: tokens -> foundations -> every component -> site overrides
    parts = []
    tok = open(os.path.join(DS, "tokens.css"), encoding="utf-8").read()
    tok = tok.replace('url("fonts/', 'url("../fonts/')
    parts.append("/* ===== tokens.css ===== */\n" + tok)
    parts.append("/* ===== components/bundle.css ===== */\n" + open(os.path.join(DS, "components", "bundle.css"), encoding="utf-8").read())
    comp_dir = os.path.join(DS, "components")
    order = ["Button", "ActionLink"]  # pieces others depend on first
    rest = sorted(d for d in os.listdir(comp_dir) if os.path.isfile(os.path.join(comp_dir, d, "style.css")) and d not in order)
    for name in order + rest:
        css = open(os.path.join(comp_dir, name, "style.css"), encoding="utf-8").read()
        parts.append(f"/* ===== components/{name}/style.css ===== */\n" + css)
    parts.append("/* ===== src/site.css (review build) ===== */\n" + open(os.path.join(SRC, "site.css"), encoding="utf-8").read())
    open(os.path.join(ASSETS, "css", "site.css"), "w", encoding="utf-8").write("\n\n".join(parts))


def page_html(p):
    robots = '\n<meta name="robots" content="noindex">' if p.get("noindex") else ""
    desc = html.escape(p.get("desc", ""), quote=True)
    title = html.escape(p["title"], quote=False)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">{robots}
<link rel="icon" href="/assets/img/logos/just-ask-blue.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/Montserrat-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css">
<script src="/assets/js/bundle.js" defer></script>
<script src="/assets/js/site.js" defer></script>
</head>
<body>
<div class="ja-root">
<a class="ja-skip" href="#main">Skip to content</a>
{header(p["key"])}
{p["body"]()}
{footer()}
</div>
</body>
</html>
"""


def main():
    build_assets()
    for p in PAGES:
        out = os.path.join(ROOT, p["path"])
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(page_html(p))
        print("wrote", p["path"])
    # Pages from the first review build that moved (see _redirects); remove them if this machine allows it.
    for old in ("the-movement.html", "the-ask.html", "after-the-yes.html", "diagnosing-migraine.html", "treating-migraine.html",
                "ongoing-care.html", "patient-resources.html", "resource-library.html", "contact.html", "thank-you.html",
                "terms.html", "privacy.html"):
        f = os.path.join(ROOT, old)
        if os.path.exists(f):
            try:
                os.remove(f)
                print("removed", old)
            except OSError:
                print("could not remove", old, "- delete it by hand (git rm)")


if __name__ == "__main__":
    sys.path.insert(0, SRC)
    main()
