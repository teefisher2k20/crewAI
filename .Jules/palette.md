## 2025-05-15 - [Dynamic Accessible Feedback]
**Learning:** For icon-only buttons that trigger an action (like "Copy"), visual feedback (icon change) is insufficient for screen readers. Providing a dynamic ARIA label that updates to "Action Copied" provides the necessary confirmation.
**Action:** Always implement dynamic `aria-label` updates alongside visual state changes for interactive utility buttons.
