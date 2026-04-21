## 2026-04-21 - [Flow Visualization Accessibility Enhancements]
**Learning:** Icon-only navigation buttons and interactive elements like theme toggles lack semantic meaning and proper labels for screen readers. Using `div` for buttons also breaks standard keyboard interaction (Tab, Enter/Space) unless manually implemented.
**Action:** Always use semantic `<button type="button">` for interactive controls. Provide explicit `aria-label` for icon-only buttons and ensure focus indicators (`:focus-visible`) are visually distinct and match the theme.
