## 2025-05-14 - [Semantic Buttons and Focus Management in Visualization Drawers]
**Learning:** Using non-semantic elements (like divs) for interactive controls in complex visualizations breaks keyboard accessibility. Explicit focus management is required when side panels take over the screen to ensure users can navigate back to their starting point.
**Action:** Always prefer semantic <button type="button"> for interactive elements and implement focus traps or restoration logic for modal-like components (drawers, dialogs).
