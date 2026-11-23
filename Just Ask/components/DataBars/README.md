# DataBars

Proportional horizontal bars against a 100% track, with the value as text (The Diagnosis Gap).

**Status:** in review (Nov 20). Built on the interior-page canvas; markup and options may still change before sign-off.

- Label `body` SemiBold, value blue at the question size; track pale blue (white on the tint), fill blue, height 20 → 24.
- Bars are decorative (`aria-hidden`); the values are text, so it reads correctly without them. Optional small caption.

**Responsive behavior** (fluid): Bars fill their column; nothing switches.

**ACF fields:** `bars` (repeater: `label`, `value` 0–100, `endnote`), `caption`.

**Files:** `components/DataBars/style.css` (and foundations; see System map).
