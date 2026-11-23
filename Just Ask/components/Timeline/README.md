# Timeline

Ordered checkpoints as cards with a blue chevron to the next one (When to Check In).

**Status:** in review (Nov 20). Built on the interior-page canvas; markup and options may still change before sign-off.

- Card: clinical-tint fill (white on the tint), H3 + SemiBold timing line. Chevron 12px, `stroke-thin-accent`, in the gap.
- No circles or connecting line, so it never echoes the StepNav above it. Optional note under the cards.

**Responsive behavior** (fluid): Three across from a 54rem content box (chevrons point right); stacked below (chevrons point down).

**ACF fields:** `checkpoints` (repeater: `title`, `text`), `note`.

**Files:** `components/Timeline/style.css` (and foundations; see System map).
