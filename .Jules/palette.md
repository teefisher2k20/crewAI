
## 2025-05-14 - [Semantic Accordion Headers for Flow Visualization]
**Learning:** Using semantic `<button>` elements for accordion headers, rather than `<div>`s, is essential for keyboard accessibility (Tab focus and Space/Enter interaction) and screen reader support (via `aria-expanded`). CSS resets like `border: none`, `font-family: inherit`, and `width: 100%` are necessary to maintain the original design when switching to button tags.
**Action:** Always prefer semantic interactive tags (like `<button>`) over generic `<div>`s for clickable UI components, and remember to reset their default browser styles.
