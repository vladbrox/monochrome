## 2025-05-14 - [Inefficient Quality Token Lookup]
**Learning:** The `normalizeQualityToken` function used a nested loop (O(N*M)) to look up quality tokens in a static map. In large tracklists (hundreds of tracks), these lookups accumulate and can contribute to UI jank during rendering.
**Action:** Always pre-compute flat lookup maps for static data that is frequently accessed in rendering loops or track processing logic.
