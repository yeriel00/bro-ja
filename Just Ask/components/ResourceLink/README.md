# ResourceLink

A row link to one Library resource: title, format label in its tag color, arrow in a 32px blue circle; the whole row is the link.

**Status:** in review (Nov 20). Built on the interior-page canvas; markup and options may still change before sign-off.

- White row, 1px blue edge, radius 8, min height 64; hover fills pale blue (sky on the tint) and underlines the title.
- Format label colors: `tag-quick-guide-text`, `tag-guideline`, `tag-tool`, `tag-article`, `tag-video`, `tag-podcast` (all AA on white, tint, pale blue and sky).
- **In an InfoCard footer** it becomes a bare blue (`text-link-on-tint`) link + arrow with no format label, aligned to the bottom of the row.
- For Library resources only; a link to a page is a Button.

**Responsive behavior** (fluid): A container query on the list: under 520px the format drops under the title, the arrow stays on the title line.

**ACF fields:** a relationship to a Resource post (title, format, URL come from it).

**Files:** `components/ResourceLink/style.css` (and foundations; see System map).
