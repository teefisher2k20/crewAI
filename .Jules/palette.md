## 2025-05-15 - [CSS Template Variable Quoting]
**Learning:** Using single quotes around Jinja2 placeholders in CSS (e.g., `'{{ VARIABLE }}'`) can lead to invalid syntax when the placeholder is replaced with a raw value that doesn't expect quotes (like a hex color in a complex property).
**Action:** Omit quotes for direct property values in CSS templates unless specifically required by the property's syntax (e.g., `outline: 2px solid {{ CREWAI_ORANGE }};`).
