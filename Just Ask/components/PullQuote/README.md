# PullQuote

A clinician quote with a blue quote mark and an attribution carrying its endnote.

**Status:** in review (Nov 20). Built on the interior-page canvas; markup and options may still change before sign-off.

- **Compact** (`--compact`): quote in bold `body`, attribution 14/22 muted. Used in InfoCards, TextSection copy and the hero quote.
- **Finding** (`--finding`): `evidence-qualifier` quote paired with a finding row in StatisticGrid findings.
- Default (quotation style) is kept for long standalone quotes.

**Responsive behavior** (fluid): Wraps to its column; no layout changes.

**ACF fields:** `quote`, `attribution`, `endnote`.

**Files:** `components/PullQuote/style.css` (and foundations; see System map).
