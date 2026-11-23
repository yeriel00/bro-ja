# Just Ask. — interior pages release (developer notes)

Nov 20, 2026 · Jerry Cavill · **One release: the fluid layout refactor, the homepage updates below, and the interior-page components ship together.** Interior components are marked "in review" until the interior pages are signed off; build them, but expect small copy and layout changes.

Read with: `handoffs/2026-11-20-fluid-layout.md` (the fluid refactor, unchanged and still part of this release), the interior-page canvas (Pages + Components) and the developer handoff doc that comes with it.

## 1. Foundations and tokens

Replace `components/bundle.css`; regenerate `tokens.css` from `tokens.json`.

| Change | Value | Effect on the live homepage |
| --- | --- | --- |
| `stroke-accent` | 4 → 3px | Every H2 accent rule (112 × 3) |
| `stroke-thin-accent` | 3 → 2px | Hero rule, quote card side bar, question and evidence brackets, stat rules |
| `section-padding-mobile` and `--ja-section` | 24 → 48 (`clamp(48px, …, 80px)`) | Sections on phones get more room (~+48 per section at 375); 1440 unchanged |
| New `text-link-on-tint` (#22679f), `tag-quick-guide-text` | — | None (used by interior cards and rows) |
| Interior foundations | `ja-content` container queries, `.ja-section--tint`, `.ja-interior` same-ground spacing, `ja-minirule`, `ja-nowrap`, 13 × 24 direction arrow | None: the homepage has no `.ja-interior` and no tinted sections |

**Template:** add `class="ja-interior"` to `<main>` on interior page templates only.

## 2. Existing blocks (live on the homepage)

All new options are off by default, so the homepage looks the same apart from the token changes above.

| Block | Change | Developer action |
| --- | --- | --- |
| Button | Long labels wrap; new `.ja-button--outline` | Replace `style.css` |
| ResourceCard | Action is an outline Button labelled by format (View Guide, Read Guideline, Open Tool, Read Article, Watch Video, Listen) | Replace `style.css`; swap the card's ActionLink for the button; enqueue Button with ResourceCard |
| ClinicalQuestion | Optional stat (`show_stat`, `stat_value`, `stat_label`, `stat_endnote`) and top alignment | Replace `style.css`; add the optional fields; enqueue StatisticGrid when the stat is on |
| StatisticGrid | Optional findings repeater | Replace `style.css`; add the optional repeater; enqueue PullQuote when used |
| QuoteBand | White card option (`ja-quote--white`) | Replace `style.css`; add a card colour select (default pale blue) |

## 3. New interior components

Each has `style.css`, `README.md` (markup, ACF fields, responsive behavior) and `preview.html` in `components/<Name>/`. Build each as an ACF flexible-content layout (pieces render inside them).

| Component | Kind | Used on |
| --- | --- | --- |
| PageHero | Layout | Every interior page |
| StepNav | Layout | Diagnosing, Treating, Ongoing Care |
| TextSection | Layout | Most pages |
| CardGrid | Layout | Most pages |
| StepCards | Layout | After the Yes |
| FeaturedResource | Layout | After the Yes |
| Timeline | Layout | Ongoing Care |
| PageNav | Layout | Step pages |
| ContactForm | Layout | Contact |
| RichText | Layout | Terms, Privacy |
| ResourceLibrary | Template | /resources/ |
| Callout, PullQuote, ResourceLink, ListBlock, DataBars | Pieces | Inside the layouts above |

Library items (ResourceCard, ResourceLink, FeaturedResource, card footer links) come from one Resource post type via relationship fields.

## Testing checklist

- [ ] Homepage at 375 / 768 / 1440: identical to today except thinner accent rules and brackets, and more section padding on phones (about +256px total at 375; 1440 within 3px).
- [ ] No horizontal scroll at any width from 320 to 1600 on the homepage and every interior page.
- [ ] Interior pages match the canvas Pages boards at 1440, and stack cleanly at 375.
- [ ] Same-ground spacing only on interior templates (`.ja-interior`); homepage spacing unchanged.
- [ ] Resource Library filters, counts, Clear filters and empty state; filters in the URL.
- [ ] Contact form: error summary focus, inline errors, success to Thank you.
- [ ] Keyboard: every card link, row, button and filter reachable with a visible 2px focus ring.
