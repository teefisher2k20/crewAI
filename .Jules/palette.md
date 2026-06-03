# Palette's Journal - CrewAI Flow Visualization

## 2025-05-15 - [Initial Exploration]
**Learning:** The Flow visualization tool uses a side drawer for node details. Currently, it lacks explicit focus management when opening and closing, which is a key accessibility requirement for modal-like components.
**Action:** Implement focus trapping/management: store the last focused element, focus the close button on open, and restore focus on close.
