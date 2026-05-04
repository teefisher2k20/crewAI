## 2025-05-15 - [Reusable "Next Steps" CLI Pattern]
**Learning:** Users benefit greatly from immediate, actionable guidance after project initialization. Using a consistent visual container (like a Rich Panel) for "Next Steps" across different creation commands (crew, flow, add-crew) creates a cohesive and helpful CLI experience.
**Action:** Use the `print_next_steps` utility in `lib/crewai/src/crewai/cli/utils.py` for any new CLI commands that initialize or modify project structures.
