## 2026-05-06 - [Aria-expanded states on semantic buttons]
**Learning:** In the Flow visualization tool, the `aria-expanded` attribute on interactive accordion buttons is updated using explicit string values 'true' or 'false' (e.g., `setAttribute('aria-expanded', isExpanded ? 'true' : 'false')`) rather than booleans to ensure consistent interpretation by all screen readers.
**Action:** Always use string values for ARIA attributes that expect specific string tokens even if they represent boolean states.
