# SiteFooter

The campaign footer on `surface-soft`: logo, utility links, copyright and legal links.

**Layout**

Reference widths (values scale between them; see Responsive behavior):

- **Desktop:** two rows. Logo (190px) and links (16px SemiBold, 24px apart) on the first; copyright (`small`, muted) and legal links on the second. Padding 48.
- **Tablet:** logo 190px (was 160); links wrap in rows 16px apart; padding 48 / 40.
- **Mobile:** logo 190px; links stacked as 48px targets; padding 32.

**Links:** links on pale blue use `text-link-on-soft` (navy) for AA, with `text-muted` + underline on hover. This was changed from the frames' blue on purpose. Figma updated on Nov 18: footer links (nav and legal) use the new `Text/Link-On-Soft` variable (navy).

**ACF / WordPress:** a `footer` menu location, a `legal` menu location, and the copyright year from PHP `date('Y')`.

**Figma options:** none (Figma "Site Footer" has Mobile / Tablet / Desktop variants only). Frames checked Nov 18, 2026: they match, apart from the link color above.

**Responsive behavior** (fluid, Nov 20)

- The footer responds to its own width (`container: ja-footer`), not the viewport. No media queries.
- Narrow: everything stacked, links as a column of 48px targets. From 40rem: links in a wrapping row (16 between lines). From 56rem: copyright | legal on one row. From 64rem: logo | nav on one row (the nav may wrap beside the logo, as it did at 1024 before).
- Padding 32 → 48 and the top-to-bottom gap 10 → 24 scale with the page. Logo 190 at every width (tablet was 160).

**Files:** `components/SiteFooter/style.css` (plus foundations; see System map for dependencies).
