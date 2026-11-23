# PartnerAttribution

The partner section ("Developed with clinicians who see patients every day"): a centered introduction (H2, body, link), then one centered row of partner logos.

**Introduction**

- Stacked and centered at every size: H2 → body (32) → link (24). No accent rule. Max 720 wide on desktop (`prose-max-desktop`), centered in the section; and at every width (narrower containers cap it).
- Optional: see Show Introduction below.

**Logos**

- One centered, wrapping row. No tile, border or background behind real logos: the logo itself is the shape.
- Every logo is the same height, **56px** at 768 and up, **40px** below, with its natural width (capped at 200px; `object-fit: contain`).
- Gaps: 32 between logos (16 below 768), 24 between lines. With the placeholders: all 7 on one line at 1440, 5 + 2 at 1024, 4 + 3 at 768, 3 + 3 + 1 at 375. Real logos wrap by their own widths.
- Space above the row: 64 on desktop, 40 on tablet and mobile (measured to the link text).

**Placeholders:** until the partner logos arrive, each item shows a pale-blue block (`surface-soft`, `radius-md`) labeled "Logo N" in `small`, `text-muted`: 144 × 56 at 768 and up, 96 × 40 below (Figma "Partner Logo / Placeholder", `105:179`). It stands in for the artwork, not a container for it.

```html
<li class="ja-partner"><span class="ja-partner__placeholder ja-small">Logo 1</span></li>
<!-- real logo -->
<li class="ja-partner"><a href="https://…"><img src="…/logo.svg" alt="Partner name"></a></li>
```

**Show Introduction off** (e.g. under a page intro): leave out `.ja-partners__head` entirely. The logo list becomes the first child of `.ja-container` and its top margin drops to 0, and the section padding tightens to **24** on mobile and tablet and **40** on desktop (instead of 24 / 40 / 80), so the row sits as a band under a page header. This is automatic (CSS checks for the missing introduction); no extra field. The section has no heading then, so swap `aria-labelledby` for `aria-label="Partner organizations"`:

```html
<section class="ja-section ja-partners" aria-label="Partner organizations">
  <div class="ja-container">
    <ul class="ja-partners__logos" aria-label="Partner organizations">…</ul>
  </div>
</section>
```

**ACF fields:** `show_introduction` (true/false, default on), `heading`, `body`, `link`, and a `partners` repeater of `logo` (SVG/PNG, transparent), `name` (used as alt text) and an optional `url` (wraps the logo in a link).

**Figma options** (Figma "Partner Collection", `20:38`)

| Figma property | Default | What it does | Code | Status |
|---|---|---|---|---|
| Show Introduction | On | Off shows the logo row by itself (no heading, body or link) | `show_introduction` (true/false) | Built (Nov 18) |
| Show Logo 1–7 | On | Hides that logo | `partners` repeater (one row per logo) | Built (the repeater count) |
| Logo 1–7 (instance swap) | Placeholder | Swaps in the partner's logo | `partners` → `logo` | Built |

**Notes**

- Nov 18 redesign: the intro is centered with no accent rule (Jerry, same day). Before, it had the rule and was a split row on desktop (560 | 656, bottom-aligned) and the logos sat in bordered 110px tiles, 4 / 3 / 2 per line. Both replaced at Jerry's request.
- Section heights with placeholders: 564 at 1440, 532 at 768, 644 at 375 (same as Figma).
- Nov 19: tighter padding with Show Introduction off (24 / 24 / 40), from the interior-page boards (Jerry).

**Logo prep:** trim to the artwork (no padding in the file), transparent background, single color or the partner's official colors. Very wide logos (wider than about 3.5 : 1) hit the 200px cap and display shorter than 56px.

**Responsive behavior** (fluid, Nov 20)

- No media queries. Logo height 40 → 56, placeholder width 96 → 144 and the link margin 14 → 24 reach their tablet values at 768; logo gap 16 → 32 and the row's top margin 30 → 64 scale to 1440. The intro is capped at 720 (`prose-max-desktop`) at every width.
- The logo row wraps on its own (flex-wrap), centered.
- Logos-only padding 24 → 40.

**Files:** `components/PartnerAttribution/style.css` (plus foundations; see System map for dependencies).
