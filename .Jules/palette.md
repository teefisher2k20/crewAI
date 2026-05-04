## 2025-05-14 - Standardizing Onboarding UX in CLI
**Learning:** Providing immediate, clear, and visually distinct "Next Steps" after project creation significantly improves user onboarding by reducing the cognitive load of remembering the next commands. Using a `rich.Panel` creates a consistent visual pattern that users can easily recognize.
**Action:** Always implement a `print_next_steps` utility for CLI-based project generators and call it upon successful creation.

## 2025-05-14 - Accurate Version Reporting
**Learning:** In multi-package repositories, it's easy to accidentally report the version of the main package instead of the sub-package requested. Correct reporting is crucial for debugging.
**Action:** Verify that `version` commands use the specific package identifier (e.g., `crewai-tools` vs `crewai`) when reporting versions for components.
