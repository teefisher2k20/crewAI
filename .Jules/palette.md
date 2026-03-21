## 2025-05-15 - [Semantic Buttons for Navigation]
**Learning:** Using semantic `<button>` elements instead of generic `<div>`s for interactive controls like navigation buttons ensures they are keyboard-accessible by default and correctly identified by screen readers.
**Action:** Always implement interactive UI elements using semantic HTML tags (`<button>`, `<a>`) and provide descriptive `aria-label` attributes for icon-only controls.

## 2025-05-15 - [Focus Indicators for Custom UI]
**Learning:** Custom UI elements often lose default focus indicators. Explicitly defining `:focus-visible` styles using the design system's primary color (e.g., `var(--edge-router-color)`) provides essential visual feedback for keyboard users.
**Action:** Include `:focus-visible` styles for all custom interactive elements to maintain high accessibility standards.
