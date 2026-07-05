## 2025-05-15 - [Semantic Button Migration Pattern]
**Learning:** Converting interactive `div` elements to semantic `<button type="button">` requires explicit CSS resets (`padding: 0`, `font: inherit`) and `background-clip: padding-box` to maintain visual parity while enabling native keyboard accessibility.
**Action:** Always apply a reset class or shared utility styles when migrating non-semantic interactive elements to buttons to prevent browser-default layout shifts.
>>>>>>> REPLACE
