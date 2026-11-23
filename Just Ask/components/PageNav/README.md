# PageNav

End-of-page wayfinding on the step pages: a back card, the next-step card, and a "Browse the Resource Library" text link.

**Status:** in review (Nov 20). Built on the interior-page canvas; markup and options may still change before sign-off.

- Cards: pale blue, radius 8, min height 88, kicker 14/22 muted ("Back: Step 1", "Next: Step 3") over a title-case `h3` title; hover sky. Back card: arrow first, pointing left.
- Right side: the next card with the Library link right-aligned under it. The last step has no next card, so only the link sits on the right.
- 1px sky rule above, 32 gap.

**Responsive behavior** (fluid): Under a 40rem content box everything stacks full width: back, next, link.

**ACF fields:** none on the page. Back/next come from the steps options repeater; the Library link is a global setting.

**Files:** `components/PageNav/style.css` plus ActionLink (and foundations; see System map).
