## 2025-05-15 - Standardized CLI Guidance Panels
**Learning:** Standardized post-creation guidance using Rich panels improves user onboarding by providing clear, actionable next steps (cd, install, run). Consistency in these panels (border style, list formatting) makes the CLI feel more professional and predictable.
**Action:** Use the `print_next_steps` utility in `lib/crewai/src/crewai/cli/utils.py` for any CLI command that creates new project artifacts or significantly changes the project state.
