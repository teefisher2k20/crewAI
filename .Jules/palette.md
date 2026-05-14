## 2024-05-14 - Semantic Accessibility in Visualization Tools
**Learning:** Visualization tools often use generic `div` elements for complex interactive components, which are inaccessible to screen readers and keyboard users. Converting these to semantic `button` elements requires careful CSS resets (border, background, font-family) to maintain the original design.
**Action:** Use `button` with `type="button"` for all interactive elements and provide explicit `:focus-visible` styles to ensure keyboard accessibility without affecting the visual design for mouse users.
