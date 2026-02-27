## 2025-05-14 - [Inefficient Quality Token Lookup]
**Learning:** The `normalizeQualityToken` function used a nested loop (O(N*M)) to look up quality tokens in a static map. In large tracklists (hundreds of tracks), these lookups accumulate and can contribute to UI jank during rendering.
**Action:** Always pre-compute flat lookup maps for static data that is frequently accessed in rendering loops or track processing logic.

## 2025-05-14 - [High-Frequency String & Array Overhead]
**Learning:** Using `Array.filter(Boolean).join(' ')` for class lists and `Array(n).fill(0).map(...).join('')` for skeleton rendering in tight loops creates unnecessary garbage and overhead. Standard string concatenation and simple `for` loops are significantly faster in Vanilla JS when generating large DOM fragments.
**Action:** Prefer string concatenation and `for` loops over modern array methods in performance-critical rendering paths where hundreds of elements are generated.
