# Palette's Journal - CrewAI CLI UX Improvements

## 2025-05-14 - Initializing Journal
**Learning:** Initializing the journal for Palette's UX work.
**Action:** Always document critical UX/accessibility learnings here.

## 2025-05-14 - Guided Onboarding with "Next Steps"
**Learning:** CLI users often feel lost after a "successful" project initialization if no immediate guidance is provided. A visually distinct "Next Steps" panel reduces cognitive load and improves the onboarding experience.
**Action:** Implement a reusable `print_next_steps` utility using `rich.Panel` to provide consistent, actionable guidance (navigation, installation, execution) after project creation commands.
