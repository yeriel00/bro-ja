# ResourceCard

A card that links to a group of After the Yes resources. It has an optional type label, an H3, an optional short description and an optional label-size link.

**Specs (from the component frames)**

- `surface-soft` with a 1px `graphic-quiet` (sky) border, `radius-md` (8) and 24px padding inside the border (content sits 25px from the outer edge, as in Figma). The border is decorative, and it keeps the card edge visible in Windows high-contrast mode.
- **Corners stay rounded.** This was decided on Nov 18, 2026. Figma updated to `Radius/MD` (8) on Nov 18.
- Optional type label `ja-resource__type ja-label` (16/24 SemiBold, `text-muted`), 16 above the title.
- Title `h3` (22/24/26, ExtraBold), description `body` in `text-muted` (#2b476b, 8.2:1 on pale blue; Jerry's Figma update, Nov 18, replaces the earlier navy decision). Gaps between all parts are 16.
- The link is `ja-link--on-soft ja-link--label` (navy, AA), **with the arrow**. This was decided Nov 18. Figma updated on Nov 18 (arrow after a non-breaking space).
- The card fills its grid cell. **Cards in a row are equal height** (decided Nov 18; Figma updated the same day: cards Fill the row height and the summary fills the spare space). The link sits at the bottom of the card. The summary takes the spare height; when the summary is hidden, the title does.

**ACF fields:** (resource post type, picked by Relationship fields) `format` (Quick Guide / Guideline / Tool / Article / Video / Podcast; drives the format tag), `patient_group` (optional; drives the group tag), `pdf_en` / `pdf_es` (files, bilingual variant), and for the hub card: `type_label` (text), `show_type_label` (true/false, default off), `title`, `description`, `show_summary` (true/false, default on), `link`, `show_link` (true/false, default on). When a toggle is off (or its field is empty), leave that element out of the markup.

**Markup**

```html
<article class="ja-resource">
  <p class="ja-resource__type ja-label">Quick Guide</p>          <!-- if show_type_label -->
  <h3 class="ja-resource__title ja-h3">Title</h3>
  <p class="ja-resource__text ja-body">Description</p>           <!-- if show_summary -->
  <a class="ja-link ja-link--on-soft ja-link--label" href="…">Link text<span class="ja-visually-hidden">: Title</span>&nbsp;<svg class="ja-arrow" aria-hidden="true" focusable="false">…</svg></a>  <!-- if show_link -->
</article>
```

**Tags** (Resource Library; Nov 19): a `ul.ja-tags` at the top of the card, in place of the type label. The format tag comes first, filled in its format color (`tag-quick-guide`, `tag-guideline`, `tag-tool`, `tag-article`, `tag-video`, `tag-podcast`) with a white 14/22 SemiBold label; the patient-group tag (if any) is white with navy text. Padding 2 / 10, `radius-sm`, 8 between tags, 16 above the title. Class: `ja-tag ja-tag--format ja-tag--{format-slug}`; an unknown format falls back to navy.

```html
<ul class="ja-tags" aria-label="Labels">
  <li class="ja-tag ja-tag--format ja-tag--quick-guide">Quick Guide</li>
  <li class="ja-tag">Pediatrics</li>
</ul>
```

**Bilingual downloads** (Resource Library; Nov 19): in place of the single link, `div.ja-resource__downloads` holds an English and a Spanish PDF link side by side (24 apart, wrapping). Both are `ja-link ja-link--on-soft ja-link--label` with `hreflang`. English is navy; Spanish is teal (`link-spanish`, 5.79:1) so color also tells them apart. Leave the Spanish link out when there's no Spanish file. Each link carries the card title in a visually hidden span.

```html
<div class="ja-resource__downloads">
  <a class="ja-link ja-link--on-soft ja-link--label" href="…" hreflang="en">English (PDF)<span class="ja-visually-hidden">: Title</span>&nbsp;<svg class="ja-arrow" …></svg></a>
  <a class="ja-link ja-link--on-soft ja-link--label" href="…" hreflang="es">Spanish (PDF)<span class="ja-visually-hidden">: Title</span>&nbsp;<svg class="ja-arrow" …></svg></a>
</div>
```

**Use** it in an intrinsic grid on the After the Yes hub (3 / 2 / 1 columns at the reference widths), gap `--ja-gap` (16 → 24), applied in ResourceCardGrid (not built yet).

**Figma options** (component properties in Figma; "To add" means not in the code yet)

| Figma property | Default | What it does | Code | Status |
|---|---|---|---|---|
| Type Label | "Quick Guide" etc. | Small label above the title (resource type) | `type_label` (text) | Built |
| Show Type Label | Off | Shows the type label | `show_type_label` (true/false) | Built |
| Show Summary | On | Shows the description | `show_summary` (true/false) | Built |
| Show Link | On | Shows the link | `show_link` (true/false) | Built |

**Notes**

- Text fills the card width.
- **Accessibility:** the link always carries the card title in a `ja-visually-hidden` span, so screen readers' link lists say "Open: How to diagnose migraine" instead of a row of "Open". The visible text still starts the accessible name (WCAG 2.5.3). The link is navy (12.3:1) with an underline; hover goes to muted navy. Type label and summary are muted navy (8.2:1). The card itself isn't a link; only the link is focusable (48px target).
- Figma writes the arrow as a "→" character; the code uses the `ja-arrow` SVG (same as ActionLink). Don't type the arrow into the ACF link text.
- Uses `:has()` so the title takes the spare height when the summary is hidden (all current browsers).
- Used inside ResourceCardGrid (Figma "After the Yes", up to 6 cards) and ResourceLibrary (with type labels and an "Open →" link).

**Responsive behavior** (fluid, Nov 20)

- No media queries. The card fills whatever column it's in. When it's built, ResourceCardGrid should use the intrinsic grid pattern (`repeat(auto-fit, minmax(min(100%, 300px), 1fr))`, gap from `--ja-gap`) instead of 3 / 2 / 1 columns per width.

**Outline button action** (Nov 20)

- The card's action is an outline Button (`ja-button ja-button--outline ja-resource__action`), 24 below the summary. Its label follows the format: View Guide, Read Guideline, Open Tool, Read Article, Watch Video, Listen. Keep the title in a visually hidden span for a unique accessible name.
- The same card renders every Library item wherever it appears (Resource Library, step pages, After the Yes): pick the Resource post with a relationship field; never retype it.
- Needs Button styles.

**Files:** `components/ResourceCard/style.css` (plus foundations; see System map for dependencies).
