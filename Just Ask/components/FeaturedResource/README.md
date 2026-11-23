# FeaturedResource

One highlighted Library item in a pale-blue panel: optional format tag, title, text, button, 4:3 preview image, with a white brain pattern.

**Status:** in review (Nov 20). Built on the interior-page canvas; markup and options may still change before sign-off.

- Panel radius 20, padding 24 → 48; white on the tint. Preview 360px wide on desktop, image cropped 4:3.
- Pattern: white at 75%, top-right beside the heading when stacked; bottom-left under the button when the preview sits on the right.

**Responsive behavior** (fluid): Copy and preview sit side by side from a 54rem content box; stacked below.

**ACF fields:** `resource` (relationship), `text` (override), `button_label`, `preview_image`, `show_format_tag`.

**Files:** `components/FeaturedResource/style.css` plus Button, ResourceCard (format tag) (and foundations; see System map).
