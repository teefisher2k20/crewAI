## 2026-04-19 - [Accessible Flow Visualization Controls]
**Learning:** When converting `div`-based icons to semantic `button` elements, it is crucial to explicitly reset browser defaults like `padding: 0`, `border: none`, and `font-family: inherit` to maintain visual consistency while gaining accessibility and keyboard focus support.
**Action:** Always check for existing `:focus-visible` patterns and use CSS resets when migrating non-semantic elements to semantic ones to ensure they behave predictably across different browsers and assistive technologies.
