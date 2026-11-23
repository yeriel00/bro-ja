# TreatmentEvidence

A text-and-statistic band on `surface-soft`: H2, body and ActionLink beside one evidence statistic inside a pair of brackets.

**Layout**

- **Wide (section 64rem and up):** text 464 | 80 gap | bracket 736 at 1440, vertically centered.
- **Narrow:** stacked, 30 → 40 gap.

**Evidence bracket**

- 3px `graphic-accent`, on both sides (left and right), open toward the inside. The Figma piece is "Evidence Panel / Paired Brackets".
- Arms top and bottom are 12px on mobile and 24px on tablet and desktop, matching the Figma frames.
- Text inset 56px (desktop/tablet) or 28px (mobile).
- The value is `display` (96/72/48, Bold, blue, -1px tracking). Under it is the `evidence-qualifier` (22/20/18 Bold navy), 26/24/24 below, with its endnote.

**ACF fields:** `heading`, `body`, `link`, `evidence_value`, `evidence_text`, `endnote`.

**Figma options** (Figma "Split Content / Evidence"; "To add" means not in the code yet)

| Figma property | Default | What it does | Code | Status |
|---|---|---|---|---|
| Show Body | On | Shows the body | `show_body` (true/false) | To add |
| Show Link | On | Shows the link | `show_link` (true/false) | To add |

**Notes**

- **Known Figma issue:** the Heading, Body, Show Body, Link Label and Show Link properties aren't connected to layers, so the pages use direct text overrides. Treat body and link as optional in code anyway.

**Don't** show more than one statistic in the bracket.

**Responsive behavior** (fluid, Nov 20)

- Spacing scales with the page: grid gap 30 → 40 and link margin 14 → 24 (reached at 768), bracket arms 12 → 24 and text inset 28 → 56 (reached at 768), column gap 40 → 80.
- The text | evidence split is a container query on the section (`container: ja-treatment`, 64rem); below it they stack. Columns are `minmax(0, …)`. No media queries.

**Files:** `components/TreatmentEvidence/style.css` (plus foundations; see System map for dependencies).
