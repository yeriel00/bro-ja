# StepCards

Three numbered, linked cards for the After the Yes sequence.

**Status:** in review (Nov 20). Built on the interior-page canvas; markup and options may still change before sign-off.

- Card: StepNav-style circle + time label, title `h3`, text, footer label "View Step N: …" + arrow (blue, left-aligned). 1px sky edge; hover pale blue fill, blue edge, label underlines.
- The whole card is one link (stretched title link). The footer label is visual only (`aria-hidden`), so screen readers hear the title once.

**Responsive behavior** (fluid): One column or three, never 2 + 1: switches at a 54rem content box.

**ACF fields:** `steps` (repeater: `page`, `time_label`, `text`, `link_label`), or read from the steps options repeater.

**Files:** `components/StepCards/style.css` (and foundations; see System map).
