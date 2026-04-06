## 2025-05-22 - Improving Accessibility in Flow Visualization
**Learning:** Using `div` elements for interactive controls like navigation buttons prevents keyboard accessibility and screen reader support. Converting them to semantic `button` elements and adding `aria-label` attributes significantly improves the user experience for all users.
**Action:** Always use semantic HTML elements (`button`, `a`) for interactive controls. Ensure icon-only buttons have descriptive `aria-label` or `title` attributes. Use `:focus-visible` to provide clear focus indicators for keyboard users.
