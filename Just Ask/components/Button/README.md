# Button

The primary campaign action ("Just Ask"): a blue, 8px-radius button with a SemiBold 16/24 label. It is 160 × 56 in every mode.

**Use it for** the single most important action in a band, such as the closing CTA. Use one primary button per section; secondary actions are an [ActionLink](../ActionLink/README.md), or, in the CTA band, the secondary button below.

**Markup**

```html
<a class="ja-button" href="/the-ask/">Just Ask</a>
<!-- or <button class="ja-button" type="button">…</button> -->
```

**ACF fields:** `label` (text, short, title case) and `link` (link field: URL, target).

**Specs (from the frames)**

- **Size and label:** `min-width: 160px`, height 56 (`space-16` vertical padding + `label` 24px line), `space-24` horizontal padding for longer labels. The label is `text-on-action`, `label` style, no wrap.
- **Fill:**
  - Default: `action-primary-default`.
  - Hover: `action-primary-hover`.
  - Pressed: `action-primary-pressed`.
  - The fill transition is 250ms.
- **Focus:** `stroke-focus` ring in `border-focus`, flush to the edge (`outline-offset: 0`). Inside `.ja-on-inverse` (the navy CTA band) the ring turns `text-inverse`, so it stays visible. That is an intentional addition; the frames only show the ring on white.
- **On navy** (`.ja-on-inverse`, Figma Tone=Inverse): hover fills `sky`, pressed `pale-blue`, both with a `navy` label, so the button doesn't disappear into the band (the default hover is navy). Default look unchanged.
- **Disabled:** not designed. Don't show disabled buttons; hide the action instead.

**Secondary (`ja-button--secondary`, Figma "Button / Secondary", Tone=Inverse)**

For the navy CTA band only, beside one primary button. Same size as the primary.

```html
<a class="ja-button ja-button--secondary" href="…">Get Involved</a>
```

- Default: no fill, 2px `white` border (inset box-shadow, so it stays 56 tall), `text-inverse` label.
- Hover: fill `muted-navy`. Pressed: fill `muted-navy`, border `sky`. 250ms, color only.
- Focus: 2px `text-inverse` ring, 2px outside the border.
- Not designed for light backgrounds yet.

**Figma options** (Figma "Button / Primary")

| Figma property | Default | What it does | Code | Status |
|---|---|---|---|---|
| Width | Hug, 160 minimum | Width follows the label | `min-width: 160px` + 24px side padding | Built |
| State | Default | Default / Hover / Focus / Pressed (Figma "Buttons / State review") | CSS states | Built, matches the frames |
| Tone=Inverse (Button / Primary) | — | Hover sky / pressed pale blue, navy label, on navy | `.ja-on-inverse .ja-button` | Built (Nov 18) |
| Button / Secondary (Tone=Inverse) | — | Secondary action on navy | `ja-button--secondary` | Built (Nov 18) |

**Notes**

- Also used in FeaturedResource ("Open the Flowchart") and ContactForm ("Send Message").

**Don't**

- Don't use the button for inline navigation inside text.
- Don't put more than one primary button side by side.
- Don't change the radius or add icons.

**Responsive behavior** (fluid, Nov 20)

- No media queries. Fixed 56px height and 160px minimum width at every size; the label doesn't wrap. In a row (CtaBand) buttons wrap onto a new line when there's no room.

**Wrapping and outline variant** (Nov 20)

- Long labels wrap (`max-width: 100%`, centered) instead of overflowing a 327 column; short labels stay on one line.
- `.ja-button--outline`: white fill, 1px blue edge drawn inside, navy label (14.15:1); hover blue with a white label (4.63:1); 48 tall, no 160 minimum. For repeated actions such as ResourceCard, where a filled button on every card would shout.
- Page CTAs use the primary Button; a text link is for secondary wayfinding only.

**Files:** `components/Button/style.css` (plus foundations; see System map for dependencies).
