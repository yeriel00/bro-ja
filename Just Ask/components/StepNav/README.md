# StepNav

A three-step stepper placed right after the PageHero on the step pages: numbered circles joined by a 2px sky line; the current step is filled blue.

**Status:** in review (Nov 20). Built on the interior-page canvas; markup and options may still change before sign-off.

- Circle 40px, 2px sky ring, muted number; current step: blue fill, white number (4.63:1). Name 16/24 Bold under it.
- "Step N" is in the markup for screen readers but visually hidden; the circle's number is CSS-generated and hidden from assistive tech.
- No padding of its own above (the hero's bottom padding sits there); 24 → 40 below. When the next block changes ground (tint, navy, photo), it gets the section gap in white first.

**Responsive behavior** (fluid): Three equal columns at every width; the gap shrinks 24 → 12. Names wrap under their circle.

**ACF fields:** none on the block. Steps come from an options-page repeater (`steps`: page link + short name); the current step is the one whose page is being viewed (`aria-current="page"`). The same repeater drives PageNav.

**Files:** `components/StepNav/style.css` (and foundations; see System map).
