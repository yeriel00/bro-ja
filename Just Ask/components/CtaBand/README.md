# CtaBand

The closing (or mid-page) campaign band on `surface-inverse`: a centered `cta` statement with lead words in `sky`, an optional question in `sky`, an optional body line, then the actions. The actions are a centered row of a primary Button and an optional secondary Button, with the share ActionLink centered underneath.

**Layout**

| | Desktop | Tablet | Mobile |
|---|---|---|---|
| Padding (top/bottom) | 96, band hugs its content | 64 | 48 |
| Content width | max 1020, centered | full (688 at 768) | full |
| Gap between statement / question / body | 24 | 24 | 24 |
| Text → actions | 48 | 48 | 32 |
| Button → button | 16, side by side | 16 | 16; the row wraps, so two buttons stack below about 360 |
| Buttons → share link | 16 (link centered under the buttons) | 16 | 16 |

- Heights (Figma = code): homepage default 564 / 464 / 458 at 1440 / 768 / 375. Why Ask (body + secondary) 508 at 1440. The Ask (question + body, copy button, no share link) 556 at 1440. After the Yes (body) 480.
- The share link hugs its text (no fixed box), so the actions stay centered.
- **Pattern:** one top-view brain (`brain-illustration-top.svg`) on each edge in `muted-navy` at 60%: the left edge at `left: 0`, the right edge at `right: 0`, 120% of the band height (128% on desktop). A navy gradient overlay runs from 0% at each edge to 100% toward the center (solid 34–66% of the width, 28–72% on desktop), so the outer half of each brain shows and the text always sits on solid navy.
  - The pattern shows at every width, mobile included (decided Nov 18, 2026).
- **Focus:** rings are white inside this band (`.ja-on-inverse`). The secondary button's ring sits 2px outside its white border.

**Markup**

```html
<section class="ja-cta ja-on-inverse" aria-labelledby="ja-cta-title">
  <span class="ja-pattern ja-pattern--l" aria-hidden="true" style="--ja-pattern-url:url('…/brain-illustration-top.svg')"></span>
  <span class="ja-pattern ja-pattern--r" aria-hidden="true" style="--ja-pattern-url:url('…/brain-illustration-top.svg')"></span>
  <div class="ja-container">
    <div class="ja-cta__content">
      <h2 class="ja-cta__text ja-cta-text" id="ja-cta-title"><span class="ja-hl--sky">One question,</span> asked of every patient, can bring migraine into the open.</h2>
      <!-- show_question --><p class="ja-cta__question ja-question">“In the past month, has a headache interfered with your work, school, family, or other activities?”</p>
      <!-- show_body --><p class="ja-cta__body ja-body">…</p>
      <div class="ja-cta__actions">
        <div class="ja-cta__buttons">
          <!-- button_action = link -->
          <a class="ja-button" href="/the-ask/">Just Ask</a>
          <!-- button_action = copy_question (instead of the link above) -->
          <button class="ja-button" type="button" data-ja-copy hidden><span class="ja-copy-label">Copy the Question</span></button>
          <!-- show_secondary_button --><a class="ja-button ja-button--secondary" href="…">Get Involved</a>
        </div>
        <!-- show_share_link --><a class="ja-link ja-link--inverse ja-link--strong" href="#share">Share With a Colleague&nbsp;<svg class="ja-arrow" …></svg></a>
      </div>
    </div>
    <!-- copy mode only --><p class="ja-copy-status ja-visually-hidden" role="status"></p>
  </div>
</section>
```

Leave out any part whose toggle is off; the flex gaps leave no extra space.

**ACF fields**

| Field | Type | Default | Notes |
|---|---|---|---|
| `headline` + `headline_highlight` | text | — | Statement; the highlight words are wrapped in `ja-hl--sky` |
| `question` + `show_question` | text, true/false | off | Sky, `ja-question`. Include the curly quotes |
| `body` + `show_body` | text, true/false | off | `ja-body` |
| `button_action` | select: `link` / `copy_question` | `link` | `copy_question` outputs the `<button data-ja-copy hidden>` and the status line; `bundle.js` shows it only when the browser can copy and copies the band's question (without quote marks), so use it with `show_question` on |
| `button` | link | Just Ask | Label + URL (link mode); in copy mode only the label is used |
| `secondary_button` + `show_secondary_button` | link, true/false | off | `ja-button ja-button--secondary` |
| `share_label`, `share_url` + `show_share_link` | text, url, true/false | on | Or a share handler |

**Figma options** (Figma "CTA Band / Centered", `105:237`)

| Figma property | Default | What it does | Code | Status |
|---|---|---|---|---|
| Statement | homepage line | The headline | `headline` (+ `headline_highlight`) | Built |
| Question + Show Question | Off | The campaign question in sky (e.g. The Ask) | `question`, `show_question` | Built |
| Body + Show Body | Off | Body line under the statement/question | `body`, `show_body` | Built |
| Show Secondary Button | Off | Second button beside the primary (Figma "Button / Secondary", default "Get Involved") | `secondary_button`, `show_secondary_button` | Built |
| Show Share Link | On | The share link under the buttons | `show_share_link` | Built |
| Primary button label (exposed instance) | Just Ask | "Copy the Question" on The Ask | `button`, `button_action` | Built |

**Notes**

- Button sets: 1 button; 1 button + share link (homepage); 2 buttons + share link (Why Ask); copy button only (The Ask).
- Labels for the buttons and the share link are edited through the exposed nested instances in Figma (the old Heading, Button Label and Link Label properties were unconnected and were removed Nov 18).
- Copy button: Figma's Primary has 16px side padding (186 wide on The Ask); code uses the standard Button (24 sides, 201 wide). Same open item as ClinicalQuestion.
- If the browser can't copy, the copy button stays hidden; on The Ask the band then has no button (the same question is in the ClinicalQuestion panel above).

**Responsive behavior** (fluid, Nov 20)

- Band padding 48 → 96 and the text-to-actions gap 32 → 48 (reached at 768) scale with the page. Buttons wrap when the row runs out of room.
- **Media query kept (art direction only):** at 1024 the brain pattern grows from 120% to 128% of the band height and the edge fade narrows (34/66% → 28/72%). It's decorative and doesn't affect layout.

**Files:** `components/CtaBand/style.css` (plus foundations, `components/Button/style.css`, `components/ActionLink/style.css`, and `components/bundle.js` for copy mode).
