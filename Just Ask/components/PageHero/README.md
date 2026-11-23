# PageHero

The header of every interior page: optional eyebrow, H1, intro, and one of four layouts.

**Status:** in review (Nov 20). Built on the interior-page canvas; markup and options may still change before sign-off.

**Variants** (ACF select `variant`)

| Variant | Use | Layout |
|---|---|---|
| Simple | Resource Library, Contact, Thank you, legal, Error | Single column |
| Media | Why Ask, After the Yes | Copy left, 4:3 image right (20 corners) |
| Question | The Ask | Copy left, the clinical question in a pale-blue panel with the open bracket |
| Step | Diagnosing, Treating, Ongoing Care | Single column, linked eyebrow "After the Yes · Step N"; StepNav follows |

- **Hero quote** (optional group): a compact PullQuote under the intro, max 720 (Ongoing Care).
- **Brain pattern** (`show_pattern`, default on; off on Contact and legal pages): pale blue at 70%, tilted, hanging off the top-right; it ends inside the hero.
- Padding: 40 → 80 top, the section padding below. Eyebrow is blue `label`; H1 `h1`; intro `body`, max 720.
- No copy action in the hero: copying the question lives in the page's CtaBand.

**Responsive behavior** (fluid): Media and Question split 6/6 and 5/7 from a 54rem content box (container query `ja-content`), stacked below with the image or panel under the copy. Pattern size and offsets scale with `clamp()`.

**ACF fields:** `variant`, `eyebrow`, `eyebrow_link`, `title`, `intro`, `image` (Media), `show_pattern`, `quote` + `quote_attribution` + `quote_endnote` (optional).

**Files:** `components/PageHero/style.css` plus PullQuote (hero quote) (and foundations; see System map).
