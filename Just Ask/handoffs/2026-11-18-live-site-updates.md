# Just Ask. — live site updates for the developer

Nov 18, 2026 · Jerry Cavill

## Overview

Nine blocks on the live homepage need updating to match the design system: **SiteHeader**, **TreatmentEvidence**, **ClinicalQuestion**, **StatisticGrid**, **PartnerAttribution**, **QuoteBand** and **References** (added Nov 19), **IntroMedia** and **CtaBand** (plus a new secondary style in the shared **Button** CSS). One shared script, `components/bundle.js`, is replaced once and covers the header menu and the copy buttons.

All files are in the [Just Ask. design system](https://claude.ai/artifact/88BTqKM1B4aFC4ZX3AfNAL). Paths below are relative to the design system root (the `project/` folder in the published design system). Each component's `README.md` has the markup, specs and ACF fields; `CHANGELOG.md` has the dated entries these notes come from.

| Block | What changes | CSS | JS | ACF |
| --- | --- | --- | --- | --- |
| SiteHeader | Full-height slide-in mobile menu, blue links with arrows, header border at every width | Replace | Replace `bundle.js` | No change |
| TreatmentEvidence | 12px bracket arms below 768px | Replace | — | No change |
| ClinicalQuestion | Desktop panel padding, new show toggles and H1 option, optional copy action (a quiet text button inside the panel, updated Nov 19) | Replace | Replace `bundle.js` | New fields |
| StatisticGrid | 2 × 2 for four stats (auto, or a `columns` field), optional intro and trailing link. Homepage look unchanged | Replace | — | New fields |
| PartnerAttribution | Redesign: centered intro (no accent rule), one row of bare logos (no tiles); Show Introduction option | Replace | — | New field |
| QuoteBand (Nov 19) | Quote style matches the interior PullQuote: no blue side bar, smaller mark box, muted attribution, no quote marks in the text; below 1024 the card overlaps a fading full-bleed photo | Replace | — | No change |
| References (Nov 19) | Clinical-tint (#f5fafd) full-width background; list numbers navy instead of blue | Replace | — | No change |
| IntroMedia | Optional eyebrow, rule, body and link; H1 option for page intros. Homepage look unchanged | Replace | — | New fields |
| CtaBand | Share link moves under the button (homepage band 500 → 564 on desktop); optional question, body, secondary button, share toggle, copy mode | Replace (+ `Button/style.css`) | Uses `bundle.js` in copy mode | New fields |

Suggested order: replace `bundle.js` first, then SiteHeader, TreatmentEvidence, ClinicalQuestion, StatisticGrid, PartnerAttribution, QuoteBand, IntroMedia, CtaBand and References. Code names and the `ja-` classes are unchanged.

## Shared files

Replace the live `bundle.js` with `components/bundle.js` (8,676 bytes). It now exposes `window.JustAsk` with four functions:

| Function | Runs on | Used by |
| --- | --- | --- |
| `initFaceGrid` | `.ja-hero` | Hero (unchanged) |
| `initHeader` | `.ja-header` | SiteHeader: menu toggle, scroll lock, focus loop, Escape, close at desktop |
| `initCopy` | `[data-ja-copy]` | ClinicalQuestion and CtaBand copy buttons (new) |
| `initAll` | the whole page | Calls the three above; runs on its own at `DOMContentLoaded` |

- Enqueue `tokens.css`, `components/bundle.css` and `bundle.js` globally, as before. Load `bundle.js` in the footer with `defer`.
- Each init is safe to call more than once. If a block is added after load (block preview, AJAX), call `window.JustAsk.initAll(container)`.
- `tokens.css` and `bundle.css` are unchanged.

## SiteHeader

The mobile and tablet menu (below 1024px) is now a full-height panel that slides in from the right, and the header has its bottom border at every width. Replace the live header CSS with `components/SiteHeader/style.css` and replace `bundle.js`. The desktop nav is unchanged.

**Header bar**

- 1px `graphic-quiet` (sky) bottom border at every width. It used to be desktop only.
- Bar height is unchanged: 80 + 1 below 1024px, 86 + 1 from 1024px.

**Open menu panel (below 1024px)**

- `position: fixed` from the header's bottom edge (`--ja-menu-top`, set by the script) to the bottom of the screen. No border on the panel.
- Slides in from the right, 300ms. No slide with `prefers-reduced-motion`.
- Links in `text-link` (blue), navy on hover and press. 48px targets, 8px apart (56px pitch). Block padding 12 (mobile) / 28 (tablet).
- Current page (`aria-current="page"`): navy with a 1px underline, offset 4.
- An arrow SVG follows each label (the ActionLink arrow without its underline segment; markup in the SiteHeader README). Add it with a nav-menu walker or the `nav_menu_item_title` filter. **Don't type "→" into menu labels**: Montserrat has no arrow glyph and screen readers would read it.

**Behaviour (`JustAsk.initHeader`)**

- Locks page scroll while open (`overflow: hidden` on `<html>` plus the `ja-menu-open` class).
- Keeps Tab inside the header (logo, Close, menu links). Escape closes the menu and returns focus to the toggle.
- Closes when the window widens to 1024px or more.
- The toggle label switches between "Menu" and "Close" and sets `aria-expanded`.

**WordPress:** menu location `primary`, labels without the arrow. No ACF change.

## TreatmentEvidence

Below 768px the evidence bracket arms are 12px wide (they were 24). From 768px they stay 24. Replace the live block CSS with `components/TreatmentEvidence/style.css`. No markup or ACF change.

## ClinicalQuestion

Replace the live block CSS with `components/ClinicalQuestion/style.css`, add five ACF fields, and output the copy button when it's on. The homepage instance looks the same apart from slightly narrower question lines on desktop.

**CSS changes**

- Desktop panel padding is 56 / 48 / 56 / 48 (the right side was 32).
- Panel border uses `border-subtle` (same color as before).
- `.ja-question__after` is a flex column with a 32px gap (24 from 1024px). This replaces the link's `margin-top`.
- The 23px gap under the eyebrow applies to an H1 or an H2.
- When body, link and copy button are all off, leave out `.ja-question__after`; on desktop the intro then centers beside the panel.
- The copy action no longer needs `components/Button/style.css` (updated Nov 19).

**New ACF fields** (existing fields unchanged: `eyebrow`, `heading`, `question`, `question_highlight`, `body`, `link`)

| Field | Type | Default | Output |
| --- | --- | --- | --- |
| `show_eyebrow` | True/false | On | Eyebrow `<p class="ja-eyebrow ja-label">` |
| `show_body` | True/false | On | `.ja-prose` body |
| `show_link` | True/false | On | The ActionLink |
| `heading_level` | Select: h2, h1 | h2 | `<h2 class="ja-h2">` or `<h1 class="ja-h1">` (h1 for a page intro, e.g. The Ask) |
| `show_copy_button` | True/false | Off | Copy action + status region (below) |

Leave an element out of the markup when its toggle is off; don't hide it with CSS.

**Copy action markup** (updated Nov 19)

A quiet text button inside the panel, after the question, in `.ja-question__actions` (it lines up with the question text). The status paragraph goes inside `.ja-question__grid`, after `.ja-question__after`. Keep `hidden` on the button: the script removes it only when the browser can copy. No `ja-button` class.

```html
<figure class="ja-question__panel">
  <blockquote class="ja-question__bracket ja-statement">…</blockquote>
  <div class="ja-question__actions"><button class="ja-question__copy" type="button" data-ja-copy hidden><span class="ja-copy-label">Copy the Question</span></button></div>
</figure>
<p class="ja-copy-status ja-visually-hidden" role="status"></p>
```

**Copy behaviour (`JustAsk.initCopy`)**

- Copies the question from the panel without the outer quote marks: "In the past month, has a headache interfered with your work, school, family, or other activities?" Set `data-ja-copy-text` on the button only if the copied text must differ.
- The label reads "Copied" for 2 seconds, then reverts. The width is held so nothing shifts.
- The status region announces "Question copied to clipboard".
- Uses the Clipboard API on HTTPS, with a fallback for older browsers. The live site must be on HTTPS.

## PartnerAttribution

Redesigned. Replace the live block CSS with `components/PartnerAttribution/style.css`, update the logo markup, and add one ACF field. See `components/PartnerAttribution/README.md` for the full markup.

- The introduction is stacked and centered (H2, body, link) at every width, max 720 wide and centered on desktop. The desktop split row is gone. **Remove the `<span class="ja-rule">` before the H2**; the accent rule is no longer used here.
- Logos have no tile. Each `li.ja-partner` holds the `<img>` (wrapped in `<a>` when the partner has a `url`). Logos are 56px tall (40 below 768) at their natural width, in one centered wrapping row.
- Until real logos arrive, output `<span class="ja-partner__placeholder ja-small">Logo N</span>` inside each `li` (pale-blue block, muted label).
- New true/false field `show_introduction` (default on). When it's off, leave out the whole `.ja-partners__head` and output the logo list as the first child of `.ja-container`; use `aria-label="Partner organizations"` on the `<section>` instead of `aria-labelledby`.
- *Added Nov 19:* with Show Introduction off, the section padding tightens to 24 (mobile, tablet) / 40 (desktop). It is in the same `style.css` and needs no markup or field change.

## QuoteBand

Added Nov 19. The quote now uses the same treatment as the interior PullQuote. Replace the live block CSS with `components/QuoteBand/style.css` and drop the typed quote marks from the template.

- No blue bar on the left of the quote, and no left padding for it.
- The large blue quote mark sits in a 36px-tall box; the quotation follows directly under it (no 16 / 24 gap).
- The attribution is `text-muted` (8.22:1 on pale blue), 16px below the quotation at every size.
- The card has a 1px sky (`graphic-quiet`) stroke, like the resource cards; padding stays inside it.
- Output the `quote` field without quote marks: the large mark is the only one. `<blockquote>` already tells screen readers it is a quote.
- **Below 1024 (overlap layout):** the photo is full-bleed, 420 tall on tablet / 320 on mobile, cropped at 78% horizontally (clinician's face), with a white fade over its bottom half; the card overlaps it by 160 / 112 (max 560 wide on tablet). All in the CSS; no markup change. Desktop is unchanged.

## References

Added Nov 19. Replace the live block CSS with `components/References/style.css`. No markup or field change.

- The section has a full-width `surface-statistic` (clinical tint, #f5fafd) background, so the reference list reads as its own section.
- List numbers are navy (was blue): blue is 4.4:1 on the tint, under AA for 14px text.

## StatisticGrid

New options for inner pages (The Movement uses four stats as a 2 × 2 grid and three in a row). The homepage block (six stats) looks the same. Replace the block CSS with `components/StatisticGrid/style.css` and add the fields. Markup is in `components/StatisticGrid/README.md`.

- Desktop columns are automatic: 2 columns for two or four stats, 3 for three, five or six. New field `columns` (select: auto / 2 / 3, default auto): 2 adds `ja-stats--cols-2` to the section, 3 adds `ja-stats--cols-3`, auto adds nothing.
- `show_intro` (default on): when off, leave out `.ja-stats__intro`.
- `link` (link) + `show_link` (default off): outputs `<a class="ja-link ja-stats__link">` after the `ul`, with the ActionLink arrow. ActionLink's CSS must be loaded on pages that use it.

## IntroMedia

New options so the block can also be an inner-page intro (e.g. The Movement). The homepage block looks the same. Replace the live block CSS with `components/IntroMedia/style.css` and add the fields. Markup is in `components/IntroMedia/README.md`.

- The text column is now a flex column with a 24px gap (rule → eyebrow → heading → body → link), not margins. Leave out an element when its toggle is off; no spacing is left behind.
- New fields: `eyebrow` (text) + `show_eyebrow` (default off), output as `<p class="ja-eyebrow ja-label">`; `show_rule` (default on); `show_body` (default on); `show_link` (default on); `heading_level` h2 / h1 (default h2), h1 outputs `<h1 class="ja-h1">`.

## CtaBand

The homepage band changes look: the share link now sits **centered under the button** (16px below), and the desktop band hugs its content with 96px top/bottom padding instead of a 500px minimum height, so the homepage band is 564 tall on desktop (464 tablet, 458 mobile). Replace the block CSS with `components/CtaBand/style.css` and the shared `components/Button/style.css` (adds `ja-button--secondary`, and on navy the primary's hover is now sky and pressed pale blue, with a navy label). Markup is in `components/CtaBand/README.md`.

- The statement, question and body sit 24px apart at every width; the buttons stay 48px (32 on mobile) below the text. This is all in the CSS.
- New wrappers: `.ja-cta__content` around everything inside `.ja-container`, and `.ja-cta__buttons` around the button(s) inside `.ja-cta__actions`. The share link stays in `.ja-cta__actions`, after `.ja-cta__buttons`.
- New fields: `question` + `show_question` (off, `<p class="ja-cta__question ja-question">`), `body` + `show_body` (off, `<p class="ja-cta__body ja-body">`), `secondary_button` (link) + `show_secondary_button` (off, `<a class="ja-button ja-button--secondary">`), `show_share_link` (on), `button_action` link / copy_question (default link).
- Copy mode outputs `<button class="ja-button" type="button" data-ja-copy hidden><span class="ja-copy-label">…</span></button>` and `<p class="ja-copy-status ja-visually-hidden" role="status"></p>` inside the container; `bundle.js` shows the button and copies the band's question.

## Testing checklist

Check each item at 375, 768 and 1440 wide, and confirm there's no horizontal scroll at 320.

**SiteHeader**

- [ ] Header bar has the 1px sky bottom border at every width.
- [ ] Below 1024px the menu fills the screen under the header, also when the page is scrolled, and slides in from the right.
- [ ] With reduced motion turned on, the menu opens without the slide.
- [ ] Page doesn't scroll behind the open menu. Tab stays in the header; Escape closes it and focus returns to Menu.
- [ ] Widening the window to 1024px or more closes the menu.
- [ ] Links are blue with an arrow and 56px apart; the current page is navy and underlined.

**TreatmentEvidence**

- [ ] Bracket arms are 12px below 768px and 24px from 768px.

**ClinicalQuestion**

- [ ] Homepage block at 1440: panel 832 × 338, 48px padding on both sides, question on four lines.
- [ ] Gap from body to link is 32px below 1024px and 24px from 1024px.
- [ ] Each show toggle removes its element; the heading switches between H2 and H1.
- [ ] With the copy action on: it sits inside the panel, 12px under the question and aligned with its text, as an underlined navy text button (no fill); the clipboard holds the question without quote marks; the label reads "Copied" for 2 seconds at the same width; a screen reader announces the copy.
- [ ] With JavaScript off, the copy action doesn't appear.

**References**

- [ ] The reference section has a clinical-tint background edge to edge; numbers are navy.

**QuoteBand**

- [ ] Band 560 / 562 / 494 tall at 1440 / 768 / 375 with the homepage quote.
- [ ] Below 1024 the card overlaps the bottom of the photo, which fades to white; the clinician's face is in view.
- [ ] No blue side bar; the quote mark, quotation and muted attribution line up on the card's left padding. The card has a 1px sky stroke.
- [ ] The quotation has no typed quote marks.

**StatisticGrid**

- [ ] Homepage block unchanged: 949 tall at 1440 (3 + 3), 1140 at 768, 1738 at 375.
- [ ] Four stats at 1440: 2 × 2, cards 628 wide; three stats: one row of three.
- [ ] `columns` = 2 or 3 forces that count on desktop; tablet stays 2, mobile 1.
- [ ] Show Link: link text 48px below the grid on desktop, 32px below on smaller screens. Intro off: the grid follows the heading.

**PartnerAttribution**

- [ ] Homepage block with placeholders: 564 tall at 1440 (all 7 logos on one line), 532 at 768 (4 + 3), 644 at 375 (3 + 3 + 1). Heading, description and link centered; no accent rule. No tiles or borders behind real logos; each is 56px tall (40 below 768).
- [ ] With Show Introduction off, only the logos show, with tighter section padding (24 / 24 / 40 at 375 / 768 / 1440; with placeholders 216 / 184 / 136 tall), and the section is announced as "Partner organizations".

**IntroMedia**

- [ ] Homepage block unchanged: 570 tall at 1440 (rule at 119, heading 147, body 267, link 403 from the section top), 712 at 768, 720 at 375.
- [ ] Page intro (eyebrow on, rule off, H1, link off) at 1440: eyebrow at 121, heading 169 (64/72), body 337.
- [ ] Each toggle removes its element with no gap left behind; with the rule off the eyebrow or heading starts at the top of the text column.

**CtaBand**

- [ ] Homepage: share link centered under Just Ask, 16px below; band 564 / 464 / 458 tall at 1440 / 768 / 375.
- [ ] Question and body sit 24px below the line above them; the buttons 48px (32 on mobile) below the text.
- [ ] With the secondary button on, the two buttons sit side by side (16 apart) and stack on narrow phones.
- [ ] Copy mode: the button appears, copies the question without quote marks, reads "Copied" for 2s.
- [ ] Secondary button: white ring 2px outside the border on keyboard focus.
- [ ] Just Ask on the band: hover turns sky with a navy label, pressed pale blue.
