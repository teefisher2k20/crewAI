## 2025-05-22 - [Semantic Buttons for Accessibility]
**Learning:** In highly interactive visualizations (like those using Vis.js), using semantic `<button type="button">` instead of `div`s for controls is essential for keyboard accessibility. It requires CSS resets (border, background, font) to maintain visual parity but provides native focus management and screen reader support.

**Action:** Always prefer semantic `<button>` elements for any clickable UI control. Use `:focus-visible` to provide clear visual focus indicators without affecting mouse users, and manage `aria-expanded`/`aria-controls` programmatically for accordion-like structures.
