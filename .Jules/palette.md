## 2025-05-15 - Improving Flow Visualization Accessibility and Feedback

**Learning:** Using `div` elements as buttons is a common accessibility anti-pattern that prevents keyboard navigation and screen reader recognition. Converting them to semantic `<button>` elements with `aria-label` and adding `:focus-visible` and `:active` states significantly improves the user experience for both keyboard and mouse users with minimal code changes.

**Action:** Always prefer semantic `<button type="button">` for interactive elements that don't navigate to a new URL. Ensure they have descriptive labels and clear visual feedback for all interaction states (hover, focus, active).
