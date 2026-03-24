## 2025-05-14 - [Flow Visualization Accessibility]
**Learning:** Interactive elements in the Flow visualization (navigation controls, drawer headers, and grouped triggers) were implemented using non-semantic elements (div, span) without keyboard support or ARIA roles, making them inaccessible to keyboard users and screen readers.
**Action:** Use semantic <button> elements for controls and ensure dynamically generated interactive elements have role="button", tabindex="0", and appropriate keyboard event listeners (Enter/Space).
