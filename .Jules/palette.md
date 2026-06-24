# Palette's UX Journal

## 2025-05-15 - Interactive Elements as Semantic Buttons
**Learning:** Using `div` or `span` for interactive elements (like navigation controls or accordions) requires manual management of focus, keyboard events (Enter/Space), and screen reader roles. Converting these to `<button type="button">` provides keyboard accessibility, focus management, and semantic meaning for "free".
**Action:** Always prefer `<button type="button">` for interactive elements that don't navigate to a new URL. Use CSS resets (`background: none`, `border: none`, etc.) to maintain custom designs while benefiting from native accessibility.

## 2025-05-15 - ARIA States for Dynamic Content
**Learning:** Screen readers need explicit state communication for dynamic UI components like accordions or copy buttons. Using `aria-expanded` on headers and updating `aria-label`/`title` on buttons (e.g., "Copy code" -> "Copied!") ensures that all users, regardless of visual ability, understand the current state and results of their actions.
**Action:** Implement `aria-expanded` for all toggleable sections and provide immediate accessible feedback for asynchronous or clipboard-related actions.
