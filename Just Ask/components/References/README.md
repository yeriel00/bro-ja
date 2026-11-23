# References

A numbered reference list for the page's endnotes: H2, a `small` muted note, then an `ol` in `small` with navy SemiBold numbers and a 44px hanging indent.

**Background** (Nov 19): the section sits on `surface-statistic` (clinical tint, #f5fafd), full width, so the end matter reads as its own section between the page content (or the navy CTA band) and the pale-blue footer. Numbers are navy, not blue: blue on the tint is 4.4:1, under AA for 14px text. Text: navy 13.46:1, muted note 9.01:1.

**Spacing**

| | 1440 | 768 | 375 |
|---|---|---|---|
| Section padding | 48 | 45 | 24 |
| H2 → note | 12 | ~9.5 | 8 |
| Note → list | 12 | ~9.5 | 8 |

**Responsive behavior** (fluid, Nov 20): no media queries. Padding is `min(var(--ja-section), 48px)` (follows the section padding, capped at 48 so the end matter stays compact); the 8 → 12 gaps scale with `clamp()`.

Items are 8px apart.

**Linking:** each item carries `id="ref-N"`, and every `ja-sup` endnote links to it.

**ACF fields:** `note`, and a `references` repeater of `citation` (WYSIWYG) and `pending` (true/false, which prefixes "Citation pending —").

**Figma options** (Figma "References")

| Figma property | Default | What it does | Code | Status |
|---|---|---|---|---|
| Show Reference 1–20 | Rows 1–11 on, 12–20 off (Desktop) | Shows each reference row | The `references` repeater (any count) | Built |

**Notes**

- Endnote numbers in Figma are placeholders, numbered per page; most references are still "Citation pending".

**Don't** reorder the references without renumbering the page's endnotes.

**Files:** `components/References/style.css` (plus foundations; see System map for dependencies).
