# System map

Read this first. To change one component, open only its folder plus the foundation files it lists.

## Files

| File | Holds | Load |
|---|---|---|
| `tokens.json` → `tokens.css` | Every color, type style, space, radius, stroke, layout and breakpoint value | Every page |
| `components/bundle.css` | **Foundations:** fluid variables (`clamp()`, 375 → 1440), base, fluid type classes (`ja-h2`…), endnote `ja-sup`, arrow `ja-arrow`, shared pieces (`ja-rule`, `ja-hl`, `ja-prose`, `ja-pattern`); interior foundations (Nov 20): `ja-content` container queries, `.ja-section--tint`, `.ja-interior` same-ground spacing, `ja-minirule`, `ja-nowrap`, the 13 × 24 direction arrow | Every page |
| `components/bundle.js` | `JustAsk.initFaceGrid` (hero grid), `JustAsk.initHeader` (mobile menu) and `JustAsk.initCopy` (ClinicalQuestion and CtaBand copy buttons) | Deferred, every page |
| `components/<Component>/style.css` | That component's CSS only | Where the block is used |
| `components/<Component>/preview.html` | The reference markup, shown on this page | — |
| `components/<Component>/README.md` | Specs, spacing, ACF fields, do/don't | — |
| `README.md` | Brand rules: color, type, imagery, motion, content | — |
| `CHANGELOG.md` | **Required** record of every change, including what the developer must do | — |
| `handoffs/YYYY-MM-DD-*.md` | Notes to the developer: what to change on the live site, gathered from the CHANGELOG, with a testing checklist | — |

In WordPress, enqueue `tokens.css`, `bundle.css` and `bundle.js` globally. Each ACF block enqueues its own `style.css` plus the ones it depends on.

## Working copy

A full copy of these files lives on Jerry's Mac at `Desktop/Brolik/ahs-emp/design-system/`, with the same paths as here (`tokens.json`, `components/…`, `assets/…`, `fonts/`). Edit there, then publish the changed files back to this design system so the two stay identical. Previews reference uploaded images by `/_blob/…` address, so in the local copy they show without images; the image files themselves are in `assets/`.

## Components

| Component | Group | Depends on | Notes |
|---|---|---|---|
| Button | Pieces | — | Primary button, 160 × 56 minimum; secondary (inverse) modifier for the CTA band |
| ActionLink | Pieces | — | Underlined link + arrow; `--on-soft`, `--inverse`, `--strong`, `--label` |
| ResourceCard | Pieces | ActionLink, Button (outline action) | After the Yes card; format + patient-group tags (Resource Library); bilingual EN / ES download links (Resource Library) |
| SiteHeader | Chrome | `bundle.js` | Full nav from 1024px; Menu below |
| SiteFooter | Chrome | — | Container query on the footer (`ja-footer`) |
| References | Chrome | — | Targets for every `ja-sup` link (`#ref-N`) |
| Hero | Sections | `bundle.js` | Face grid; hero-only type styles |
| IntroMedia | Sections | ActionLink | Photo + optional rule and eyebrow, H2 or H1, optional body and link; container query on the section (`ja-intro`) |
| ClinicalQuestion | Sections | ActionLink; `bundle.js` with the copy action; StatisticGrid with the optional stat | Bracketed question panel; optional Copy the Question text action inside the panel; container query on the section (`ja-question`) |
| StatisticGrid | Sections | PullQuote with findings rows | Intrinsic grid, 320px min columns, max 3 (2 for two or four stats) |
| QuoteBand | Sections | — | Photo band + quote card; container query on the band (`ja-quote`) |
| TreatmentEvidence | Sections | ActionLink | Text + evidence bracket; container query on the section (`ja-treatment`) |
| PartnerAttribution | Sections | ActionLink | Stacked intro + one row of partner logos |
| CtaBand | Sections | Button, ActionLink; `bundle.js` with the copy button | Navy band, top-view brain on each edge with an edge-to-centre fade; optional question, body, secondary button, share link, copy mode |
| PageHero | Interior | PullQuote (hero quote) | Simple / Media / Question / Step; brain pattern (in review) |
| StepNav | Interior | — | Stepper after the PageHero on step pages; steps from an options repeater (in review) |
| TextSection | Interior | Button, ActionLink, Callout, PullQuote, ListBlock, ResourceLink, ResourceCard, CardGrid, DataBars (per option) | Basic / Split / Aside; tint option (in review) |
| CardGrid | Interior | Button, ResourceLink, Callout, PullQuote, ListBlock, ResourceCard (per option) | InfoCards, max 2 / 3 / 4 columns; inverse card; closing pair (in review) |
| StepCards | Interior | — | Three linked step cards (in review) |
| FeaturedResource | Interior | Button, ResourceCard | One highlighted Library item (in review) |
| Timeline | Interior | — | Checkpoint cards with chevrons (in review) |
| PageNav | Interior | ActionLink | Back / next / Library link on step pages (in review) |
| ResourceLibrary | Interior | ResourceCard, Button | Filters, grouped results, empty state (in review) |
| ContactForm | Interior | Button | Fields, validation, social icons, brain pattern (in review) |
| RichText | Interior | — | Legal pages and WYSIWYG copy (in review) |
| Callout | Pieces | ActionLink (optional) | Closed-bracket tip (in review) |
| PullQuote | Pieces | — | Compact and finding variants (in review) |
| ResourceLink | Pieces | — | Resource row; card-footer form (in review) |
| ListBlock | Pieces | — | Numbered, check, bullet, columns, list panel (in review) |
| DataBars | Pieces | — | Proportional bars (in review) |
| HomePage | Pages | all of the above | Assembled example, checked against the frames |

## How to change things

- **Every change needs a `CHANGELOG.md` entry** in the same publish, using its template. Say what the developer must do ("Developer action").
- **A value used everywhere** (a color, a size, spacing): edit `tokens.json`.
- **One component's look:** edit `components/<Component>/style.css`, then update its preview and README if the markup or specs change.
- **A new component:** add a new folder with `style.css`, `preview.html` and `README.md`, add a row to the table above, and build only from tokens and foundation classes.

## Status and open items

- **Fluid refactor (started Nov 20):** foundations are fluid (`bundle.css`). All 14 components are refactored (Nov 20). Media queries left: SiteHeader nav at 1024 (layout), Hero veil and CtaBand pattern (art direction), plus `prefers-reduced-motion`. Each component README has a Responsive behavior note.

- **Built so far:** the homepage set, measured against the 1440 / 768 / 375 homepage frames.
- **Interior components (Nov 20):** the 16 interior components from the interior-page canvas are in the system, marked "in review" until Jerry signs off the interior pages. The canvas loads this system's CSS, so the two stay in step. Figma is retired; the canvas is the reference for interior pages.
- **The live homepage's ACF fields differ** from the fields listed in these READMEs. Update the READMEs to match the developer's field groups.
