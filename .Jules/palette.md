## 2025-05-15 - Semantic Buttons and Focus Management in Hybrid Canvas UIs
**Learning:** In applications where the primary interaction is on a `<canvas>` (like Vis.js networks), secondary UI elements like navigation bars and side drawers are often implemented with `div` tags for styling ease, which breaks keyboard accessibility. Converting these to semantic `<button>` elements requires careful CSS resets (padding, font-family, border) to preserve the original design while gaining native focus management and screen reader support.
**Action:** Always check if interactive "clickable" elements are semantic `<button>` or `<a>` tags. Use `:focus-visible` with a high-contrast outline (like `CREWAI_ORANGE`) to provide clear visual feedback for keyboard users without affecting mouse users.

## 2025-05-16 - Focus Management for Side Drawers
**Learning:** When using side drawers in a complex visualization, it's essential to manage focus to prevent keyboard users from losing their place. Saving the triggering element and restoring focus upon closure, combined with focusing the close button on open, creates a seamless experience for assistive technologies.
**Action:** Implement `lastFocusedElement` tracking in drawer managers. Use `setTimeout` with the animation duration to ensure focus is moved only after the element is visible and reachable.
