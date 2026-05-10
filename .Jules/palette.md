## 2026-05-10 - Enhance accordion accessibility in Flow visualization

**Learning:** Converting interactive `div` elements to semantic `button` tags significantly improves keyboard accessibility and screen reader support, but requires careful CSS resets (border, width, text-align, font-family) to maintain visual consistency. Implementing the ARIA disclosure pattern (`aria-expanded`, `aria-controls`) is essential for communicating the state of collapsible components to assistive technologies.

**Action:** Always use semantic HTML for interactive elements and explicitly manage ARIA attributes when implementing custom UI components like accordions or drawers.
