# QuoteBand

A clinician quote in a pale-blue card over the consultation photo.

**Layout**

- **Wide (band 64rem and up):** a full-bleed 560px band. The photo is `cover`, with a white fade from 100% on the left to 0% on the right. The 560px card is vertically centered at the content edge: `radius-media`, a 1px `graphic-quiet` (sky) stroke like ResourceCard (Nov 19; decorative, and it keeps the card edge visible over the photo and in high-contrast mode), padding 40 inside the stroke. Inside it is the PullQuote treatment: a 64px ExtraBold `graphic-accent` quote mark in a 36px-tall box, the `quotation` text (34/44 ExtraBold) right below it, then a `label` attribution in `text-muted` 16px below, with endnote. **No side bar** (removed Nov 19 to match the interior-page PullQuote).
- **Narrow (overlap, Nov 19):** the photo runs full-bleed, 320 → 420 tall, cropped at 78% horizontally so the clinician's face stays clear, and fades from clear (at half height) to white at the bottom. The card rides up over the faded part (160 / 112 overlap), keeps 24 / 40 side margins from the content edge, max 560 wide on tablet, padding 40 / 24, then 24 below. Band height with the homepage quote: 562 at 768, 494 at 375 (desktop 560, unchanged). Replaces the stacked layout (photo above, no fade), which lost the card-on-photo feel and cropped the clinician out.

**ACF fields:** `quote` (text, without quote marks: the large blue mark is the only quote mark, as in PullQuote; `<blockquote>` tells screen readers it is a quote), `attribution`, `endnote`, `image`.

**Figma options:** none (Figma "Boxed Full" has Mobile / Tablet / Desktop variants only). Frames checked Nov 18, 2026: they match.

**Notes**

- One quote style across the site (decided Nov 19, from the interior-page canvas): QuoteBand and the inline PullQuote share the mark, quotation and muted attribution, and neither has a side bar. PullQuote (inline in text sections and cards, with a compact size) is on the interior-page canvas and replaces the planned navy-bar "Blockquote". Figma's quote frames still show the bar; update them to match.
- Muted attribution on pale blue: 8.22:1.

**Don't**

- Don't use more than about 25 words.
- Don't attribute a quote to a named person without consent; use a role ("Clinician, AHS Study").

**Responsive behavior** (fluid, Nov 20)

- The band responds to its own width (`container: ja-quote`). No media queries.
- Narrow (overlap): photo height 320 → 420 and the card's overlap 112 → 160 scale up to 768, then hold; card padding 24 → 40; card max 560.
- From 64rem: the photo fills the band behind the card with the left-to-right fade; the card is 560 wide, vertically centered, 560 min band height.
- **Content limit:** quote under ~120 characters so the card stays inside the 560 band.

**White card option** (Nov 20)

- `card_color` (pale blue default / white): `ja-quote--white` gives the card a white fill, same sky edge and padding, so the band doesn't run into pale-blue panels right above it (Why Ask, The Ask). Default unchanged.

**Files:** `components/QuoteBand/style.css` (plus foundations; see System map for dependencies).
