## 2025-05-14 - [CLI Test Compatibility with Rich Styling]
**Learning:** CLI tests often perform simple string matching (e.g., "assert 'label:' in output"). When introducing Rich styling like Tables, the default alignment might add spaces that don't break string matching, but removing characters like colons will.
**Action:** Always include expected legacy labels (including colons) within Rich-styled components to maintain backward compatibility with existing test suites.
