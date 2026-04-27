# Palette Journal

This journal tracks critical UX and accessibility learnings for the CrewAI project.

## 2025-05-15 - Improving Accessibility of Flow Visualization Controls
**Learning:** Using `div` elements for interactive controls like navigation buttons prevents native keyboard accessibility and screen reader support. Missing focus indicators further exclude keyboard-only users. Explicitly associating labels with form controls (using `for` and `id`) is essential for both accessibility and improved hit areas.
**Action:** Always use semantic `<button type="button">` for interactive elements that are not links. Ensure all icon-only buttons have descriptive `aria-label` attributes. Use `:focus-visible` to provide clear visual feedback for keyboard navigation without affecting mouse users.
