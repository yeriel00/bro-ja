# Just Ask. — fluid layout refactor (developer notes)

Nov 20, 2026 · Jerry Cavill · **Complete — ships as part of the interior pages release** (`handoffs/2026-11-20-interior-pages-release.md`), together with the homepage updates and interior components there. Note: `--ja-section` is now 48 → 80 (was 24 → 80 in the table below).

## Overview

The site is moving from three breakpoint-driven layouts (mobile < 768, tablet 768–1023, desktop ≥ 1024) to fluid layouts that adapt continuously from 375 to 1440. The 375 / 768 / 1440 designs are now guideline checks, not breakpoints. Media queries stay only where something breaks and has to be forced at a width (today: the header nav, full links from 1024). Rules: README → Responsive behavior.

| Part | Status | Files |
| --- | --- | --- |
| Foundations: fluid type, gutters, section padding | Done (Nov 20) | `components/bundle.css`, `tokens.json` → `tokens.css` |
| Hero, IntroMedia, References | Done (Nov 20) | `components/Hero/style.css`, `components/IntroMedia/style.css`, `components/References/style.css` |
| SiteHeader, SiteFooter, StatisticGrid, ClinicalQuestion, QuoteBand, CtaBand, PartnerAttribution, TreatmentEvidence | Done (Nov 20) | each `components/<Block>/style.css` |
| Button, ActionLink, ResourceCard | No change (no media queries) | — |

## Foundations (done)

Replace `components/bundle.css` and regenerate or replace `tokens.css`.

- **Type:** the display and heading classes (`ja-display`, `ja-h1`–`ja-h3`, `ja-question`, `ja-statement`, `ja-evidence-qualifier`, `ja-statistic`, `ja-quotation`, `ja-cta-text`, `ja-hero-*`) now size from `clamp()` variables (`--ja-<style>-size`, `--ja-<style>-lh`), in rem. `ja-body`, `ja-small`, `ja-label`, links and endnotes are unchanged.
- **Layout variables:** `--ja-margin` (24 → 80), `--ja-gap` (16 → 24) and `--ja-section` (24 → 80) are fluid. `--ja-content` is always 1280 and `--ja-prose` always 720; the container is 100% wide below that. `--ja-cols` is removed (unused).
- **No media queries** remain in `bundle.css`.
- **Class names and markup:** unchanged. No ACF change.

## Hero (done)

Replace `components/Hero/style.css`. No markup or ACF change.

- The text column is sized from the highlight type (`5.4em`, min 21rem), so "40 million" stays on one line at every width. Keep the `highlight` field to about 10 characters.
- Text inset, top padding, subtitle and rule spacing, and the face grid's pitch, top and left scale between the 375 and 1440 values. Min height 570.
- The veil keeps its two media queries (768, 1024): art direction only.

## IntroMedia (done)

Replace `components/IntroMedia/style.css`. No ACF change.

- **Keep the `ja-intro` class on the `<section>`:** it's the size container. The photo moves beside the text when the section is 896px (56rem) or wider, via `@container ja-intro`, not a viewport media query.
- Columns use `minmax(0, …)`. Without it, the photo's intrinsic width (1871px) pushed the page wider than the screen below 1440 and squeezed the text column to 287px at 1440. Check whether the live homepage shows that today.
- Photo height scales 220 → 410; column gap 40 → 80.

## References (done)

Replace `components/References/style.css`. No markup or ACF change. Padding follows the section padding up to 48; gaps 8 → 12. No media queries.

## Other blocks (done)

Replace each `style.css`. No markup or ACF change. Keep the classes the container queries use.

| Block | What changes | Container / media query |
| --- | --- | --- |
| SiteHeader | Bar 80 → 86 and logo 160 → 190 scale; menu padding 12 → 28 | Keeps `@media (min-width: 1024px)` for the nav switch (the only layout media query left) |
| SiteFooter | Padding and gaps scale; logo 190 everywhere | `container: ja-footer` on `.ja-footer`: link row from 40rem, copyright \| legal from 56rem, logo \| nav from 64rem |
| StatisticGrid | Intrinsic grid (320px min, max 3 columns; 2 for two or four stats or `ja-stats--cols-2`); spacing and pattern scale | `container: ja-stats` on `.ja-stats__grid` for the card floor height only |
| ClinicalQuestion | Panel padding and bracket inset scale | `container: ja-question` on the section: split from 64rem |
| QuoteBand | Photo height, overlap and card padding scale | `container: ja-quote` on the band: photo-behind layout from 64rem |
| CtaBand | Padding 48 → 96, gap 32 → 48 | Keeps one art-direction media query (pattern size, edge fade at 1024) |
| PartnerAttribution | Logo size, gaps and margins scale | None |
| TreatmentEvidence | Gaps, bracket arms and inset scale | `container: ja-treatment` on the section: split from 64rem |

## Testing checklist (run when the whole release is ready)

- [ ] 375, 390, 768, 1024, 1280 and 1440: no horizontal scroll; nothing clipped.
- [ ] Drag the window from 1440 down to 375: no jumps in type or spacing except at the header nav (1024); split blocks change layout once each (IntroMedia ~896, the others ~1024), when their columns would get too tight.
- [ ] At 1440 every block measures the same as before this release.
- [ ] Above 1440 nothing grows.
- [ ] Browser font size set to 20px: headings scale up with it; no overlap.
- [ ] Zoom to 200%: content reflows, no horizontal scroll at 1280 (WCAG 1.4.10).
