## 2025-05-22 - Semantic Button Accessibility Pattern
**Learning:** Using `<div>` for interactive elements (like navigation buttons and accordion headers) breaks keyboard accessibility and screen reader expectations. Semantic `<button type="button">` elements provide native focus management and ARIA support.
**Action:** Always prefer `<button>` for interactive controls. When converting from `<div>`, ensure CSS resets (`appearance: none`, `background: none`, `border: none`, `font-family: inherit`) are applied to maintain visual design while gaining accessibility.

## 2025-05-22 - Visual Feedback for Async Script Loading
**Learning:** Long-running client-side operations (like generating exports with `html2canvas` and `jspdf`) can feel unresponsive if they rely on dynamically loading scripts without visual feedback.
**Action:** Use `document.body.style.cursor = 'wait'` as a lightweight way to provide immediate feedback when starting async operations, ensuring a reset in both `onload` and `onerror` handlers.

## 2025-05-22 - Keyboard Focus Visibility
**Learning:** Custom UI components (like side drawers and legend panels) often lack clear focus indicators, making keyboard navigation difficult.
**Action:** Implement a consistent `:focus-visible` style across all interactive elements using the application's primary brand color for clear visual guidance.
