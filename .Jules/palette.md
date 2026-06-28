## 2025-05-15 - [Flow Visualization Accessibility]
**Learning:** Interactive elements implemented as `div` tags lack keyboard accessibility and standard button behaviors. Converting them to `<button type="button">` with CSS resets (`padding: 0`, `font: inherit`) preserves layout while enabling tab access.
**Action:** Always use semantic `<button>` for interactive controls and provide `:focus-visible` states using brand colors for clear navigation.
