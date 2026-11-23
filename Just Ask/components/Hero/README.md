# Hero

The campaign statement: "More than / 40 million / Americans live with migraine", the care-gap subtitle, a 100 × 3 rule and "Led by:" with the AHS logo, over the animated face grid.

**Type (hero-only styles, measured from the frames)**

| Line | Desktop | Tablet | Mobile |
|---|---|---|---|
| `hero-lead-in` | 36/44 | 28/36 | 24/32 |
| `hero-highlight`, blue | 100/112 | 76/88 | 58/68 |
| `hero-continuation` | 44/56 | 36/46 | 30/40 |
| `hero-subtitle`, SemiBold; "1 in 3" ExtraBold | 20/32 | 18/28 | 18/28 |

These sizes belong to this layout only. Don't reuse them as general headings.

**Layout** (reference values; between them everything scales, see Responsive behavior)

| | 1440 | 768 | 375 |
|---|---|---|---|
| Height | content (634) | content (~570) | 570 min |
| Text left inset | margin + 92px | margin + ~34px | margin |
| Text max width | 540 | ~397 | (column) |

**Responsive behavior** (fluid, Nov 20)

- The type scales with the foundations' hero styles; the text column is `5.4em` of the highlight size (min 21rem, so it's the full column on phones). "40 million" is 5.34em wide, so it never wraps at any width.
- Text inset beyond the margin scales 0 → 92 (`--ja-hero-inset`); top padding 56 → 89; subtitle and rule spacing ease from 19 / 21 to 15 / 16.
- Face grid pitch scales 54.67 → 60 (cells 0.8445 of the pitch), its top 27 → 48 and left −28 → 0.
- **Media queries kept:** only the veil's art direction (768, 1024), because the fade's alpha can't be interpolated in CSS. It's decorative; the text sits on at least 80% white at every width (checked 375–1600).
- **ACF limits:** keep `highlight` to about 10 characters ("40 million"), or the column will wrap it. `continuation` may wrap to two lines.

**Face grid**

- It's 24 × 9 cells:
  - 60px pitch, 50.67px cells at 1440, scaling down to 54.67 / 46 at 375 (tablet frame was 56.67 / 47.33).
- The starting arrangement is the one in `Hero/hero-face-grid.webp`, with the same people in the same cells.
- A white veil (measured gradient) keeps the text area quiet.
- `JustAsk.initFaceGrid` crossfades random visible cells: a silhouette fades in over 0.8s (`--ja-duration-fade`) and fades out more slowly, over 1.6s (`--ja-duration-silhouette-out`), swapping a face and a silhouette together every 2s (`--ja-grid-interval`): 2–4 cells on desktop, 2 on mobile.
- It pauses off-screen, when the tab is hidden, and with the pause button. It never runs under `prefers-reduced-motion`.
- The grid is `aria-hidden`.

**ACF fields**

- `lead_in`, `highlight`, `continuation`: text.
- `subtitle`: WYSIWYG (bold allowed).
- `endnote_numbers`.
- `led_by_logo`: image.
- `portraits`: repeater of `photo` + `silhouette`, square transparent PNG/WebP. The template fills the 216 cells from this list in a fixed pattern.

**Don't**

- Don't put body copy in the hero.
- Don't animate on reduced-motion.
- Don't let portrait placement imply diagnosis status.

**Files:** `components/Hero/style.css` (plus foundations; see System map for dependencies).
