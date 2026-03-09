## 2025-05-15 - [Improving Accessibility in Flow Visualization]
**Learning:** In complex interactive components like the Flow visualization, using semantic buttons instead of divs for navigation and controls is crucial for screen reader support. Dynamic components like accordions also need explicit state management via `aria-expanded` to be fully accessible.
**Action:** Always prefer `<button type="button">` for interactive elements and use `focus-visible` for keyboard-friendly focus indicators that don't clutter the mouse experience.
