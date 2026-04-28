## 2025-05-15 - Interactive Flow Accessibility
**Learning:** The Flow visualization used non-semantic `div` elements for navigation and lacked proper keyboard focus indicators, making it inaccessible to screen readers and keyboard-only users. Additionally, icon-only buttons lacked ARIA labels.
**Action:** Always use semantic `<button type="button">` for interactive elements, provide descriptive `aria-label` attributes for icon-only controls, and implement clear `:focus-visible` styles using theme-consistent colors.
