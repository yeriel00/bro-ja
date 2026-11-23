# TextSection

The block for prose sections: accent rule, H2, copy, and options for lists, quotes, asides, resource links and cards.

**Status:** in review (Nov 20). Built on the interior-page canvas; markup and options may still change before sign-off.

**Layout** (ACF select)

| Layout | Use |
|---|---|
| Basic | Rule, H2, prose; optional subsections, list, pull quote, resource links, resource card, closing button |
| Split | Short single-point sections on the tint: heading left (5 cols), larger lede right (7 cols), 1px sky divider; optional button or one resource link |
| Aside | Copy left (7 cols), Callout right (5 cols). The callout's top lines up with the H2 (`align aside with` = heading), or with the first subsection on a 2-up row matching resource cards below (`= first subsection`) |

- **Background** (`white` / `tint`): see the tinted section in foundations.
- **Resource cards** (`.ja-text-section__cards`): ResourceCards on CardGrid's intrinsic 2-up grid under the copy.
- **Resource links**: prose width by default; `full_width` true when the row closes a card grid.
- **Closing button**: a Button that leads to another page (title case). Resource rows are for Library resources only.
- **DataBars** can sit in the copy column (The Diagnosis Gap).

**Responsive behavior** (fluid): Aside and Split switch at a 54rem content box; below that they stack (copy, then callout). Resource cards and the subsection row use the 300px-minimum 2-up grid, so they stack together.

**ACF fields:** `layout`, `background`, `heading`, `body` (WYSIWYG), `subsections` (repeater: `heading`, `body`), `list` (ListBlock group), `quote` group, `aside_callout` (Callout), `align_aside_with`, `resource_links` (relationship to Resources) + `full_width`, `resource_cards` (relationship), `button` (link).

**Don't** put two tinted Split sections back to back unless they belong together.

**Files:** `components/TextSection/style.css` plus Button, ActionLink, Callout, PullQuote, ListBlock, ResourceLink, ResourceCard, CardGrid (grid for resource cards), DataBars (and foundations; see System map).
