## 2025-05-15 - [Semantic Button Transition]
**Learning:** Converting interactive `div` elements to semantic `button` tags improves accessibility but requires explicit CSS resets (`border: none`, `background: inherit`, `width: 100%`) and `type="button"` to avoid visual regressions and accidental form submissions.
**Action:** Always include a CSS reset block and set `type="button"` when refactoring `div` click handlers to semantic buttons.

## 2025-05-15 - [Accessible Accordion State]
**Learning:** Screen readers require the `aria-expanded` attribute to be a string ('true' or 'false') rather than a boolean. When toggling states in JavaScript, explicit string conversion or ternary operators are necessary for proper attribute updates.
**Action:** Use `element.setAttribute('aria-expanded', isExpanded ? 'true' : 'false')` for robust accessibility state management.
