# CardGrid

A grid of InfoCards under an accent rule, H2 and optional intro, with an optional closing button or closing pair.

**Status:** in review (Nov 20). Built on the interior-page canvas; markup and options may still change before sign-off.

- **Max columns** (2 / 3 / 4) is a cap: the grid fits as many 300px columns as it can up to that cap (1 at 375, 2 at 768, the cap at 1440).
- **InfoCard:** clinical-tint fill (white on the tint), 40 × 2 blue marker above the H3, padding 24 → 32. Options: compact PullQuote, bullet list, footer link (ResourceLink card form), **inverse** (navy, white text, sky marker) for the one card to see first.
- **Closing pair** (optional): a Callout left and a ResourceCard right on the cards' columns (Check for Red Flags, Match Acute Treatment to Severity).
- **Closing button:** Button to another page.

**Responsive behavior** (fluid): Intrinsic grid (300px minimum, capped); the pair uses the same 2-up grid, so it stacks at the same width as the cards.

**ACF fields:** `heading`, `intro`, `max_columns`, `background`, `cards` (repeater: `title`, `text`, `list`, `quote` group, `footer_resource` relationship or `footer_link`, `inverse`), `closing_callout`, `closing_resource` (relationship), `button`.

**Files:** `components/CardGrid/style.css` plus Button, ResourceLink, Callout, PullQuote, ListBlock, ResourceCard (when those options are used) (and foundations; see System map).
