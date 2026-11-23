# Just Ask. — client review site

Static build of the Just Ask. campaign site (American Headache Society) for client approval.
Plain HTML/CSS/JS — no framework, no build step needed on the host.

## Pages (URLs follow the content outline's sitemap)
| URL | Page |
|---|---|
| `/` | 0.0 Home |
| `/why-ask/` | 1.0 Why Ask |
| `/the-ask/` | 2.0 The Ask |
| `/after-the-yes/` | 3.0 After the Yes (header dropdown lists the three steps) |
| `/after-the-yes/diagnosing-migraine/` | 3.1 Diagnosing Migraine |
| `/after-the-yes/treating-migraine/` | 3.2 Treating Migraine |
| `/after-the-yes/ongoing-migraine-care/` | 3.3 Ongoing Care |
| `/resources/` | 3.4 Resource Library (filters; supports `?step=`, `?group=`, `?format=`) |
| `/contact/` → `/contact/thank-you/` | 4.0 Contact (validates, then goes to Thank You; nothing is sent) |
| `/terms/`, `/privacy/` | 5.1 / 5.2 Legal |
| `/404.html` | Error page (Cloudflare Pages serves it automatically) |

`_redirects` sends the first review build's URLs (`/the-movement.html`, `/patient-resources.html`, …) to the new ones.
Links use root paths, so preview locally with a server, not by double-clicking a file:
`python3 -m http.server 8000` then open http://localhost:8000.

## Deploy on Cloudflare Pages
1. Cloudflare dashboard → Workers & Pages → Create → Pages → Connect to Git → pick this repo.
2. Framework preset: **None**. Build command: *(leave empty)*. Build output directory: **`/`**.
3. Save and Deploy. Every push to `main` redeploys.

`_headers` sends `X-Robots-Tag: noindex` so the review site stays out of search engines.

## Editing
Page copy lives in `src/pages.py` (shared markup in `src/parts.py`, library data in `src/resources.py`,
review-only CSS/JS in `src/site.css` / `src/site.js`). After editing, rebuild from the repo root:

```
python3 src/build.py
```

The build reads the exported design system in `Just Ask/` (tokens, component CSS, fonts, images,
`bundle.js`), bundles all CSS into `assets/css/site.css`, copies images/fonts into `assets/`, and
rewrites the HTML files. Commit the generated files — the host serves them as-is.

## Review-build notes
- The shared clinician photo is a placeholder: it shows a pale-blue tint with **FPO** in primary blue.
- "Share With a Colleague", social icons and "Download the Menu" show a "not connected yet" notice.
- Partner logos and most citations are placeholders, as in the design.
