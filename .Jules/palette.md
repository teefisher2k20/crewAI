## 2025-05-22 - Semantic HTML for Interactive Overlays
**Learning:** Interactive controls implemented as `div` elements in overlays (like navigation buttons and accordion headers) are invisible to screen readers and lack keyboard support. Converting them to semantic `button` elements with `aria-label` and `aria-expanded` significantly improves accessibility without changing visual design.
**Action:** Always use `<button type="button">` for custom interactive controls instead of clickable `div`s, and ensure focus styles are preserved using `:focus-visible`.
