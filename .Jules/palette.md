## 2025-05-15 - Standardizing Semantic Buttons for Accessibility
**Learning:** Converting non-semantic interactive elements (like `div` or `span` used as triggers) to `<button>` tags requires explicit CSS resets (`background: none`, `border: none`, `padding: 0`) and `width: 100%` for block-level triggers to maintain original layout while gaining keyboard accessibility and screen reader support.
**Action:** Always apply a base reset class or explicit styles when switching to semantic buttons in an existing design system to prevent browser-default styles from breaking the layout.
