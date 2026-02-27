## 2025-05-14 - [Inefficient Quality Token Lookup]
**Learning:** The `normalizeQualityToken` function used a nested loop (O(N*M)) to look up quality tokens in a static map. In large tracklists (hundreds of tracks), these lookups accumulate and can contribute to UI jank during rendering.
**Action:** Always pre-compute flat lookup maps for static data that is frequently accessed in rendering loops or track processing logic.

## 2025-05-14 - [High-Frequency String & Array Overhead]
**Learning:** Using `Array.filter(Boolean).join(' ')` for class lists and `Array(n).fill(0).map(...).join('')` for skeleton rendering in tight loops creates unnecessary garbage and overhead. Standard string concatenation and simple `for` loops are significantly faster in Vanilla JS when generating large DOM fragments.
**Action:** Prefer string concatenation and `for` loops over modern array methods in performance-critical rendering paths where hundreds of elements are generated.

## 2025-05-14 - [Early Exit & Pre-computation for Metadata]
**Learning:** Quality derivation and priority logic was previously processing all metadata before deciding the best quality. By using pre-computed rank maps and early exits (once HI_RES_LOSSLESS is found), we can skip significant amounts of processing.
**Action:** Always implement early-exit logic when looking for a "best" result in a prioritized list, and use pre-computed maps to avoid repetitive array lookups.

## 2025-05-14 - [Cached Collators for Sorting]
**Learning:** Using `Intl.Collator` for string comparisons in sort functions is much faster than `localeCompare` when dealing with large arrays. Creating the collator once and reusing it avoids repetitive initialization overhead.
**Action:** Use a cached `Intl.Collator` instance for alphabetical sorting in UI lists.
