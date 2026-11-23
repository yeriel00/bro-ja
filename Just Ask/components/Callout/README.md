# Callout

A titled tip or note marked by closed brackets on both sides ([ … ]), with no fill, so it never reads as a card.

**Status:** in review (Nov 20). Built on the interior-page canvas; markup and options may still change before sign-off.

- Title `h3`, text `body` 12 below; optional ActionLink. Brackets: 14px wide, `stroke-thin-accent` blue, padding 32 inside them.
- Used as a TextSection aside and as the left half of the CardGrid closing pair. The callout fills its column, so the right bracket sits on a fixed edge.
- The open left-only bracket stays the clinical question's signature; callouts always close.

**Responsive behavior** (fluid): Fills its column at every width.

**ACF fields:** `title`, `text`, `link` (optional).

**Files:** `components/Callout/style.css` plus ActionLink (optional link) (and foundations; see System map).
