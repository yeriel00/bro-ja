# ClinicalQuestion

The exact clinical question in a pale-blue panel with an open blue bracket, beside an eyebrow, heading, short body, and an optional ActionLink and "Copy the Question" text action in the panel.

**Layout**

- **Wide (section 64rem and up):**
  - Left column 400px: eyebrow, heading, body, link.
  - Gap 48px, then the 832px panel, vertically centered.
  - Panel padding 56 / 48 / 56 / 48 (matches Figma; the right side was 32 until Nov 18, 2026).
  - The panel is 832 wide and ends at the content edge (decided Nov 18, 2026). Figma updated to match the same day (it was 851 and ran 19px past the edge).
- **Narrow:** eyebrow → heading → panel (padding 40/24) → body → link, 32px between blocks.
- At 375 the panel padding is 24/12 (it scales to 56/48).
- **Body and link** stack in `.ja-question__after` with one gap: 32 when stacked, 24 side by side. The link keeps its own width (it doesn't stretch).
- **Question text:** `statement` (44/56 → 34/46 → 28/38) ExtraBold navy. "work, school, family, or other activities?" is in blue, which passes as large text on pale blue.
- **Bracket:** 3px `graphic-accent`, 16px arms, the full height of the text.
- **Panel border:** 1px `border-subtle` (same color as the fill, as in Figma).

**Copy action** (`show_copy_button`, off by default; used on The Ask)

- A quiet text button, "Copy the Question", **inside the panel** under the question and lined up with the question text (12 below it). 16/24 SemiBold navy (`text-link-on-soft`, 12.27:1 on pale blue), underlined; hover `text-muted`; 2px navy focus ring. 48px tall target. Changed Nov 19 from a filled primary Button below the body: the filled button pulled attention from the question (interior-page canvas decision). No Button stylesheet needed.
- It copies the question without the outer quote marks: `In the past month, has a headache interfered with your work, school, family, or other activities?` The text is read from the panel, so it always matches what's shown. Set `data-ja-copy-text` on the button only if the copied text must differ.
- After a copy, the label reads "Copied" for 2 seconds at the same width, and the `.ja-copy-status` live region announces "Question copied to clipboard".
- The button ships with `hidden`. `bundle.js` (`JustAsk.initCopy`) shows it only when the browser can copy, so it never appears as a dead control. It uses the Clipboard API on HTTPS, with a fallback for older browsers.

```html
<figure class="ja-question__panel">
  <blockquote class="ja-question__bracket ja-statement">…</blockquote>
  <div class="ja-question__actions"><button class="ja-question__copy" type="button" data-ja-copy hidden><span class="ja-copy-label">Copy the Question</span></button></div>  <!-- if show_copy_button -->
</figure>
<p class="ja-copy-status ja-visually-hidden" role="status"></p>  <!-- inside .ja-question__grid, after .ja-question__after -->
```

**Heading level** (`heading_level`): `h2` by default; `h1` when the block is a page intro (The Ask). Use `<h1 class="ja-h1">` or `<h2 class="ja-h2">`; the 23px gap under the eyebrow applies to both.

**ACF fields:** `eyebrow`, `show_eyebrow` (default on), `heading`, `heading_level` (h2 / h1, default h2), `question`, `question_highlight`, `body`, `show_body` (default on), `link`, `show_link` (default on), `show_copy_button` (default off). Leave out an element when its toggle is off. If body, link and copy button are all off, leave out `.ja-question__after`; on desktop the intro then centers beside the panel. The question text is fixed campaign copy; edit it only with AHS approval.

**Figma options** (Figma "Split Content / Emphasized Text", `65:443`; panel is "Question Panel / Emphasized", `162:202`)

| Figma property | Default | What it does | Code | Status |
|---|---|---|---|---|
| Show Eyebrow | On | Shows the eyebrow | `show_eyebrow` | Built |
| Show Body | On | Shows the body copy | `show_body` | Built |
| Show Link | On | Shows the text link | `show_link` | Built |
| Show Copy Button | Off | Adds "Copy the Question", which copies the question text | `show_copy_button` + `JustAsk.initCopy` in `bundle.js` | Built (Nov 18, 2026); quiet text action in the panel since Nov 19 (Figma still shows a filled button: update it) |
| Heading AHS/H1 (instance override, per the component description) | H2 | Page-intro use | `heading_level` | Built |

**Notes**

- The panel is also its own piece in Figma ("Question Panel / Emphasized"). It's proposed as QuestionPanel, for PageIntro "with question panel". Keep the existing `ja-question__*` classes when it's split out.
- The copy action used to be the standard primary Button (201 × 56) below the body. Since Nov 19 it's a text action inside the panel; Figma's "Copy the Question" instance needs the same change.
- Figma draws the mobile question at a fixed 279 width; code lets it fill the panel (liquid layout).
- As H1 on desktop, the heading runs to four lines in the 400 column (64/72).

**Don't**

- Don't reword the question.
- Don't set the whole question in blue.
- Don't put small blue text on the pale panel.
- Don't show the copy button without `bundle.js`; it stays hidden.

**Responsive behavior** (fluid, Nov 20)

- Panel padding (24/12 → 56/48) and bracket inset (20 → 33) scale with the page.
- The intro | panel split is a container query on the section (`container: ja-question`, 64rem): the intro column needs ~280px for the heading. Below it, the blocks stack: intro → panel → body/link. No media queries.
- Columns are `minmax(0, …)`, so a long word can't push the page wider.

**Optional supporting stat** (Nov 20, Why Ask)

- Optional fields `show_stat` (off by default), `stat_value`, `stat_label`, `stat_endnote`. Off: the homepage block, unchanged.
- On: add `ja-question--top` to the section and wrap the panel and a `ja-stat ja-stat--wide` card in `.ja-question__side`. The side column starts level with the accent rule; the panel takes the card's 8px corners. Needs StatisticGrid styles.
- The wide stat stacks value, rule and label under a 48rem section.

**Files:** `components/ClinicalQuestion/style.css`, `components/bundle.js` (copy button) (plus foundations and ActionLink; see System map for dependencies).
