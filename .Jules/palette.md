## 2025-05-15 - Improving Accessibility of Icon-Only Buttons
**Learning:** Icon-only buttons without labels are inaccessible to screen reader users and often lack semantic clarity. Using `<button type="button">` with `aria-label` and `:focus-visible` styles ensures both accessibility and a clear visual focus indicator for keyboard navigation.
**Action:** Always prefer semantic `<button>` elements over `<div>` for interactive controls and provide descriptive `aria-label` for any button that doesn't have visible text.
