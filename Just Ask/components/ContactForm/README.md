# ContactForm

The Contact page: social links beside a form with validation states.

**Status:** in review (Nov 20). Built on the interior-page canvas; markup and options may still change before sign-off.

- Fields: name, email, subject, message required; phone optional (hint in muted text). Inputs 56 tall, 1px muted-navy edge, navy on hover; focus ring 2px navy.
- **Errors:** an error summary on top (`role="alert"`, focused, items link to fields) and an inline message under each field with the "!" mark; 2px red edge and red tint. Red is used only here.
- **Social:** icon-only 48px circles, pale blue, the platform as the link's `aria-label` (placeholders until icons are supplied).
- **Pattern:** a pale-blue brain behind the form, hanging off the right; shown only when this is the last block above the footer (`ja-contact-section--last`).

**Responsive behavior** (fluid): Aside and form sit side by side from a 60rem section (container query `ja-contact`); field pairs sit side by side when each gets 256px.

**ACF fields:** `social_links` (repeater: `platform`, `url`), form via the site’s form plugin (fields above), `success_page` (Thank you).

**Files:** `components/ContactForm/style.css` plus Button (and foundations; see System map).
