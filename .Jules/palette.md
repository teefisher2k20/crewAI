## 2025-05-15 - Semantic Accordion Headers
**Learning:** Using `div` elements for interactive toggles like accordion headers breaks keyboard navigation and screen reader support. Converting them to semantic `<button type="button">` elements with `aria-expanded` and `aria-controls` attributes immediately improves accessibility by making the control focusable and providing state feedback.
**Action:** Always implement interactive toggles using `<button type="button">` and explicitly manage ARIA states (`aria-expanded`) in the interaction logic.
