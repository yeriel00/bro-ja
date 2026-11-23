# ListBlock

List styles used inside TextSection and InfoCards: numbered, check, bullet, bullets in columns, and the list panel.

**Status:** in review (Nov 20). Built on the interior-page canvas; markup and options may still change before sign-off.

- **Numbered:** navy 32px circles, white numbers (14.15:1); SemiBold items. Use when the count matters.
- **Check:** a drawn blue check, not a checkbox.
- **Bullet:** 8px blue squares; **--cols** lays bullets out in up to 3 intrinsic columns with sky rules.
- **List panel:** white, 1px sky edge, radius 8, padding 24 → 32, max 720 — reads as a tool or checklist.

**Responsive behavior** (fluid): Columns are intrinsic (260px minimum).

**ACF fields:** part of the parent block: `list_style`, `items` (repeater), `in_panel`.

**Files:** `components/ListBlock/style.css` (and foundations; see System map).
