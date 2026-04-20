## 2025-03-07 - [Flow Visualization Accessibility]
**Learning:** Interactive elements implemented as `div` tags lack semantic meaning for screen readers and are not keyboard-focusable by default. Converting them to `<button type="button">` and adding `aria-label` provides an immediate accessibility win without changing the visual design, provided that browser-default button styles (padding, border, font) are reset in CSS.
**Action:** Always prefer semantic `<button>` elements for interactive controls and ensure `:focus-visible` styles are implemented to support keyboard navigation.
