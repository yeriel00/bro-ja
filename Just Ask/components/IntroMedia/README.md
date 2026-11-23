# IntroMedia

Rich text + campaign imagery: the consultation photo beside an accent rule, H2, short body and an ActionLink. It covers components 04 and 05 in the component plan.

**Layout**

- **Wide (section 896px and up):** photo | text in a 608 : 592 split, vertically centered, gap up to 80. `radius-media`, `object-fit: cover`.
- **Narrow:** text first, then the photo, 32px apart.

**Responsive behavior** (fluid, Nov 20)

- The block responds to its own width: `.ja-intro` (the section) is a size container named `ja-intro`, and one container query (`min-width: 56rem`) puts the photo beside the text. Below that, each column would be under ~360px and the text gets squeezed. Keep `ja-intro` on the section.
- Columns are `minmax(0, …)`, so the photo can never push the text column narrower or the page wider. (Before, the image's intrinsic width did both: the text column was 287px at 1440 and the page scrolled sideways below 1440.)
- Photo height scales with the section: 220 at 375, ~320 at 768, 410 max. Column gap 40 → 80.
- No media queries.
- **ACF limits:** body under 250 characters (unchanged). The narrowest split (section ~900) gives the text ~370px, so keep headings short.
- **Text column:** a flex column with a 24px gap: rule → eyebrow → heading → body → link. Every part except the heading is optional, and a part that's off leaves no space behind.

**Markup (text column)**

```html
<div class="ja-intro__text">
  <span class="ja-rule" aria-hidden="true"></span>              <!-- show_rule -->
  <p class="ja-eyebrow ja-label">Why Ask</p>               <!-- show_eyebrow -->
  <h2 class="ja-h2" id="…">Better migraine care starts with <span class="ja-hl">asking</span></h2>
  <div class="ja-prose ja-body"><p>…</p></div>                   <!-- show_body -->
  <a class="ja-link" href="…">See the Question&nbsp;<svg class="ja-arrow">…</svg></a>  <!-- show_link -->
</div>
```

With `heading_level` = h1, use `<h1 class="ja-h1">` (fluid, 36/44 → 64/72). Leave out any element whose toggle is off.

**ACF fields**

- `eyebrow`: text. `show_eyebrow`: true/false, default off.
- `show_rule`: true/false, default on.
- `heading`: text, with a span option for the blue highlighted word.
- `heading_level`: select h2 / h1, default h2. Use h1 when the block is the page intro (one H1 per page).
- `body`: WYSIWYG, under 250 characters, endnotes allowed. `show_body`: true/false, default on.
- `link`: link. `show_link`: true/false, default on.
- `image`: image (swappable; keep the clinician's face clear).
- `image_position`: left/right (an intentional addition for reuse on inner pages).

**Page intro with photo** (05 / Why Ask): eyebrow on, rule off, H1, link off. Desktop measures the same as Figma (eyebrow at 121, heading 169, body 337 in a 570 section).

**Figma options** (Figma "Split Content")

| Figma property | Default | What it does | Code | Status |
|---|---|---|---|---|
| Eyebrow | "Why Ask" | Label above the heading (AHS/Eyebrow, Text/Link) | `eyebrow` (text) | Built |
| Show Eyebrow | Off | Shows the eyebrow | `show_eyebrow` | Built |
| Show Rule | On | Shows the 112 × 4 accent rule | `show_rule` | Built |
| Heading | — | Heading text | `heading` | Built |
| Body | — | Body text | `body` | Built |
| Show Body | On | Shows the body | `show_body` | Built |
| Label (nested Text Link, exposed) | "See the Question →" | Link text | `link` (title) | Built |
| Show Link | On | Shows the link | `show_link` | Built |
| Heading AHS/H1 (instance override, per the component description) | H2 | Page-intro use | `heading_level` | Built |

**Notes**

- Figma (Nov 18): every property is connected to its layer at all three breakpoints (before, Desktop's Heading/Body/Show Body and Show Link everywhere did nothing). The old Link Label property was removed: the nested Text Link is exposed, so its own Label shows in the Split Content panel.
- Both the rule and the eyebrow can be on together (rule first). As a page intro, use the eyebrow and H1 and drop the rule.

**Don't** use two images or more than one link.

**Files:** `components/IntroMedia/style.css` (plus foundations; see System map for dependencies).
