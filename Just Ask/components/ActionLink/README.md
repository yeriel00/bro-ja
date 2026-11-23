# ActionLink

The underlined SemiBold text link that ends a section ("See the Question →", "Simple by Design →", "After the Yes: Guidance and Resources →").

**Use it for** moving to the page that expands a section. It is the secondary action beside a Button. Inline links inside body copy use the same colors without the arrow.

**Markup.** Keep the arrow inside the link, after a non-breaking space, so it wraps with the last word:

```html
<a class="ja-link" href="/the-ask/">See the Question&nbsp;<svg class="ja-arrow" viewBox="0 0 10.8 21.6" aria-hidden="true" focusable="false"><path d="M0.88 12.06h6.44v1.96H0.88zM4.35 17.12l2.45-4.09-2.45-4.05h2.43l2.66 4.05-2.66 4.09zM0 20.25h10.8v0.9H0z"/></svg></a>
```

**ACF fields:** `link` (link field: title, URL, target). The template appends the arrow.

**Variants**

| Class | Where | Color |
|---|---|---|
| `ja-link` | On `surface-page` | `text-link` (blue). Hover and pressed: `text-link-hover` (navy) |
| `ja-link ja-link--on-soft` | On `surface-soft` (resource cards, footer) | `text-link-on-soft` (navy). Hover: `text-muted`. Replaces blue to pass AA |
| `ja-link ja-link--inverse` | On `surface-inverse` | White in every state, white focus ring |
| `+ ja-link--strong` | CTA band "Share With a Colleague" | Bold 700, as in the frames |
| `+ ja-link--label` | Resource card and footer links, and section links such as "Browse all primary care resources" | 16/24 instead of 18/28 |

**Specs (from the frames)**

- **Text:** `link` style (18/28, SemiBold).
- **Underline:** the font's own underline (0.9px, 1.8px below the baseline at 18px).
- **Arrow:** copied from the frames' arrow, in em units, with its own underline segment.
- **Hit target:** at least 48px tall (`control-min-height`), with the text vertically centered. The focus ring (`stroke-focus`, `border-focus`) wraps the full 48px target.

**Figma options** (Figma "Button / Text Link")

| Figma property | Default | What it does | Code | Status |
|---|---|---|---|---|
| State | Default | Default / Hover / Focus / Pressed, light and inverse (Figma "Buttons / State review") | CSS states | Built, matches the frames |

**Notes**

- The Figma focus ring is a fixed-width box, wider than the text. The code keeps the ring hugging the link's 48px target on purpose.

**Don't**

- Don't drop the underline.
- Don't set links in blue on pale blue.
- Don't use the arrow on links inside body copy.

**Responsive behavior** (fluid, Nov 20)

- No media queries. The link text wraps like body text; the last word and the arrow stay together (non-breaking space before the SVG).

**Files:** `components/ActionLink/style.css` (plus foundations; see System map for dependencies).
