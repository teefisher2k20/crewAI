## 2025-05-15 - [Unified Next Steps Pattern]
**Learning:** Providing consistent post-creation guidance (navigation, installation, execution) via Rich panels significantly improves the "first-mile" experience for CLI users. A unified `print_next_steps` utility ensures this experience remains consistent across different project types (crews, flows).
**Action:** Always include actionable next steps after successful creation or initialization commands using a standard visual format like `rich.panel.Panel`.

## 2025-05-15 - [Robust Version Reporting]
**Learning:** Users appreciate knowing if they are out of date. Integrating update checks into the `version` command provides a non-intrusive way to encourage staying current.
**Action:** Enhance `version` commands with update notifications and use styled output to highlight key information like version numbers and update instructions.
