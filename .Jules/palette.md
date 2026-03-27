## 2025-05-15 - Synchronizing ARIA labels with dynamic state changes
**Learning:** When interactive elements like theme toggles use icons and titles to reflect state, the ARIA label must be manually synchronized in JavaScript alongside the visual changes. Screen readers rely on the ARIA label, which doesn't automatically update when only the inner HTML or title attribute changes.
**Action:** Always update `aria-label` using `setAttribute` whenever a toggle's state changes, especially for icon-only buttons.
