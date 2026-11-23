# Changelog

**Required.** Every change to this design system gets an entry here *in the same publish* as the change. A change without an entry isn't done. Newest first.

## How to fill it out

Copy the template and fill every field. Write "—" if a field doesn't apply, never leave one blank.

```
### YYYY-MM-DD — Short title
- **By:** name (via tool, if any)
- **Components:** code names (e.g. CtaBand, ActionLink) or Foundations / Tokens / Assets / Docs
- **Type:** New component | Update to existing | Foundations | Tokens | Assets | Docs
- **Developer action:** None | Ship new component | Update live block — say what
- **What changed:** one or two plain sentences
- **Why:** the request or reason
- **Files:** paths changed
- **Verified:** how it was checked (frames + widths, contrast, visual check)
```

Rules:

- **Developer action** is the field that matters most. Any change to an *existing* component that's already live must say "Update live block" and describe it, or the live site drifts from the system.
- Use code names, not Figma names (see `system-map.md`).
- Update `system-map.md` in the same publish when you add a component or change its dependencies.

---

### 2026-11-20 — Homepage sample copy from the new content outline
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** HomePage, IntroMedia, ClinicalQuestion, StatisticGrid, TreatmentEvidence, PartnerAttribution (Docs)
- **Type:** Docs
- **Developer action:** Update live content — homepage headings and body copy per the content model (IntroMedia "Better migraine care starts with asking", ClinicalQuestion "One question that fits into every visit", StatisticGrid, TreatmentEvidence and PartnerAttribution "Developed with clinicians who see patients every day" bodies). ACF content only; no CSS or markup change. Hero and CtaBand copy unchanged.
- **What changed:** Preview sample copy, the README voice examples and the release note's Library slug (`/resources/`) match the Nov 20 content outline.
- **Why:** New content outline (Nov 20) rewrites the homepage copy.
- **Files:** components/{HomePage,IntroMedia,ClinicalQuestion,StatisticGrid,TreatmentEvidence,PartnerAttribution}/preview.html; IntroMedia/README.md; PartnerAttribution/README.md; README.md; handoffs/2026-11-20-interior-pages-release.md; design-system.json (lastChange)
- **Verified:** Text-only replacements, each matched once per file; previews checked for leftover old headings.

### 2026-11-20 — "The Movement" renamed "Why Ask"; preview copy synced to the new content outline
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** SiteHeader, SiteFooter, HomePage, PartnerAttribution, CtaBand, CardGrid, PageHero, IntroMedia, StatisticGrid, ClinicalQuestion, QuoteBand, TextSection, Timeline (Docs)
- **Type:** Docs
- **Developer action:** Update live content — rename the nav item "The Movement" to "Why Ask" (slug `/why-ask/`), Resource Library slug `/resources/`, and the homepage partner link to "Why Ask About Migraine". No CSS or markup change.
- **What changed:** Preview sample text, nav labels/links and "used on" notes now say Why Ask; interior-page sample copy matches the new content outline (Nov 20), incl. the stat label "as common in women."
- **Why:** New content outline: 1.0 The Movement is now 1.0 Why Ask, with revised headings and copy.
- **Files:** components/*/preview.html and README.md for the components above; design-system.json (lastChange)
- **Verified:** Text-only search and replace; no "Movement" left in previews or READMEs (CHANGELOG and handoff history unchanged).

### 2026-11-20 — Previews: more space between variants
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** PageHero, TextSection, CardGrid, PageNav, ResourceLibrary, ListBlock, ResourceLink, Callout, PullQuote; then CtaBand, StatisticGrid, ClinicalQuestion, IntroMedia, PartnerAttribution (previews only)
- **Type:** Docs
- **Developer action:** None (preview files only; no CSS or markup change)
- **What changed:** Each variant in a multi-variant preview now has a small muted label and a 1px sky rule with 48–64px above it, so variants no longer run into each other. Side-by-side variants (Callout, PullQuote) have wider gaps. Card heights updated.
- **Why:** Jerry (Nov 20): more space between component variants in the design system.
- **Files:** `components/{PageHero,TextSection,CardGrid,PageNav,ResourceLibrary,ListBlock,ResourceLink,Callout,PullQuote,CtaBand,StatisticGrid,ClinicalQuestion,IntroMedia,PartnerAttribution}/preview.html`, `CHANGELOG.md`
- **Verified:** Previews rendered at 375 and 1440, no horizontal overflow.

### 2026-11-20 — Interior-page components added (in review)
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** PageHero, StepNav, TextSection, CardGrid, StepCards, FeaturedResource, Timeline, PageNav, ContactForm, RichText, ResourceLibrary, Callout, PullQuote, ResourceLink, ListBlock, DataBars; Foundations; Docs
- **Type:** New component
- **Developer action:** Ship new components — build each as an ACF layout from its README (fields, responsive behavior) and `style.css`; ResourceLibrary is a page template on a Resource post type. Add `class="ja-interior"` to `<main>` on interior templates. Part of `handoffs/2026-11-20-interior-pages-release.md`.
- **What changed:** The interior-page components from the canvas review moved into the system, one folder each with `style.css`, `README.md` and `preview.html`, marked "in review" until the interior pages are signed off. `bundle.css` gains the interior foundations: `ja-content` container queries, `.ja-section--tint` (tinted section with gradient), `.ja-interior` same-ground spacing (interior pages only), `ja-minirule`, `ja-nowrap` and the 13 × 24 direction arrow.
- **Why:** Jerry (Nov 20): sync the design system with the reviewed interior pages so the developer gets one set of files and one release.
- **Files:** `components/{PageHero,StepNav,TextSection,CardGrid,StepCards,FeaturedResource,Timeline,PageNav,ContactForm,RichText,ResourceLibrary,Callout,PullQuote,ResourceLink,ListBlock,DataBars}/*`, `components/bundle.css`, `README.md`, `system-map.md`, `handoffs/2026-11-20-interior-pages-release.md`, `CHANGELOG.md`, `design-system.json`
- **Verified:** Every new preview rendered at 375 / 768 / 1440 with no horizontal overflow; TextSection, CardGrid, PageNav and ResourceLibrary checked visually against the canvas.

### 2026-11-20 — Homepage blocks: new options and lighter accents
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** Tokens, Foundations, Button, ResourceCard, ClinicalQuestion, StatisticGrid, QuoteBand
- **Type:** Update to existing
- **Developer action:** Update live blocks — regenerate `tokens.css`; replace `bundle.css` and the `style.css` of Button, ResourceCard, ClinicalQuestion, StatisticGrid and QuoteBand; swap ResourceCard's action link for the outline button; add the optional fields (ClinicalQuestion stat, StatisticGrid findings, QuoteBand card colour). Ship with the fluid release (`handoffs/2026-11-20-interior-pages-release.md`).
- **What changed:** `stroke-accent` 4 → 3px and `stroke-thin-accent` 3 → 2px (lighter accent rules, brackets and stat rules). `section-padding-mobile` 24 → 48px, so `--ja-section` is now 48 → 80. New tokens `text-link-on-tint` (#22679f) and `tag-quick-guide-text`. Button: long labels wrap; new outline variant. ResourceCard: outline-button action labelled by format. ClinicalQuestion: optional supporting stat and top alignment. StatisticGrid: optional findings rows. QuoteBand: white card option. All new options are off by default.
- **Why:** Review of the interior pages (Jerry, Nov 19–20): thinner accents, sections running into each other on phones, buttons for page CTAs, and options the interior pages need.
- **Files:** `tokens.json`, `components/bundle.css`, `components/{Button,ResourceCard,ClinicalQuestion,StatisticGrid,QuoteBand}/style.css`, their `README.md`, `components/Button/preview.html`, `components/ResourceCard/preview.html`, `README.md`, `handoffs/2026-11-20-fluid-layout.md`, `CHANGELOG.md`
- **Verified:** HomePage preview, before vs after: 1440 within 3px (5681 → 5678, thinner rules); 768 +118px and 375 +256px from the section padding, as intended; no horizontal overflow at any of the three.

### 2026-11-20 — Fluid refactor: all remaining components (step 2 complete)
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** SiteHeader, SiteFooter, StatisticGrid, ClinicalQuestion, QuoteBand, CtaBand, PartnerAttribution, TreatmentEvidence (CSS + README); Button, ActionLink, ResourceCard (README only); Docs
- **Type:** Update to existing
- **Developer action:** Update live blocks (SiteHeader, SiteFooter, StatisticGrid, ClinicalQuestion, QuoteBand, CtaBand, PartnerAttribution, TreatmentEvidence): replace each `style.css`. No markup or ACF change, but keep the section classes the container queries hang on (`ja-question`, `ja-quote`, `ja-treatment`, `ja-footer`, `ja-stats__grid`). The whole fluid release (foundations + all blocks) in `handoffs/2026-11-20-fluid-layout.md` can now ship together.
- **What changed:** Breakpoint layouts replaced with fluid values and intrinsic or container-query layouts. **StatisticGrid:** intrinsic grid (320px min columns, capped at 3, or 2 for two/four stats), even card floor height only when cards sit side by side, fluid spacing and pattern. **ClinicalQuestion, TreatmentEvidence, QuoteBand:** the split switches with a container query on the section at 64rem, `minmax(0, …)` columns, fluid padding, brackets and photo sizes. **SiteFooter:** container queries at 40 / 56 / 64rem; logo 190 at every width. **PartnerAttribution:** fluid spacing and logo size, no media queries. **CtaBand:** fluid padding and gap; one art-direction query (pattern size, edge fade). **SiteHeader:** fluid bar height, logo and menu padding; the 1024 nav switch is the only layout media query left in the system. Button, ActionLink, ResourceCard had none; READMEs say so. Every README has a Responsive behavior note.
- **Why:** Step 2 of the fluid layout refactor (Jerry, Nov 20).
- **Files:** `components/{SiteHeader,SiteFooter,StatisticGrid,ClinicalQuestion,QuoteBand,CtaBand,PartnerAttribution,TreatmentEvidence}/style.css`, those plus `components/{Button,ActionLink,ResourceCard}/README.md`, `README.md`, `system-map.md`, `handoffs/2026-11-20-fluid-layout.md`, `CHANGELOG.md`, `design-system.json`
- **Verified:** Every component preview and the HomePage, old vs new, at 375 / 600 / 768 / 900 / 1023 / 1024 / 1280 / 1440: identical heights at 1440 for every block (header 87, statistics 949 / 948 / 772, question 1142, quote 560, treatment 492, partners 700, CTA 1572, footer 216), identical at 375 except where the old layout capped the column; no horizontal overflow at any width. Visual check at 600 and 960.

### 2026-11-20 — Fluid refactor: Hero, IntroMedia, References
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** Hero, IntroMedia, References
- **Type:** Update to existing
- **Developer action:** Update live blocks (Hero, IntroMedia, References): replace each `style.css`. Part of the fluid release in `handoffs/2026-11-20-fluid-layout.md` (still "don't ship yet"). No ACF change. IntroMedia: the section must keep the `ja-intro` class (it's the container for the block's container query). Check the live homepage intro: if it has the same column bug, its text column is currently squeezed on desktop.
- **What changed:** **Hero:** text column is 5.4em of the highlight size (min 21rem), so "40 million" never wraps; text inset (0 → 92), top padding, subtitle/rule spacing and face-grid geometry scale with `clamp()`; min-height 570. Only the veil's art-direction media queries remain (decorative). **IntroMedia:** columns are `minmax(0, …)` (fixes the photo forcing horizontal scroll below 1440 and squeezing the text column to 287px at 1440); the side-by-side switch is a container query on the section (56rem) instead of the 1024 viewport query; photo height and column gap scale. No media queries. **References:** padding is `min(var(--ja-section), 48px)`; gaps 8 → 12 with `clamp()`. No media queries.
- **Why:** Fix the issues found when the foundations went fluid (hero number wrapping at 900–1023, IntroMedia overflow, References overriding the fluid padding), per Jerry's fluid layout rule.
- **Files:** `components/Hero/style.css`, `components/Hero/README.md`, `components/IntroMedia/style.css`, `components/IntroMedia/README.md`, `components/References/style.css`, `components/References/README.md`, `handoffs/2026-11-20-fluid-layout.md`, `system-map.md`, `CHANGELOG.md`, `design-system.json`
- **Verified:** HomePage preview, old vs new, at 375 / 390 / 600 / 768 / 880 / 900 / 1000 / 1023 / 1024 / 1280 / 1440 / 1600: no horizontal overflow at any width (old: 514px page at 375, 1260 at 1024); "40 million" on one line at every width; hero identical at 1440 and up (text at 172, 540 wide, 634 tall). Hero text sits on ≥ 0.8 white veil everywhere (lowest at 768: ~0.82 at the line ends). IntroMedia at 1440 now 608 | 592 as specified. References 48 at 1440, 24 at 375.

### 2026-11-20 — Foundations: fluid type and spacing (start of the fluid layout refactor)
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** Foundations, Tokens, Docs (affects every live block that uses the type classes or the container)
- **Type:** Foundations
- **Developer action:** Update live foundations: replace `components/bundle.css`. **Ship it together with the component refactor, not alone** — until Hero, IntroMedia, References and the other blocks lose their 768 / 1024 layout switches, some widths look off (for example, at 900–1023 the hero's "40 million" wraps under the tablet layout's narrow column). Tracked in `handoffs/2026-11-20-fluid-layout.md`. `tokens.css` regenerates from `tokens.json` (two new layout tokens; no value changes).
- **What changed:** Display and heading type (display, h1–h3, question, statement, evidence-qualifier, statistic, quotation, cta, hero styles) and the page gutter, grid gap and section padding now scale continuously with `clamp()` from 375 to 1440, between the mobile token (min) and the desktop token (max). New variables `--ja-margin`, `--ja-gap`, `--ja-section`, `--ja-<style>-size`, `--ja-<style>-lh`; fluid type is in rem. The content column is now 100% wide up to 1280 at every width (it used to be capped at 375 below 768 and at 768 from 768 to 1023). All media queries are gone from the foundations; `--ja-cols` is retired (nothing used it). Body, small, label, link and endnote are unchanged. New tokens `fluid-min-width` (375) and `fluid-max-width` (1440); breakpoint and type-mode notes reworded as guidelines. README gains a Responsive behavior section ("media query only when something breaks").
- **Why:** Jerry (Nov 20): layouts adapt continuously; desktop, tablet and mobile designs are guidelines, not breakpoints; media queries only where something breaks.
- **Files:** `components/bundle.css`, `tokens.json`, `README.md`, `system-map.md`, `handoffs/2026-11-20-fluid-layout.md`, `CHANGELOG.md`, `design-system.json`
- **Verified:** HomePage preview rendered with the old and new foundations at 375 / 390 / 600 / 768 / 900 / 1023 / 1024 / 1280 / 1440 / 1600. Identical at 375 and at 1440 and above. At 768 fluid values land within ~6px of the tablet tokens (display 66 vs 72, statistic 60 vs 64, h2 32 vs 36, margin and section 45 vs 40). No new horizontal overflow. Found, not caused by this change: IntroMedia overflows horizontally below 1440 (its grid columns need `minmax(0, …)`) — fix in the IntroMedia refactor.

### 2026-11-19 — Navigation: Resource Library replaces Patient Resources
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** SiteHeader, SiteFooter, HomePage, ResourceCard (docs only)
- **Type:** Update to existing
- **Developer action:** Update live menus — in the WordPress `primary` and footer menus, replace "Patient Resources" (/after-the-yes/patient-resources/) with "Resource Library" (/resource-library/; confirm the final slug). No CSS change.
- **What changed:** Patient Resources is no longer a page. The header, mobile menu and footer nav now link to the Resource Library instead. ResourceCard's bilingual downloads are now documented as part of the Resource Library.
- **Why:** Site structure change: the Patient Resources page was removed; Resource Library takes its nav slot for now.
- **Files:** components/SiteHeader/preview.html, components/SiteHeader/README.md, components/SiteFooter/preview.html, components/HomePage/preview.html, components/ResourceCard/README.md, components/ResourceCard/preview.html, components/ResourceCard/style.css (comment), system-map.md
- **Verified:** text check — no "Patient Resources" left outside earlier changelog entries.

### 2026-11-19 — References: clinical-tint background
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** References
- **Type:** Update to existing
- **Developer action:** Update live block (References, homepage): ship the updated `components/References/style.css`. No markup change. Added to `handoffs/2026-11-18-live-site-updates.md`.
- **What changed:** The section now has a full-width `surface-statistic` (clinical tint) background, matching the interior list panel, and the list numbers are navy instead of blue.
- **Why:** Jerry: the references should live on their own, on the same light gray as the numbered list panel; applies to the homepage too.
- **Files:** `components/References/style.css`, `components/References/README.md`, `handoffs/2026-11-18-live-site-updates.md`, `CHANGELOG.md`, `design-system.json`
- **Verified:** Contrast on #f5fafd: navy text and numbers 13.46:1, muted note 9.01:1 (blue numbers would have been 4.4:1, so changed to navy). Rendered on the Diagnosing page board.

### 2026-11-19 — QuoteBand: sky stroke around the card
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** QuoteBand
- **Type:** Update to existing
- **Developer action:** Update live block (QuoteBand): included in the same `components/QuoteBand/style.css` as today's other QuoteBand changes. Handoff updated.
- **What changed:** The quote card has a 1px `graphic-quiet` (sky) stroke, matching ResourceCard; padding stays inside it.
- **Why:** Jerry's request on the interior-page canvas, approved for the system.
- **Files:** `components/QuoteBand/style.css`, `components/QuoteBand/README.md`, `handoffs/2026-11-18-live-site-updates.md`, `CHANGELOG.md`, `design-system.json`
- **Verified:** Preview rendered at 375 / 768 / 1440 (heights +2px from the stroke: 494 / 562 / 560 band, card +2). Stroke decorative (1.25:1 on white), visible in forced-colors mode.

### 2026-11-19 — QuoteBand: overlap layout on tablet and mobile
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** QuoteBand
- **Type:** Update to existing
- **Developer action:** Update live block (QuoteBand): ship the updated `components/QuoteBand/style.css` (same file as the quote-style change today; no markup change). Handoff updated.
- **What changed:** Below 1024 the photo runs full-bleed (420 tablet / 320 mobile), cropped at 78% so the clinician's face shows, with a white fade over its bottom half; the card rides up over it by 160 / 112 (max 560 wide on tablet). Replaces the stacked photo-then-card layout. Desktop unchanged.
- **Why:** Jerry wanted the desktop look and feel kept on mobile; option B on the interior-page canvas, approved by Jerry.
- **Files:** `components/QuoteBand/style.css`, `components/QuoteBand/README.md`, `handoffs/2026-11-18-live-site-updates.md`, `CHANGELOG.md`, `design-system.json`
- **Verified:** Preview rendered at 375 / 768 / 1024 / 1440: 492 / 560 / 560 / 560 tall, no overflow; text stays on the solid card (contrast unchanged).

### 2026-11-19 — QuoteBand: PullQuote treatment (no side bar)
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** QuoteBand, HomePage (preview)
- **Type:** Update to existing
- **Developer action:** Update live block (QuoteBand): ship the updated `components/QuoteBand/style.css` and output the quote without typed quote marks. Added to `handoffs/2026-11-18-live-site-updates.md`.
- **What changed:** The card's quote now matches the interior-page PullQuote, which Jerry made the source of truth: the 3px blue side bar and its padding are gone, the 64px blue mark sits in a 36px box with the quotation right under it, and the attribution is `text-muted`, 16 below at every size. The large mark is the only quote mark. The planned navy-bar "Blockquote" is replaced by PullQuote (interior canvas).
- **Why:** Jerry: the quote style on the interior-page canvas should be the source of truth.
- **Files:** `components/QuoteBand/style.css`, `components/QuoteBand/README.md`, `components/QuoteBand/preview.html`, `components/HomePage/preview.html`, `handoffs/2026-11-18-live-site-updates.md`, `CHANGELOG.md`, `design-system.json`
- **Verified:** Preview rendered with the system's CSS at 1440 / 768 / 375: band 560 / 584 / 524, no overflow. Attribution muted navy on pale blue 8.22:1. Figma's quote frames still show the bar: update them.

### 2026-11-19 — ClinicalQuestion: copy action becomes a text button in the panel
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** ClinicalQuestion
- **Type:** Update to existing
- **Developer action:** Update live block (ClinicalQuestion, already in the Nov 18 handoff and not yet shipped): put the copy button inside the panel in `.ja-question__actions`, class `ja-question__copy` only (no `ja-button`); Button CSS is no longer needed for it. Handoff updated. `bundle.js` unchanged.
- **What changed:** "Copy the Question" is a quiet underlined navy text button (16/24 SemiBold, 48px target, hover muted, 2px focus ring) under the question, lined up with its text, instead of a filled primary Button below the body.
- **Why:** Jerry found the filled copy button distracting; the interior-page canvas (PageHero question variant) settled on the quiet text action, and the canvas is the source of truth.
- **Files:** `components/ClinicalQuestion/style.css`, `components/ClinicalQuestion/README.md`, `components/ClinicalQuestion/preview.html`, `system-map.md`, `handoffs/2026-11-18-live-site-updates.md`, `CHANGELOG.md`, `design-system.json`
- **Verified:** Preview rendered at 1440 / 768 / 375 (card 1142 tall at 1440), no overflow; action aligned with the question text at 20 / 23 / 33. Navy on pale blue 12.27:1. Figma's copy button instance needs the same change.

### 2026-11-19 — ResourceCard: tags and bilingual downloads; Spanish link token
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** ResourceCard, Tokens
- **Type:** Update to existing
- **Developer action:** None (ResourceCard isn't on the live site). When the Resource Library and Patient Resources are built, use the tag and download markup in the README.
- **What changed:** Two variants from the interior-page canvas. Tags: a format tag filled in its `tag-*` color plus an optional white patient-group tag, at the top of the card. Bilingual downloads: English and Spanish PDF links side by side, Spanish in the new `link-spanish` teal (#0a6670), Spanish left out when there's no file. New token `link-spanish`.
- **Why:** Jerry: the canvas decisions are the source of truth; these cards extend the system's ResourceCard.
- **Files:** `components/ResourceCard/style.css`, `components/ResourceCard/README.md`, `components/ResourceCard/preview.html` (card 640 → 1490), `tokens.json`, `system-map.md`, `CHANGELOG.md`, `design-system.json`
- **Verified:** Preview rendered at 1440 / 768 / 375, no overflow. Tag labels white on each format color 4.63–14.15:1; Spanish link 5.79:1 on pale blue and 2.1:1 against navy.

### 2026-11-19 — Docs: brain pattern placement rules
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** Docs / Assets
- **Type:** Docs
- **Developer action:** None.
- **What changed:** README Imagery and `assets/Patterns/README.md` list the interior-page placements (page header corner, FeaturedResource corner, Contact form, Resource Library empty state) and the rules: allowed inks (pale blue 70% on white, white 75% on pale blue, muted navy on navy, blue only for the small spot illustration), vary crop, scale and rotation, one per section, end inside the section, never on repeated items or strongly behind text.
- **Why:** Jerry asked for more visual interest from the pattern without repeating it; the rules keep future placements consistent.
- **Files:** `README.md`, `assets/Patterns/README.md`, `CHANGELOG.md`
- **Verified:** Placements rendered on the interior-page canvas at 1440 / 768 / 375.

### 2026-11-19 — Tokens: format tag colors
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** Tokens / Foundations (used by the Tag piece on the Resource Library, still on the interior-page boards)
- **Type:** Tokens
- **Developer action:** None yet (Resource Library isn't built). When it is: add the six `--tag-*` variables and give each format tag `ja-tag--format ja-tag--{format-slug}` (e.g. `ja-tag--quick-guide`); an unknown format falls back to navy.
- **What changed:** Six new color tokens, one per resource format: `tag-quick-guide` {blue}, `tag-guideline` {navy}, `tag-tool` #7a5c00 (dark gold), `tag-article` #3d4451 (charcoal), `tag-video` #8e2f7a (berry), `tag-podcast` #4a4fb0 (indigo). README color rules updated. No red or orange (red stays reserved for form errors).
- **Why:** Jerry asked for a color per content type so formats are easier to spot, then for a palette that holds up for color-blind users (the first draft's teal/green and indigo/plum pairs were too close).
- **Files:** `tokens.json`, `README.md`, `CHANGELOG.md`, `design-system.json`
- **Verified:** White label contrast: 4.63 / 14.15 / 6.25 / 9.79 / 7.40 / 6.92 : 1 (AA at 14px). Every pair of the six simulated at full-severity deuteranopia, protanopia and tritanopia (colorspacious, CAM02-UCS): closest pair 11.2 apart (indigo vs berry), against 4.2 for the first draft's teal vs green. Rendered on the Resource Library boards.

### 2026-11-19 — PartnerAttribution: tighter padding when it shows logos only
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** PartnerAttribution
- **Type:** Update to existing
- **Developer action:** Update live block (PartnerAttribution): ship the updated `components/PartnerAttribution/style.css` along with the Nov 18 redesign (added to `handoffs/2026-11-18-live-site-updates.md`). No markup or ACF change; the homepage block (introduction on) is unaffected.
- **What changed:** With Show Introduction off, the section padding is 24 on mobile and tablet and 40 on desktop (was 24 / 40 / 80), so the logo row sits as a band under a page header. Applied automatically with `.ja-partners:not(:has(.ja-partners__head))`; no extra field.
- **Why:** Proposed on the interior-page component boards (The Movement: PageHero followed by the logo row); Jerry approved moving it into the system.
- **Files:** `components/PartnerAttribution/style.css`, `components/PartnerAttribution/README.md`, `components/PartnerAttribution/preview.html` (card height 730 → 700), `handoffs/2026-11-18-live-site-updates.md`, `CHANGELOG.md`, `design-system.json`
- **Verified:** Preview rendered with the system's tokens.css and bundle.css at 375 / 768 / 1440: homepage example unchanged (644 / 532 / 564, padding 24 / 40 / 80); logos-only example 216 / 184 / 136 tall, padding 24 / 24 / 40. No horizontal overflow.

### 2026-11-19 — Tokens: error red for form errors only
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** Tokens / Foundations
- **Type:** Tokens
- **Developer action:** None yet (no form is live). When the Contact form is built: add `--error: #b42318` and `--surface-error: #fef3f2` to the live token variables and use them only for form error states.
- **What changed:** New color tokens `error` (#b42318) and `surface-error` (#fef3f2), not Figma variables. The color rule now reads: red is for form errors only (field border and tint, message and "!" mark, error summary), otherwise only inside the AHS logo. Errors always carry a message, never color alone.
- **Why:** Decision on the interior-page boards (ContactForm): headings stay sentence case, red is used only for form errors. Jerry approved moving the proposed token into the system.
- **Files:** `tokens.json`, `README.md` (Color section and contrast table), `CHANGELOG.md`, `design-system.json`
- **Verified:** Contrast computed (WCAG 2.x): error on white 6.57:1, on surface-error 6.05:1, white on error 6.57:1, navy on surface-error 13.01:1 — all AA for normal text. Rendered a 2px error border on the tint with the system's tokens; values resolve as expected.

### 2026-11-18 — StatisticGrid: 2 × 2 for four stats, columns field, optional intro and link (E11)
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** StatisticGrid
- **Type:** Update to existing
- **Developer action:** Update live block (StatisticGrid): ship the updated `components/StatisticGrid/style.css` and add the fields `show_intro`, `columns` (auto / 2 / 3 → `ja-stats--cols-2` / `--cols-3`), `link` + `show_link` (`<a class="ja-link ja-stats__link">` after the grid). The homepage block (six stats) doesn't change. Added to `handoffs/2026-11-18-live-site-updates.md`.
- **What changed:** On desktop, two or four stats now use 2 columns (four make a 2 × 2 grid of 628-wide cards, as on 05 / The Movement) instead of 3 + 1; three, five or six keep 3 columns. A `columns` field can force 2 or 3. New optional intro toggle and trailing ActionLink (text 32 / 48 below the grid, as in Figma). Tablet stays 2 columns (an odd last card sits alone, half width; Jerry's choice), mobile 1. Intro max width stays 1080 (Jerry; Figma's 1100 changed to match).
- **Why:** Audit item E11 and the Figma "Statistics Section" options (Show Statistic 3 / Row 2 / Statistic 6, Show Body, Show Link). Jerry chose an ACF columns field with auto as the default.
- **Files:** `components/StatisticGrid/style.css`, `components/StatisticGrid/preview.html`, `components/StatisticGrid/README.md`, `handoffs/2026-11-18-live-site-updates.md`, `CHANGELOG.md`, `design-system.json`
- **Verified:** Playwright at 375 / 768 / 1024 / 1440, no horizontal overflow. 1440: six stats 949 (unchanged, = Figma), four stats 948 (2 × 2, = Figma once its row-2 min-height was fixed), three stats grid at 312 (= The Movement), link text 62 below the grid (Figma 48 + 14). Also tested two, five, forced 2 and 3, and intro off. Preview now has three examples (card 2669 tall). **Figma updated** (Jerry approved), Statistics Section `105:140`: Desktop Heading, Body and Show Body connected (were dead), Desktop body 1100 → 1080 to match code, row-2 cards min-height 281 → 280. Mobile: Show Statistic 3 on row 3, rows 4–6 grouped in "Statistics row 2 group" on Show Row 2, row 6 on Show Statistic 6. Tablet: the three 2-card rows replaced by one wrap row (24 gaps, cards 332 fixed), Statistic 3 / 4 / 5 on their toggles, card 6 in a "Statistic 6 slot" (slot on Show Statistic 6, card on Show Row 2). Mobile and Tablet got the Text Link on Show Link (32 below the grid). Description updated: two stats now means hiding Statistic 3 + Row 2 + Statistic 6. Every combination tested on temporary instances at all three breakpoints (removed after). The Movement instances kept their text (now 948 / 592).

### 2026-11-18 — ResourceCard: sky border, muted summary, title in the link for screen readers
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** ResourceCard
- **Type:** Update to existing
- **Developer action:** None (ResourceCard isn't on the live site). When it's built: wrap the card title in `<span class="ja-visually-hidden">: {title}</span>` inside the link, before the arrow, on every card.
- **What changed:** The card has a 1px `graphic-quiet` (sky) border; padding stays 24 inside it. The summary is `text-muted` (replaces this morning's navy choice). The link includes the card title as visually hidden text, so a screen reader hears "Open: How to diagnose migraine" rather than a list of "Open" links.
- **Why:** Jerry's Figma update to Resource Card (17:15) and an accessibility review. Figma's Desktop link was muted while Mobile/Tablet were navy; fixed to navy (Text/Default) in Figma, with Jerry's OK.
- **Files:** `components/ResourceCard/style.css`, `components/ResourceCard/preview.html`, `components/ResourceCard/README.md`, `design-system.json`
- **Verified:** Rendered at 375 / 768 / 1440: cards 248 tall on mobile (Figma 248), content 25 from the outer edge, links 25 from the bottom, no overflow. Contrast on pale blue: link navy 12.3:1, summary and type label muted 8.2:1 (AAA). The border is decorative (1.25:1 on white), and it shows in forced-colors (high-contrast) mode. Accessible names checked: e.g. "Open : Headache diary template".

### 2026-11-18 — CtaBand (Figma only): brain pattern fills taller bands
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** CtaBand
- **Type:** Docs
- **Developer action:** None (code already correct).
- **What changed:** In Figma's CTA Band / Centered, the brain frames were a fixed height (458 / 400 / 500) with a 600px brain, so taller bands (question + body on, and the homepage band since the share link moved under the button) showed an empty navy strip at the bottom. The frames and their gradient rectangles now stretch with the band, and each brain is larger (820 / 720 / 760 tall, aspect kept) and centered vertically, so it covers the tallest option mix (798 / 682 / 728). Variants re-spaced so they don't overlap. No code change: the code brain is already 120% (128% desktop) of the band height, centered.
- **Why:** Jerry noticed the pattern didn't fill the height with Show Question and Show Body on.
- **Files:** `CHANGELOG.md`, `design-system.json`
- **Verified:** Figma screenshots of the component set and The Ask band (556); a test instance with every option on (mobile, 798 tall) has the brain from -11 to 809. Code checked at 375 / 768 / 1440: the brain is taller than the band in every preview example. Figma's default bands now show a slightly larger crop of the brain than the code (Jerry chose this over distorting the brain).

### 2026-11-18 — CtaBand: 24px between the text lines
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** CtaBand
- **Type:** Update to existing
- **Developer action:** Update live block (CtaBand): ship the updated `components/CtaBand/style.css` (same file as the CtaBand entry below; no markup change). Added to `handoffs/2026-11-18-live-site-updates.md`.
- **What changed:** The statement, question and body now sit 24px apart at every width (were 48 on tablet/desktop, 32 on mobile). The space above the buttons stays 48 / 32. Done with a `--ja-cta-gap` custom property and a negative top margin on the question and body, so the markup is unchanged. The homepage band (statement only) doesn't change.
- **Why:** Jerry asked to reduce the space between the text lines only.
- **Files:** `components/CtaBand/style.css`, `components/CtaBand/README.md`, `handoffs/2026-11-18-live-site-updates.md`, `design-system.json`
- **Verified:** Playwright at 320 / 375 / 768 / 1440. At 1440, same as Figma: The Movement 508 tall (body 188, buttons 292, share link 364); The Ask 556 (question 188, body 300, button 404); homepage unchanged at 564 / 464 / 458. No horizontal overflow. **Figma updated** (Jerry approved): in CTA Band / Centered, the statement, question and body are grouped in a "Text" frame with a 24 gap (`Spacing/24`) at all breakpoints; question/body text set back to auto height; description updated. Instances kept their content.

### 2026-11-18 — Button: hover and pressed colors on navy (Tone=Inverse)
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** Button (used in CtaBand)
- **Type:** Update to existing
- **Developer action:** Update live block (CtaBand): ship the updated `components/Button/style.css` (same file as the CtaBand entry below). Added to `handoffs/2026-11-18-live-site-updates.md`.
- **What changed:** On navy (`.ja-on-inverse`), the primary button's hover is now a `sky` fill and its pressed state `pale-blue`, both with a `navy` label. Before, the hover was navy, the same as the band, so the button's fill disappeared. Default look and the secondary button unchanged.
- **Why:** Jerry asked to fix the button hovers after the CtaBand review.
- **Files:** `components/Button/style.css`, `components/Button/README.md`, `handoffs/2026-11-18-live-site-updates.md`, `design-system.json`
- **Verified:** Playwright at 1440 in the CtaBand preview: default rgb(43,121,185) / white; hover rgb(195,236,255) / navy; pressed rgb(227,241,249) / navy. Buttons on white unchanged. **Figma updated** (Jerry approved): Button / Primary has a new Tone=Inverse (Default, Hover Sky + navy label, Focus white ring, Pressed Pale Blue + navy label); every CTA Band Primary instance uses Tone=Inverse (The Ask's "Copy the Question" label restored after the swap).

### 2026-11-18 — CtaBand: secondary button, share link under the buttons, question/body/share options, copy mode (E10)
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** CtaBand, Button (and the HomePage preview), Foundations (`bundle.js`)
- **Type:** Update to existing
- **Developer action:** Update live block (CtaBand): replace the block CSS with `components/CtaBand/style.css` and `components/Button/style.css` (new `ja-button--secondary`); new markup wrappers `.ja-cta__content` and `.ja-cta__buttons`; share link moves under the button; desktop band hugs its content (homepage 500 → 564). New ACF fields `question` + `show_question`, `body` + `show_body`, `secondary_button` + `show_secondary_button`, `show_share_link`, `button_action` (link / copy_question). Replace `bundle.js` (initCopy now also works inside `.ja-cta`). Added to `handoffs/2026-11-18-live-site-updates.md`.
- **What changed:** The actions are now a centered row of the primary button and an optional new secondary button (no fill, 2px white border; hover/pressed fill `muted-navy`, pressed border `sky`), with the share link centered 16px under them; it was beside the button in a fixed 300px box. Optional sky question and body lines (statement → question → body → actions, 32 / 48 / 48 gap). Share link can be turned off. Copy mode turns the primary into "Copy the Question" (The Ask). Desktop: padding 96 and no 500 min-height, content 1020 wide (was 960).
- **Why:** Audit item E10; Jerry asked for a second button for the secondary link with the share link centered under the two buttons, links that hug their text, and Figma's desktop sizing.
- **Files:** `components/CtaBand/style.css`, `components/CtaBand/preview.html`, `components/CtaBand/README.md`, `components/Button/style.css`, `components/Button/README.md`, `components/bundle.js`, `components/HomePage/preview.html`, `handoffs/2026-11-18-live-site-updates.md`, `system-map.md`, `design-system.json`
- **Verified:** Playwright at 320 / 375 / 768 / 1024 / 1440. Homepage default 564 / 464 / 458 tall at 1440 / 768 / 375, button and share link at Figma's exact positions (1440: button 640,348, link 602,420). The Movement (body + secondary) 532 at 1440, every element at Figma's position. The Ask (question + body + copy) 604 at 1440, same as Figma; the copy button copies the question without quotes, reads "Copied", announces the copy. Two buttons stack at 320; no horizontal overflow. **Figma updated** (Jerry approved): new "Button / Secondary" set (Tone=Inverse, 4 states, on 03 / Component sources); CTA Band / Centered actions rebuilt at all breakpoints (Buttons row with Primary + Secondary, 16 gap, wraps; share link hugs its text, centered 16 below); Show Link connected and renamed Show Share Link; Show Secondary Link renamed Show Secondary Button and now drives the new button; unconnected Heading, Button Label and Link Label removed; nested button and link instances exposed; description updated. Page instances kept their content (The Ask still hides the share link).

### 2026-11-18 — IntroMedia: eyebrow, show toggles and H1 option for page intros (E13)
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** IntroMedia
- **Type:** Update to existing
- **Developer action:** Update live block (IntroMedia): replace the block CSS with `components/IntroMedia/style.css` and add ACF fields `eyebrow` + `show_eyebrow` (off), `show_rule` (on), `show_body` (on), `show_link` (on), `heading_level` (h2/h1). Leave out an element when its toggle is off. Added to `handoffs/2026-11-18-live-site-updates.md`.
- **What changed:** Optional eyebrow (`ja-eyebrow ja-label`, blue) between the rule and the heading; the rule, body and link can each be turned off; the heading can be an H1 (`ja-h1`) for inner-page intros. The text column is now a flex column with a 24px gap instead of margins, so a part that's off leaves no space. The default (rule, H2, body, link) looks the same.
- **Why:** Audit item E13; Figma Split Content has these options and 05 / The Movement uses it as the page intro.
- **Files:** `components/IntroMedia/style.css`, `components/IntroMedia/preview.html`, `components/IntroMedia/README.md`, `handoffs/2026-11-18-live-site-updates.md`, `system-map.md`, `design-system.json`
- **Verified:** Rendered at 375 / 768 / 1024 / 1440 with four combinations. Default: 720 / 712 / 570 tall, every element at Figma's position (desktop rule 119, heading 147, body 267, link 403). The Movement page intro at 1440: eyebrow 121, heading 169, body 337, same as Figma. Rule + eyebrow and rule-off cases have no extra gaps. No horizontal overflow. **Figma updated** (Jerry approved): Split Content Desktop Heading, Body and Show Body connected to their layers (the blue "asking" highlight kept); Show Link connected at all breakpoints; Desktop rule color bound to Graphic/Accent; Mobile and Tablet headings now have the blue "asking" highlight (Text/Link) like Desktop and the code; the nested Text Link is exposed and the unused Link Label property removed; component description updated. Existing instances (homepage, The Movement) kept their text.

### 2026-11-18 — PartnerAttribution: centered introduction, no accent rule
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** PartnerAttribution (and the HomePage preview)
- **Type:** Update to existing
- **Developer action:** Update live block (PartnerAttribution), together with the redesign entry below: replace the block CSS with `components/PartnerAttribution/style.css` and remove the `<span class="ja-rule">` before the H2. Added to `handoffs/2026-11-18-live-site-updates.md`.
- **What changed:** The heading, description and link are centered at every size, and the accent rule above the heading is gone. On desktop the 720 intro column is centered in the section.
- **Why:** Jerry asked for the section to be centered without the accent bar.
- **Files:** `components/PartnerAttribution/style.css`, `components/PartnerAttribution/preview.html`, `components/PartnerAttribution/README.md`, `components/HomePage/preview.html`, `handoffs/2026-11-18-live-site-updates.md`, `design-system.json`
- **Verified:** Rendered at 320 / 375 / 768 / 1024 / 1440. Section 644 / 532 / 564 tall at 375 / 768 / 1440, same as Figma; logo row at 452 / 356 / 428 (Figma the same). Desktop intro 720 wide at x 360; link text centered. No horizontal overflow at 320. **Figma updated** (Jerry approved): Partner Collection, all breakpoints, rule removed, heading, body and link centered, Desktop intro centered.

### 2026-11-18 — PartnerAttribution: redesign (stacked intro, one row of bare logos); Show Introduction option (E12)
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** PartnerAttribution (and the HomePage preview)
- **Type:** Update to existing
- **Developer action:** Update live block (PartnerAttribution): (1) replace the block CSS with `components/PartnerAttribution/style.css`. (2) Logo markup: each `li.ja-partner` now holds the `<img>` (wrapped in `<a>` when `url` is set) with no tile; placeholders use `<span class="ja-partner__placeholder ja-small">Logo N</span>`. (3) Add ACF true/false `show_introduction` (default on); when off, leave out `.ja-partners__head` and use `aria-label="Partner organizations"` on the section instead of `aria-labelledby`. Details in `handoffs/2026-11-18-live-site-updates.md`.
- **What changed:** The introduction is stacked (rule, H2, body, link) at every size, max 720 wide on desktop; it was a split row on desktop. The logos sit in one centered, wrapping row with no tile or border, each 56px tall (40 below 768) at its natural width; they were in bordered 110/100px tiles, 4 / 3 / 2 per line. Placeholders are pale-blue blocks labeled "Logo N" in muted navy (144 × 56, 96 × 40 on mobile). New Show Introduction option shows the logo row by itself.
- **Why:** Jerry asked for the logos in a row, with the shape representing the logo rather than a container, and the heading stacked on top of the description. Also audit item E12.
- **Files:** `components/PartnerAttribution/style.css`, `components/PartnerAttribution/preview.html`, `components/PartnerAttribution/README.md`, `components/HomePage/preview.html`, `handoffs/2026-11-18-live-site-updates.md`, `system-map.md`, `design-system.json`
- **Verified:** Rendered at 320 / 375 / 768 / 1024 / 1440 with placeholders and with seven test logos of different shapes. Section 672 / 560 / 592 tall at 375 / 768 / 1440, same as Figma, logo positions within 0px. Lines: 3+3+1 / 4+3 / 7 (5+2 at 1024, 2-up at 320). Logos only: the row starts at the section padding (24 / 40 / 80). No horizontal overflow at 320. **Figma updated** (Jerry approved): Partner Logo / Placeholder has no border, 144 × 56, label "Logo"; Partner Collection has the stacked intro (720 on Desktop, bound to Layout/Prose/Max-Width) and one wrapping logo row (gaps 32 / 16 mobile, 24 between lines); the Show Logo 1–7 and Logo 1–7 properties are now connected to the logo layers (they weren't before).

### 2026-11-18 — Developer handoff note for the live site
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** Docs (covers SiteHeader, TreatmentEvidence, ClinicalQuestion, `bundle.js`)
- **Type:** Docs
- **Developer action:** Read `handoffs/2026-11-18-live-site-updates.md`. It gathers every pending live-block update from today's entries in one place, with a testing checklist.
- **What changed:** Added a `handoffs/` folder for notes to the developer, and the first note in it.
- **Why:** Jerry asked for the handoff to live in the design system, next to the files it refers to.
- **Files:** `handoffs/2026-11-18-live-site-updates.md`, `system-map.md`, `design-system.json`
- **Verified:** Checked the note against today's CHANGELOG entries and the component READMEs.

### 2026-11-18 — ClinicalQuestion: Copy the Question button, show toggles, H1 option (E9); desktop panel padding 48
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** ClinicalQuestion (and `bundle.js`)
- **Type:** Update to existing
- **Developer action:** Update live block (ClinicalQuestion) and replace `bundle.js`: (1) replace the block CSS with `components/ClinicalQuestion/style.css`. The desktop panel's right padding is now 48 (was 32), the panel border uses `border-subtle` (same color), and `.ja-question__after` is now a flex column with a 32 / 24 gap (replaces the link's `margin-top`). (2) Add ACF fields `show_eyebrow`, `show_body`, `show_link` (default on), `heading_level` (h2 / h1, default h2) and `show_copy_button` (default off). Leave out an element when its toggle is off. (3) With `show_copy_button` on, output the button and the `.ja-copy-status` live region exactly as in the README, and enqueue `components/Button/style.css`. (4) `bundle.js` adds `JustAsk.initCopy`, which shows the button and copies the question.
- **What changed:** Added the optional "Copy the Question" primary button. It copies the question without the outer quote marks, reads "Copied" for 2 seconds at the same width, and is announced to screen readers. It stays hidden if the browser can't copy. Added show toggles for the eyebrow, body and link, and an H1 heading option for page-intro use. The desktop panel padding is now 56 / 48 / 56 / 48, as in Figma.
- **Why:** Audit item E9 and the Figma Split Content / Emphasized Text options (`65:443`). Jerry chose: Figma's 48 padding, plain-text copy (no quote marks), a "Copied" label swap, and adding the toggles and H1 option in this pass.
- **Files:** `components/ClinicalQuestion/style.css`, `components/ClinicalQuestion/preview.html`, `components/ClinicalQuestion/README.md`, `components/bundle.js`, `system-map.md`, `design-system.json`
- **Verified:** Rendered at 375 / 768 / 1440 with the homepage block and a page-intro example (H1, no link, copy button). Desktop homepage block 1440 × 511; the panel is 832 × 338, as in Figma (338), with the same line breaks. Mobile panel 327 × 316 (Figma 316 tall). Body to link/button gap 32 / 32 / 24. Clipboard holds the plain question; the label swaps and reverts after 2s at a constant 201px width; the live region announces. No horizontal overflow. Figma: no change needed (the button and options were already there).

### 2026-11-18 — Figma: Resource Library cards equal height per row; sentence-case titles
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** ResourceCard (in Figma's Resource Library, not built yet)
- **Type:** Docs
- **Developer action:** None (Figma only; the ResourceCard CSS already does this).
- **What changed:** In Figma (Resource Library, Desktop): the card grid was a wrapping auto-layout with Hug cards, so rows were uneven. It's now three horizontal rows (24 gaps) with cards set to Fill, like the After the Yes rows. Rows are 302 / 296 / 330 with the links lined up, the same as the code. The nine card titles are now sentence case. (Figma's Grid layout was tried first, but it collapses Fill cards to their padding, so rows were used.) Also fixed in After the Yes (Desktop, Columns=2): its three cards wrap onto two lines, which collapsed their Fill-height summaries so the text ran under the link; those cards now Hug their content. And 16 After the Yes card links that had the underline overridden off are underlined again.
- **Why:** Jerry asked to double-check equal heights against this section; brand rule is sentence case for headings.
- **Files:** —
- **Verified:** Code rendered at 1440 with the same nine cards in a 3-column grid: rows 302 / 296 / 330, card width 411, links aligned. Figma measured the same after the change.

### 2026-11-18 — ResourceCard: type label and show options (E6); link gap 16
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** ResourceCard
- **Type:** Update to existing
- **Developer action:** None (ResourceCard isn't on the live site). When it's built: ACF fields `type_label`, `show_type_label` (default off), `show_summary` (default on), `show_link` (default on); leave out the element when its toggle is off. Use `components/ResourceCard/style.css` as is.
- **What changed:** Added an optional type label (`ja-resource__type ja-label`, 16/24 SemiBold, `text-muted`, 16 above the title) and show toggles for the type label, summary and link. The visible gap above the link is now 16 (was 20), matching Figma. Equal height still works with parts hidden: the summary takes the spare height, or the title when there's no summary. The summary stays navy.
- **Why:** Audit item E6 and the Figma Resource Card (17:15). Jerry chose 16 for the link gap and navy for the summary.
- **Files:** `components/ResourceCard/style.css`, `components/ResourceCard/preview.html`, `components/ResourceCard/README.md`, `design-system.json`
- **Verified:** Rendered at 375 / 768 / 1440 with four cards (default, type label, no summary, no link). Default mobile card is 327 × 246, same as Figma. All gaps 16, 24 inset, links line up at the bottom of each row, no horizontal overflow. Figma updated to match (Jerry approved): summary on `Text/Default` at all three breakpoints; Tablet and Desktop links underlined (Mobile already was).

### 2026-11-18 — Brand README: corner and line weights corrected (D1, D2)
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** Docs
- **Type:** Docs
- **Developer action:** None (the CSS already used these values).
- **What changed:** Corners: statistic cards, partner tiles, resource cards and the callout are listed under `radius-md` (8); `radius-sm` (4) is marked as unused. Lines: brackets, the statistic rule and the hero rule are `stroke-thin-accent` (3); `stroke-accent` (4) is only the 112 × 4 accent rule.
- **Why:** 004 - Website audit items D1 and D2: the README disagreed with Figma and the CSS. (D3 and D4 were already resolved by the Nov 18 Figma sync and handoff update.)
- **Files:** `README.md`
- **Verified:** Checked against the component CSS (`radius-md` in StatisticGrid, PartnerAttribution, ResourceCard; `stroke-thin-accent` in TreatmentEvidence, ClinicalQuestion, StatisticGrid, Hero) and Figma.

### 2026-11-18 — SiteHeader: full-height slide-in menu; header border at every size
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** SiteHeader (and `bundle.js`)
- **Type:** Update to existing
- **Developer action:** Update live block (SiteHeader) and replace `bundle.js`: (1) the header has a 1px `graphic-quiet` bottom border at every width (it was desktop only); (2) below 1024px the menu panel is `position: fixed` from the header's bottom edge to the bottom of the screen, slides in from the right (300ms, none with reduced motion) and has no border; (3) `JustAsk.initHeader` sets `--ja-menu-top`, locks page scroll, keeps Tab inside the header, closes on Escape and when the window widens to desktop. Replace the live header CSS with `components/SiteHeader/style.css`.
- **What changed:** The open menu is now a full-height panel that slides in from the Menu button's side instead of a short dropdown. The single separator is the header's bottom border in every mode. This replaces the panel border from the earlier entry today.
- **Why:** Jerry asked for a full-height panel with the border on the header at all sizes; he chose a slide from the right (the toggle's side) over the left.
- **Files:** `components/SiteHeader/style.css`, `components/SiteHeader/README.md`, `components/bundle.js`
- **Verified:** Rendered at 320 / 375 / 768 / 1023 / 1024 / 1440. Header is 81 below 1024px and 87 at desktop, border at every width. Panel runs from the header bottom (also when the page is scrolled) to the bottom of the viewport. Text inset 24 / 40, link pitch 56. Mid-slide frame checked. Reduced motion: no transition. Tab loop, Escape returns focus, scroll unlocks, closes on resize to desktop. No horizontal overflow. Figma updated to match: Site Header Mobile/Tablet bottom stroke; Navigation Panel Mobile/Tablet full height (731 / 943), no stroke; behaviour noted in the component description.

### 2026-11-18 — Figma synced to code decisions
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** SiteHeader, ResourceCard, SiteFooter, ClinicalQuestion, CtaBand
- **Type:** Docs
- **Developer action:** None (code already matched; Figma now matches the code).
- **What changed:** In Figma (page 03 / Component sources): Navigation Panel Mobile/Tablet got a 1px Graphic/Quiet bottom stroke. Resource Card got Radius/MD (8) corners and an arrow on the link (after a non-breaking space), and its summary fills spare height. In the After the Yes rows, cards Fill the row height. Site Footer links (nav and legal) are bound to a new `Text/Link-On-Soft` variable (navy, mirrors `--text-link-on-soft`). The Question Panel / Emphasized desktop variant is 832 wide (was 851). The CTA Band mobile variant shows the brain pattern. READMEs no longer say Figma differs.
- **Why:** Handoff "pending Figma sync updates"; Jerry approved each edit.
- **Files:** `components/ResourceCard/README.md`, `components/SiteFooter/README.md`, `components/ClinicalQuestion/README.md`, `components/CtaBand/README.md`, `components/SiteHeader/README.md`
- **Verified:** Figma screenshots of After the Yes (tablet), Navigation Panel, Split Content / Emphasized Text (desktop), CTA Band (mobile); question text kept 4 lines at 832.

### 2026-11-18 — SiteHeader open mobile menu matches the Figma Navigation Panel
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** SiteHeader
- **Type:** Update to existing
- **Developer action:** Update live block (SiteHeader mobile/tablet menu, below 1024px): (1) menu links blue (`text-link`), navy on hover/press; (2) an arrow SVG after each label (the ActionLink arrow path without the underline segment; see SiteHeader README for markup), added with a nav-menu walker or `nav_menu_item_title` filter, not typed into menu labels; (3) list is a column with 8px gaps between 48px links and 12px (mobile) / 28px (tablet ≥768) block padding; (4) current page (`aria-current="page"`) navy with a 1px underline, offset 4. The 1px sky bottom border stays. Replace the live header CSS with `components/SiteHeader/style.css`.
- **What changed:** The open menu now matches Figma "Navigation Panel": blue links with arrows, 56px pitch, panel 240 tall on mobile and 272 on tablet (plus the 1px border). The desktop header is unchanged.
- **Why:** 004 - Website audit item E1. Jerry's decisions: keep the bottom border (Figma has none, but the panel overlays white content); mark the current page with navy + underline so it doesn't rely on color alone.
- **Files:** `components/SiteHeader/style.css`, `components/SiteHeader/preview.html`, `components/SiteHeader/README.md`
- **Verified:** Rendered at 320 / 375 / 768 / 1440 with the menu open: link pitch 56, text inset 24 / 40, panel height 240 / 272 + 1px border, hover and current colors; desktop nav unchanged; no horizontal overflow at 320. Figma updated to match (Navigation Panel Mobile/Tablet: 1px Graphic/Quiet bottom stroke).

### 2026-11-18 — TreatmentEvidence mobile bracket arms; CtaBand mobile pattern kept
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** TreatmentEvidence, CtaBand
- **Type:** Update to existing; Docs
- **Developer action:** Update live block (TreatmentEvidence): below 768px the evidence bracket arms are 12px wide (was 24); from 768px they stay 24. CtaBand: none.
- **What changed:** TreatmentEvidence bracket arms now match the Figma mobile frame. CtaBand README records that the brain pattern stays on mobile on purpose.
- **Why:** 004 - Website audit items E2 and E3; Jerry chose to keep the CtaBand pattern on mobile.
- **Files:** `components/TreatmentEvidence/style.css`, `components/TreatmentEvidence/README.md`, `components/CtaBand/README.md`
- **Verified:** Rendered at 375 / 768 / 1440 and measured the bracket arms

### 2026-11-18 — ResourceCard: link at the bottom, arrow in preview
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** ResourceCard
- **Type:** Update to existing
- **Developer action:** None (ResourceCard isn't on the live site yet). Build it with this CSS and the arrow in the link.
- **What changed:** In equal-height cards, the block before the link takes the spare space, so links line up at the bottom of a row. The preview now shows two cards in a row, with the arrow on the link (it was missing from the preview markup).
- **Why:** Jerry's decisions: equal-height cards and arrows on card links.
- **Files:** `components/ResourceCard/style.css`, `components/ResourceCard/preview.html`
- **Verified:** Rendered the preview at 2-up and checked the link positions

### 2026-11-18 — Figma options and notes in component READMEs
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** ResourceCard, IntroMedia, ClinicalQuestion, TreatmentEvidence, CtaBand, StatisticGrid, PartnerAttribution, Button, References, SiteHeader, QuoteBand, ActionLink, SiteFooter
- **Type:** Docs
- **Developer action:** None now. The "Figma options" tables list fields that are "To add"; those become live-block updates when they're built.
- **What changed:** Each README now has a "Figma options" table (property, default, what it does, code field, status) and "Notes" (unconnected Figma properties, pending audit items). ResourceCard records Jerry's decisions: rounded corners, arrow on the link, equal-height cards. ClinicalQuestion keeps the 832px panel.
- **Why:** Jerry asked for the Figma build's optional parts to be written down per component, after the 004 - Website audit.
- **Files:** `components/*/README.md` (the 13 above)
- **Verified:** Checked against `figma-build-notes.md` and the 004 component PDFs (audit, project doc `claude/audit-004-website.md`)

### 2026-11-18 — Changelog added
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** Docs
- **Type:** Docs
- **Developer action:** None
- **What changed:** Added this required changelog, and backfilled the earlier entries.
- **Why:** Track every change and what the developer needs to act on.
- **Files:** `CHANGELOG.md`, `system-map.md`
- **Verified:** —

### 2026-11-18 — Top-view brain pattern
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** StatisticGrid, CtaBand, Assets
- **Type:** Update to existing; Assets
- **Developer action:** Update live block — swap the side-view topographic brains for `Patterns/brain-illustration-top.svg` in StatisticGrid and CtaBand
- **What changed:** The new top-view brain replaces `topographic-brain-01/02` (retired, kept in Assets for now).
- **Why:** New asset used in the design.
- **Files:** `components/StatisticGrid/*`, `components/CtaBand/*`, `README.md`, Patterns assets
- **Verified:** Visual check at 1440 / 768 / 375

### 2026-11-18 — CSS split per component; system map; local working copy
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** Foundations, all components
- **Type:** Foundations; Docs
- **Developer action:** None (same output). Optional: enqueue each block's own `style.css`
- **What changed:** `bundle.css` now holds foundations only; each component has its own `style.css`. Added `system-map.md`. A full copy now lives in `ahs-emp/design-system/`.
- **Why:** Work on one component without loading the whole system.
- **Files:** `components/bundle.css`, `components/*/style.css`, `components/*/preview.html`, `system-map.md`
- **Verified:** Layout identical before and after at 1440 / 768 / 375

### Between 11-04 and 11-18 — AHS logo colors fixed
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** Hero, PartnerAttribution, Assets
- **Type:** Assets
- **Developer action:** Check that the live site uses the two-color AHS logo file (inline fills)
- **What changed:** The logo showed all black because its `<style>` block was stripped on upload. Rebuilt it with inline fills (#231f20, #6f0f10, #fff).
- **Why:** The logo must be two-color.
- **Files:** `Logos/ahs-horizontal-2-color.svg`, Hero and PartnerAttribution previews
- **Verified:** Visual check

### Between 11-04 and 11-18 — Contrast usage notes
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** Tokens, Docs
- **Type:** Docs
- **Developer action:** None
- **What changed:** Reworded the `muted-navy` and `text-link` usage notes. Brand colors are unchanged.
- **Why:** Muted navy on navy is 1.4:1 (decorative only); blue on pale blue is 4.01:1 (use `text-link-on-soft`).
- **Files:** `tokens.json`
- **Verified:** Contrast ratios calculated

### Between 11-04 and 11-18 — Hero animation timing
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** Hero, Foundations
- **Type:** Update to existing
- **Developer action:** Update live block — swap interval 2s; silhouette fades in 0.8s and out 1.6s
- **What changed:** Faster face-grid swaps; the silhouette fades out slower than it fades in.
- **Why:** Jerry's revision.
- **Files:** `components/bundle.css` (`--ja-grid-interval`, `--ja-duration-fade`, `--ja-duration-silhouette-out`), `components/bundle.js`, `components/Hero/style.css`
- **Verified:** Visual check

### Between 11-04 and 11-18 — CtaBand edge-to-centre gradient
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** CtaBand
- **Type:** Update to existing
- **Developer action:** Update live block — add the navy gradient overlay above the brain patterns
- **What changed:** The gradient runs from 0% at each edge to solid navy behind the text.
- **Why:** Jerry's revision.
- **Files:** `components/CtaBand/style.css`
- **Verified:** Visual check at 1440 / 768 / 375

### 2026-11-04 — Initial build
- **By:** Jerry Cavill (via Claude, Cowork)
- **Components:** Tokens, Foundations, Button, ActionLink, ResourceCard, SiteHeader, SiteFooter, References, Hero, IntroMedia, ClinicalQuestion, StatisticGrid, QuoteBand, TreatmentEvidence, PartnerAttribution, CtaBand, HomePage
- **Type:** New component
- **Developer action:** Done — the developer built the homepage from these (with their own ACF fields)
- **What changed:** First release of the system and the homepage.
- **Why:** —
- **Files:** all
- **Verified:** Word positions within 1.5px of the homepage frames at 1440 / 768 / 375
