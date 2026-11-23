# Just Ask. — client review site

Static build of the Just Ask. campaign site (American Headache Society) for client approval.
Plain HTML/CSS/JS — no framework, no build step needed on the host.

## Pages
| File | Page |
|---|---|
| `index.html` | 0.0 Home |
| `the-movement.html` | 1.0 The Movement |
| `the-ask.html` | 2.0 The Ask |
| `after-the-yes.html` | 3.0 After the Yes |
| `diagnosing-migraine.html` | 3.1 Diagnosing Migraine |
| `treating-migraine.html` | 3.2 Treating Migraine |
| `ongoing-care.html` | 3.3 Ongoing Care |
| `patient-resources.html` | 3.4 Patient Resources |
| `resource-library.html` | 3.5 Resource Library (filters; supports `?step=`, `?group=`, `?format=`) |
| `contact.html` → `thank-you.html` | 4.0 Contact (validates, then goes to Thank You; nothing is sent) |
| `terms.html`, `privacy.html` | 5.1 / 5.2 Legal |
| `404.html` | Error page (Cloudflare Pages serves it automatically) |

## Deploy on Cloudflare Pages
1. Cloudflare dashboard → Workers & Pages → Create → Pages → Connect to Git → pick this repo.
2. Framework preset: **None**. Build command: *(leave empty)*. Build output directory: **`/`**.
3. Save and Deploy. Every push to `main` redeploys.

`_headers` sends `X-Robots-Tag: noindex` so the review site stays out of search engines.
Cloudflare serves `/the-ask.html` at `/the-ask` too.

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
