## 2025-05-14 - [A11y] Semantic Buttons and Keyboard Focus
**Learning:** Using `div` elements for interactive controls prevents screen readers from identifying them as buttons and breaks default keyboard navigation. Converting them to semantic `button` elements and adding `:focus-visible` styles significantly improves accessibility with minimal CSS overhead.
**Action:** Always use `<button type="button">` for custom UI controls and ensure every icon-only button has an `aria-label`.
