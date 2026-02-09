# Palette's Journal - CrewAI

This journal tracks critical UX and accessibility learnings while working on the CrewAI codebase.

## 2025-02-14 - [Consistent CLI Feedback]
**Learning:** Initial CLI commands like `crewai create` provided minimal feedback, making it unclear for new users what to do next. Using visual cues like panels and explicit "Next Steps" improves the onboarding experience significantly.
**Action:** Use `rich` panels for success messages in CLI commands to guide users through the next steps of their journey.
