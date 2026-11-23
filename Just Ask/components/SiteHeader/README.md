# SiteHeader

The campaign header: the Just Ask. logo on the left and the primary navigation on the right.

**Behaviour**

- **Every mode:** a 1px sky (`graphic-quiet`) bottom border (added below 1024px on Nov 18).
- **From 1024px:** four SemiBold links, 24px apart, never wrapping. The bar is 86px tall plus the border at 1440, and the logo 190px wide (both scale; see Responsive behavior).
- **Below 1024px:** "Menu" plus an 18 × 14 burger icon. The bar is 80px tall plus the border at 375, and the logo 160px wide. The toggle opens the full-height menu panel (below).
- **Open menu behaviour** (`bundle.js` → `JustAsk.initHeader`):
  - The panel fills the screen below the header bar and slides in from the right (the Menu button's side), 300ms. No slide with `prefers-reduced-motion`.
  - Page scroll is locked while it's open (`overflow: hidden` on `<html>`, plus a `ja-menu-open` class).
  - Tab cycles through the header only (logo, Close, menu links). Escape closes it and returns focus to the toggle.
  - Widening to 1024px or more closes it.

**Open menu (Figma "Navigation Panel")**

- Built to the Figma panel (audit E1, Nov 18):
  - Links in `text-link` (blue), each followed by the arrow (the ActionLink arrow without its underline segment, since these links aren't underlined). Hover/press: `text-link-hover` (navy).
  - 48px targets, 8px apart (56px pitch, the same as Figma's 24px labels with a 32 gap).
  - Block padding 12 (mobile) / 28 (tablet), so the text sits 24 / 40 from the panel edges, as in Figma.
  - Text inset 24 (mobile) / 40 (tablet), from `ja-container`.
- **Current page** (`aria-current="page"`): navy with a 1px underline (offset 4), so it doesn't rely on color alone and looks different from hover.
- The panel has **no border**; the header bar's bottom border separates them. Figma's Navigation Panel Mobile/Tablet frames are full height (375 × 731, 768 × 943: an 812 / 1024 screen minus the 81px header).
- **Markup:** the arrow is an inline SVG after the label text (no `&nbsp;`; the link is a flex row, so the arrow can't wrap away). In WordPress, add it with a nav-menu walker or `nav_menu_item_title` filter, **not** by typing "→" into menu labels (Montserrat has no →, and screen readers would read it).
- The desktop variant of the panel isn't used, because desktop shows the full nav.

**ACF / WordPress:** a WordPress menu location (`primary`), with the current page marked `aria-current="page"` (shown in `text-link`). The logo is fixed and isn't a field.

**Figma options:**

| Figma property | Default | What it does | Code field | Status |
|---|---|---|---|---|
| Site Header → Breakpoint | Mobile | Mobile / Tablet / Desktop variants | — (CSS modes) | Built |
| Navigation Panel → Breakpoint | Mobile | Mobile / Tablet / Desktop variants (Desktop unused) | — (CSS modes) | Built |
| Navigation Panel → Why Ask / The Ask / After the Yes / Resource Library | "… →" | Editable link labels | WordPress menu `primary` (labels without the arrow) | Built |

"Button / Menu" is the toggle; it has no options.

**Don't**

- Don't add a fifth top-level link without checking that the row still fits at 1024px.
- Don't change the logo color version on white.

**Responsive behavior** (fluid, Nov 20)

- Bar height 80 → 86 and logo 160 → 190 scale with the page; the menu panel's block padding grows 12 → 28 by 768.
- **Media query kept (the system's one layout breakpoint):** full nav from 1024 (`breakpoint-desktop`), Menu toggle below. The four links need ~560px plus the logo on one line; below 1024 they'd wrap.
- **Content limit:** four top-level links. A fifth needs a check that the row still fits at 1024.

**Files:** `components/SiteHeader/style.css` (plus foundations; see System map for dependencies).
