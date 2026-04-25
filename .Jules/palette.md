## 2025-05-15 - [Flow Visualization Accessibility]
**Learning:** Control elements implemented as `div` with `onclick` are not accessible to keyboard or screen reader users. Native semantic elements like `<button>` provide focusability and interactivity out-of-the-box, but require CSS resets (padding, font-family) to maintain visual consistency with previous `div`-based designs.
**Action:** Always prioritize semantic HTML elements over generic containers for interactive components, and ensure `:focus-visible` styles are provided for better keyboard navigation.
