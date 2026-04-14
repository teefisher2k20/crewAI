## 2025-05-15 - Semantic Buttons and Icon Labels

**Learning:** The Flow visualization interface heavily utilized `div` elements for interactive controls, which lacks native keyboard accessibility and screen reader support. Additionally, icon-only buttons lacked descriptive labels.

**Action:** Always prefer semantic `<button type="button">` for interactive elements and ensure all icon-only controls have descriptive `aria-label` attributes. Use `:focus-visible` styles with brand-consistent colors to provide clear keyboard navigation feedback.
