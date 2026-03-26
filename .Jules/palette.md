## 2025-05-22 - Improving Navigation Control Accessibility

**Learning:** Using semantic `<button>` elements instead of generic `div` tags for interactive controls automatically provides keyboard support (Tab to focus, Enter/Space to activate) and allows for standard ARIA labeling. Pairing these with `:focus-visible` styles ensures a clear, accessible focus indicator that only appears when needed by keyboard users.

**Action:** Always use `<button type="button">` for non-link interactive elements and ensure `aria-label` is present for icon-only buttons. Apply `:focus-visible` with a high-contrast outline to all interactive components.
