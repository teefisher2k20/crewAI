## 2026-03-28 - [Flow Visualization Accessibility]
**Learning:** Icon-only navigation controls implemented as `div` elements are invisible to screen readers and inaccessible via keyboard. Converting them to semantic `button` elements with `aria-label` and `focus-visible` styles significantly improves accessibility with minimal code changes.
**Action:** Always use semantic `<button type="button">` for interactive controls and ensure `aria-label` is dynamically synchronized if the control's state (like theme) changes.
