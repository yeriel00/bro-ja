# StatisticGrid

A section of statistic cards: value (`statistic`, blue, -1px tracking), a 40 × 3 blue rule, description and endnote. At 1440 it shows 3 columns, or 2 for two or four stats (a 2 × 2 grid); at 768, 2; at 375, 1. An optional ActionLink follows the grid.

**Specs**

| | Desktop | Tablet | Mobile |
|---|---|---|---|
| Card padding | 32 | 24 | 24 |
| Card min-height | 280 | 252 | (auto) |
| Grid gap | 24 | 24 | 12 |

- **Card:** `surface-statistic` with a 1px `border-subtle` border and `radius-md` (8).
- **Spacing:** the rule sits 16px below the value and 16px above the text. The intro body → grid gap is 48 (desktop) or 32.
- **Pattern:** the brain pattern (`brain-illustration-top.svg`) sits behind the grid, bottom right, `pale-blue` at 70%.
- **Mobile:** the section has 64px bottom padding to leave room for the pattern.
- **Columns (desktop ≥1024):** `columns = auto` (default) gives 2 columns for 2 or 4 stats and 3 columns for 3, 5 or 6 (CSS counts the cards with `:has()`). `ja-stats--cols-2` or `ja-stats--cols-3` on the section forces a count. Tablet is always 2 (an odd last card sits alone on the left, half width); mobile is always 1.
- **Link:** `<a class="ja-link ja-stats__link">` after the `ul`. The link text sits 32 (mobile/tablet) or 48 (desktop) below the grid; the margins are 36 / 52 because the link's 48px box adds 4 more than Figma's 56px link frame. Arrow as in ActionLink.

**Markup (options)**

```html
<section class="ja-section ja-stats [ja-stats--cols-2|ja-stats--cols-3]" aria-labelledby="…">
  <span class="ja-pattern" aria-hidden="true" style="--ja-pattern-url:url('…/brain-illustration-top.svg')"></span>
  <div class="ja-container">
    <span class="ja-rule" aria-hidden="true"></span>
    <h2 class="ja-h2" id="…">{heading}</h2>
    <div class="ja-prose ja-body ja-stats__intro">{intro}</div>          <!-- only if show_intro -->
    <ul class="ja-stats__grid"> <li class="ja-stat">…</li> … </ul>
    <a class="ja-link ja-stats__link" href="{link.url}">{link.title}&nbsp;<svg class="ja-arrow" …></svg></a>   <!-- only if show_link -->
  </div>
</section>
```

**Measured (Nov 18, = Figma):** 1440: six stats 949, four stats (2 × 2, 628-wide cards) 948 (Figma 949 because its row-2 cards had a 281 min-height; fixed), three in a row with the link 772, link text 62 below the grid (Figma 48 + 14). 768: four stats 820. 375: four stats 1264.

**ACF fields:** `heading`, `intro` + `show_intro` (true/false, default on), a `stats` repeater of `value` (text), `description` (text) and `endnote` (number), `columns` (select: auto / 2 / 3, default auto; sets `ja-stats--cols-2` / `--cols-3`), and `link` (link) + `show_link` (true/false, default off).

**Figma options** (Figma "Statistics Section"; "To add" means not in the code yet)

| Figma property | Default | What it does | Code | Status |
|---|---|---|---|---|
| Show Statistic 3 | On | Third card in row 1 | The number of `stats` rows | Built (the count drives the grid; 4 stats = 2 × 2) |
| Show Row 2 | On | Second row of cards | The number of `stats` rows | Built |
| Show Statistic 6 | On | Sixth card | The number of `stats` rows | Built |
| Show Body | On | Shows the intro | `show_intro` (true/false) | Built |
| Show Link | Off | An ActionLink under the grid | `link`, `show_link` | Built |
| (no Figma property) | — | Forces 2 or 3 columns on desktop | `columns` (auto / 2 / 3) | Built |

- **Counts:** 6 (3 × 2), 4 as a 2 × 2 grid (hide Statistic 3 + Statistic 6), 3 in one row (hide Row 2), or 2 (hide Statistic 3 + Row 2). Figma has no 5; code shows 3 + 2.
- **Used on:** 05 / Why Ask: "A common disease with a significant impact" (4, 2 × 2) and "What frontline clinicians told us" (3; that page instance has its bottom padding set to 0 because the next block continues it, a page-level choice).

**Notes**

- Since Nov 18 every property works at all three breakpoints (Desktop Heading/Body/Show Body were dead, and Mobile/Tablet had no count toggles or link). Tablet cards sit in one wrap row (2 per line), so 4 stats make a 2 × 2 there too.
- Figma's link frame is a fixed 340 × 56; code's ActionLink hugs its text (48 tall).

**Don't**

- Don't use more than about 8 words in a value.
- Don't use icons.
- Don't leave a statistic without an endnote.

**Responsive behavior** (fluid, Nov 20)

- No media queries. The grid fits as many 320px-minimum columns as the content width allows, capped at `--ja-stat-cols` (3; 2 for two or four stats or `ja-stats--cols-2`): 1 column at 375, 2 at 768, 3 at 1440, with no fixed switch widths.
- Side-by-side cards keep an even floor height (252 → 280, a container query on the grid); a single column hugs its content.
- Card padding 24 → 32, grid gap 12 → 24, grid top margin 32 → 48, link margin 36 → 52 scale. Bottom padding is the section padding, at least 64 (room for the pattern).
- The brain pattern grows 660 → 900 wide and drifts right with the page.
- **Content limit:** keep labels to about 90 characters so cards in a row stay close in height.

**Optional findings rows** (Nov 20, Why Ask)

- Optional repeater `findings` (`title`, `text`, `quote`, `attribution`, `endnote`) under the stats: each finding (H3 + text) beside the quote that backs it (PullQuote finding variant), sky rules between rows.
- 6/5 columns from a 54rem content box, stacked below. Off by default; the homepage block is unchanged. Needs PullQuote styles.

**Files:** `components/StatisticGrid/style.css` (plus foundations; see System map for dependencies).
