The American Headache Society's **Just Ask.** campaign site for clinicians. The design is called *Clinical Clarity*: white space, clear hierarchy, human connection. Everything below is a rule for building pages: name the token, style or asset, and don't invent new ones.

## How pages are built

Work in this order: **tokens → typography → components → pages**. A page is a stack of section components filled from the content outline (the AHS_EMP Website Content Model). Don't style one-off sections.

- Every **H2 starts a new section**. Sections use the fluid section padding (`--ja-section`, 48 → 80) above and below, and sit in the content column (`content-width-desktop` max, fluid `--ja-margin` gutters, 24 → 80).
- **Components:**
  - Site chrome: SiteHeader, SiteFooter, References.
  - Sections: Hero, IntroMedia, ClinicalQuestion, StatisticGrid, QuoteBand, TreatmentEvidence, PartnerAttribution, CtaBand.
  - Pieces: Button, ActionLink, ResourceCard.
  - Interior sections (Nov 20, in review): PageHero, StepNav, TextSection, CardGrid, StepCards, FeaturedResource, Timeline, PageNav, ContactForm, RichText, ResourceLibrary.
  - Interior pieces: Callout, PullQuote, ResourceLink, ListBlock, DataBars.
  - Example: `HomePage` shows the homepage set assembled. The interior pages are assembled on the interior-page canvas.
- **Interior pages** add `.ja-interior` to `<main>`: two adjacent sections on the same ground then share one gap. The homepage does not, so its spacing is unchanged. Long pages alternate white and tinted sections (`.ja-section--tint`) for rhythm.
- **Files:** load `tokens.css`, `components/bundle.css` (foundations) and, deferred, `components/bundle.js` on every page. Each component's CSS is in its own `components/<Component>/style.css`. **System map** (the next section) lists every file and its dependencies; read it before changing anything.
- The target is WordPress with ACF: each component is one block, and its README lists the fields it needs. Components are plain HTML with `ja-` classes from the foundations plus their own `style.css`. There's no JavaScript framework; the hero face grid is the only script.
- **Responsive:** fluid from 375 to 1440, with no layout modes. The 375, 768 and 1440 references are guideline checks, not breakpoints. See Responsive behavior below.

## Responsive behavior

Layouts adapt continuously from 1440 down to 375. The mobile, tablet and desktop designs are **guidelines** (goals to check against), not breakpoints.

- **Fluid range: 375 → 1440** (`fluid-min-width`, `fluid-max-width`). Below 375 values hold at their mobile size; above 1440 they stop growing and the content column stays at `content-width-desktop` (1280).
- **Type and spacing use `clamp()`** between the mobile token (min) and the desktop token (max), in a straight line across the range. The variables live in `components/bundle.css`: `--ja-margin`, `--ja-gap`, `--ja-section` and `--ja-<style>-size` / `--ja-<style>-lh`. Use them; don't write new clamp values in components. Fluid type is in rem, so it also follows the reader's browser font-size setting.
- **Tablet tokens are a check.** At 768 the fluid values land within about 6px of them (largest: `display` 66 vs 72, `section` and `margin` 45 vs 40).
- **Grids are intrinsic:** `repeat(auto-fit, minmax(<min>, 1fr))` or flex-wrap, not a column count per width. Splits and asides wrap when their content runs out of room, not at a set width.
- **Components in narrow places respond to their own width** with container queries (`container-type: inline-size` on the block, `@container` rules inside), so the same card or row works in a sidebar, a column or full width.
- **Media queries only where something breaks** and has to be forced at a width. The only layout one is the SiteHeader nav (full links from 1024, Menu below, `breakpoint-desktop`). Two decorative art-direction queries also remain, because CSS can't blend their values smoothly: the Hero veil (768, 1024) and the CtaBand pattern size and edge fade (1024). Each component README names any media query it keeps and why.
- **Split layouts** (IntroMedia, ClinicalQuestion, TreatmentEvidence, QuoteBand, SiteFooter) switch with a container query on their own section, at the width where the narrow column would get too tight (56–64rem), with `minmax(0, …)` columns.
- **Each component README has a short "Responsive behavior" note:** what wraps or stacks, minimum widths, and content-length limits for ACF fields.
- **Check renders at 390, 768 and 1440,** plus one in-between width (such as 1024) to catch anything that only breaks between the references.

## Content fundamentals

- **Audience:** frontline and specialist clinicians. Address them as "you". Patients are "patients", never "sufferers".
- **Voice:** clear and direct, plain clinical language, short declarative headings ("Better migraine care starts with asking", "A disability that can hide in plain sight").
- **Casing:** headings use sentence case. Action links use title case and end with an arrow: "See the Question →", "After the Yes: Guidance and Resources →". The campaign name is always **Just Ask.**, with the period, in logo and display settings. In running text or on a button label it's "Just Ask".
- **The question** is fixed copy and is never reworded: "In the past month, has a headache interfered with your work, school, family, or other activities?"
- **Evidence:** every statistic and quoted claim carries an endnote number that links to References. Use a real `<sup class="ja-sup"><a href="#ref-N">N</a></sup>`, not superscript characters. Endnotes are one fixed size everywhere (`endnote`: 10px Medium, raised 5px), whatever text they follow. Mark pending citations as "Citation pending — …" until the client confirms them.
- Use no emoji and no exclamation marks.

## Color

There are six campaign colors plus one tint, each with a fixed role. Build from the role tokens (`text-*`, `surface-*`, `action-*`, `graphic-*`, `border-*`), never from raw hex values.

- **White is dominant.** `surface-page` is the default. `surface-soft` (pale blue) is for quiet panels: the question panel, quote card, treatment band, resource cards and footer. `surface-statistic` (clinical tint) is for stat cards, InfoCards and the References band. `surface-inverse` (navy) is for the closing CTA band and the one inverse InfoCard in a set that must be seen first.
- **Text:**
  - `text-default` (navy) for headings and body on every light surface.
  - `text-muted` for secondary text.
  - `text-inverse` on navy.
- **Blue is for emphasis and action:** `action-primary-default`, `text-link`, `graphic-accent`, and the highlighted words in large type ("40 million", "asking", "work, school, family, or other activities?").
- **Blue on pale blue fails AA for small text (4.01:1).** Links on `surface-soft` use `text-link-on-soft` (navy). Blue on pale blue is allowed only at 24px and up, such as the question callout.
- **On navy,** highlight lead words in `sky` ("One question,"), with the rest in `text-inverse`.
- **Red is for form errors only** (`error`, `surface-error`): the 2px border and tint on a field in error, the error message and its "!" mark, and the error summary. Otherwise red appears only inside the official AHS logo: never for decoration, emphasis or headings. An error is never shown by color alone; it always has a message.
- **Format tags** on resource cards each have a color (`tag-quick-guide` blue, `tag-guideline` navy, `tag-tool` dark gold, `tag-article` charcoal, `tag-video` berry, `tag-podcast` indigo) with white SemiBold 14px labels, all AA. These colors are only for format tags. Patient-group tags stay white with navy text. The set was chosen so every pair stays distinct under simulated deuteranopia, protanopia and tritanopia; the label still names the format.

Verified contrast pairs:

| Pair | Ratio |
|---|---|
| Navy on white | 14.15:1 |
| Navy on pale blue | 12.27:1 |
| Muted navy on pale blue | 8.22:1 |
| White on blue | 4.63:1 |
| Blue on white | 4.63:1 |
| Blue on clinical tint (large statistics only) | 4.4:1 |
| Sky on navy | 11.29:1 |
| Error on white | 6.57:1 |
| Error on surface-error | 6.05:1 |
| White on error | 6.57:1 |
| Navy on surface-error | 13.01:1 |

## Typography

There's one family: **Montserrat** (`fonts/`, weights 400, 500 italic, 600, 700 and 800). Use the type classes (`ja-h2`, `ja-body`…). Display and heading styles scale fluidly between their mobile and desktop sizes (the `--ja-*-size` / `--ja-*-lh` variables); body, small, label, link and endnote stay the same at every width. The Typography view lists each style's mobile, tablet and desktop values: mobile and desktop are the guardrails, tablet is a check.

| Weight | Used for |
|---|---|
| ExtraBold 800 | Every heading (`h1`–`h3`), the hero lines, `statement` (the question callout), `quotation`, `cta` |
| Bold 700 | `statistic`, `display` (evidence number), `evidence-qualifier`, `question` (compact question panel) |
| SemiBold 600 | `label` (nav, eyebrows, buttons, attribution), `link`, `hero-subtitle` |
| Regular 400 | `body`, `small` (references, captions, legal) |

- `body` is 18/28 in every mode. Keep prose under `prose-max-*`.
- `statistic` and `display` take `tracking-display` (-1px). Everything else uses `tracking-normal`.
- In the hero, "1 in 3" is ExtraBold inside the SemiBold subtitle, and "Led by:" is `small-italic`.
- The `hero-*` styles belong to the Hero layout only. Their tablet and mobile sizes follow the homepage frames, not the Figma variables. Don't use them as general headings.

## Spacing, shape and lines

- **Spacing:** `space-*` from 0 to 96.
  - 24–32 inside content groups.
  - 24–80 between sections (`--ja-section`, fluid).
  - Card padding is `space-24`.
- **Corners:**
  - `radius-md` (8): buttons, statistic cards, partner tiles, resource cards and the callout.
  - `radius-media` (20): the consultation photo, question panel and quote card.
  - `radius-sm` (4): not used at the moment.
  - `radius-portrait` (10): portraits.
  - Bands and photo-fade edges stay square.
- **Lines:**
  - `stroke-border` (1) for decorative borders.
  - `stroke-focus` (2) for focus rings.
  - `stroke-thin-accent` (2, was 3 until Nov 20) for the evidence, question and callout brackets, the statistic and card rules and the hero rule.
  - `stroke-accent` (3, was 4 until Nov 20) for the 112 × 3 accent rule.
- **No shadows.**
- **Accent rule:** a 112 × 4 `graphic-accent` bar above a section heading. The hero uses a 100 × 3 rule under the subtitle.
- **Evidence bracket:** an open bracket (top and bottom bars with short sides, `stroke-thin-accent`) framing a key statistic. Always add its endnote.
- **Question bracket:** an open bracket (`stroke-thin-accent`) on the left of the question callout.

## Imagery

- **Consultation photo** (`Photography/consultation-clinician-patient.webp`): crop to keep the clinician's face clear. Use a soft white edge fade only where text needs room (the quote band). The image is swappable in WordPress and must keep that framing.
- **Portraits** (`Portraits/`): 16 people, each with a hand-made silhouette in `graphic-silhouette`. They are illustrative only. Placement must never imply a real diagnosis, or a diagnosed-to-undiagnosed ratio.
- **Hero face grid:** portraits and silhouettes tiled behind the hero, fading toward the text.
  - It loads in the same arrangement as `Hero/hero-face-grid.webp`, then random cells crossfade between face and silhouette (silhouette in 0.8s `--ja-duration-fade`, silhouette out a slower 1.6s `--ja-duration-silhouette-out`), 2–4 at a time every 2s (`--ja-grid-interval`). On mobile, fewer cells change.
  - It is decorative (`aria-hidden`) and has a pause button (WCAG 2.2.2).
  - It stops off-screen and when the tab is hidden.
  - It is still under `prefers-reduced-motion`.
- **Brain pattern** (`Patterns/brain-illustration-top.svg`, a top-view brain): a faint texture behind the statistic grid and on both edges of the CTA band. Interior pages (Nov 19, interior-page canvas) add: the page header's top-right corner, a corner of the FeaturedResource panel, behind the Contact form (bottom-right, only when the form is the last block), and a small whole brain over the Resource Library's "no results" message. The side-view `topographic-brain-0*` files are retired.
  - Recolor it with a CSS mask (`--ja-pattern-ink`): `pale-blue` at 70% on white, `white` at 75% on pale blue, `muted-navy` on navy. `graphic-accent` only for the small whole-brain spot illustration.
  - Vary the crop, scale and rotation so no two placements on a page look alike, and use at most one per section.
  - It ends inside its section, or runs into an edge of the same color (the pale-blue footer), never into a hard cut.
  - Never behind body text at strength, and never on repeated items (cards, list rows, step navigation).
  - Never put it behind body text at full strength.

## Logos

- **Lockup:** `Logos/just-ask-full-color.svg` (navy "Just" + blue "Ask.") is the header and footer lockup on light grounds. Use `just-ask-white.svg` on navy. One-color navy, blue and black versions are for single-ink use.
- **AHS logo:** `Logos/ahs-horizontal-2-color.svg` is the official mark (dark red and black). It appears only as "Led by:" attribution and in partner rows. Never recolor or redraw it.
- **Partner logos:** they don't exist yet. Use the neutral placeholder tiles until Jerry supplies sized files.

## Motion and states

- **Transitions:** hover and press take 250ms (`--ja-duration-hover`) on color or background only. Nothing moves or scales.
- **Focus:** keyboard focus is always a 2px solid ring (`stroke-focus`) in `border-focus`. It's `text-inverse` on navy.
- **Targets:** every action target is at least `control-min-height` (48px) tall.
- **Primary button states:**
  - Default: `action-primary-default`.
  - Hover: `action-primary-hover`.
  - Pressed: `action-primary-pressed`.
  - Disabled: only when an action is truly unavailable.

## Iconography

There's no icon set. The only glyph is the action arrow, drawn inline as `.ja-arrow` SVG because Montserrat has no "→" glyph. Use real `<sup>` elements for endnote markers, not superscript characters.
