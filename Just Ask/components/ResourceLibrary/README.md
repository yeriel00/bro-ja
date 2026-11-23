# ResourceLibrary

The Resource Library template: three filters, a live results count, results grouped under headings, and an empty state.

**Status:** in review (Nov 20). Built on the interior-page canvas; markup and options may still change before sign-off.

- **Filters:** native selects (step in care, patient group, format), 200px minimum, 3 across when they fit. Active select: 2px navy edge, SemiBold value.
- **Results bar:** count (`aria-live="polite"`) and a "Clear filters" text button once any filter is on.
- **Groups:** `h3` heading + count, sky rule, then a 1 → 2 → 3 column grid of ResourceCards (outline button actions).
- **Empty state:** pale-blue panel with the small blue brain mark, a message and Clear filters.
- Filters should be reflected in the URL so other pages can link to a pre-filtered view.

**Responsive behavior** (fluid): Selects and grids are intrinsic; the results bar wraps.

**ACF fields:** Resource post type: `title`, `summary` (≤100 characters), `format` (taxonomy), `step` (taxonomy), `patient_group` (taxonomy), `file` or `url`, `spanish_file` (optional). Page: `intro`.

**Files:** `components/ResourceLibrary/style.css` plus ResourceCard, Button (and foundations; see System map).
