## 2026-03-20 - [Accessibility Enhancement for Flow Visualization]
**Learning:** Converting `div` based interactive elements to semantic `button` elements is critical for keyboard accessibility but requires careful CSS resets (`border: none`, `background: none`, `padding: 0`) and `outline: none` (to be replaced by `:focus-visible`) to avoid visual regressions from default browser styles.
**Action:** Always include a comprehensive button reset when converting non-semantic elements to buttons, and use `:focus-visible` for high-contrast focus indicators using brand colors.
