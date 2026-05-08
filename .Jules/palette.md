## 2025-05-15 - [Flow Visualization Accessibility]
**Learning:** Prioritize keyboard accessibility by using semantic `<button>` elements for all interactive controls (like accordion headers) and explicitly managing focus when opening new UI contexts (like side drawers).
**Action:** Always check for `div` or `span` elements used with click listeners and convert them to `<button type="button">`. Ensure `:focus-visible` styles are provided for all interactive elements.
