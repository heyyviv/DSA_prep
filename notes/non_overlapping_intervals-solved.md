# Non-overlapping Intervals

- **Difficulty**: Medium
- **Topic**: 16_intervals
- **Pattern**: Greedy Interval Selection
- **Companies**: Meta, Google, Amazon
- **LeetCode Link**: https://leetcode.com/problems/non-overlapping-intervals/
- **Date Solved**: 2026-09-05

---

## 💡 Core Insight
> Keeping the compatible interval that finishes earliest leaves the most room for every future interval. Any later-ending overlapping interval is therefore the one to discard.

---

## 🧠 Mental Model & Decision Matrix

| Decision / Step | Why / Rationale |
|-----------------|-----------------|
| Sort by ending time | Makes the currently selected interval end as early as possible. |
| Keep the earliest-finishing compatible interval | It maximizes room for later intervals. |
| Count an overlap as a removal | The already kept interval ends no later than the current interval. |

---

## ⏱ Complexity Analysis
- **Time Complexity**: $O(n \log n)$ — sorting dominates the subsequent linear scan.
- **Space Complexity**: $O(1)$ auxiliary — only counters and the last accepted end time are stored (excluding the sort implementation).

---

## 💻 C++ Optimal Solution

```cpp
// See ../topics/16_intervals/non_overlapping_intervals.cpp
```

---

## ⚠️ Common Pitfalls & Edge Cases
- [x] Intervals that touch (`end == start`) do not overlap.
- [x] The comparator must be a strict ordering; use `<`, not `<=`.
- [x] After sorting by end, never replace a kept interval with a later-ending overlap.

---

## 🔄 SRS Tracking
- **Stage**: 1
- **Review Date**: 2026-09-06
- **Last Rating**: New
- **Review Count**: 0
- **Graduated**: No
- **Pattern Tag**: greedy-interval-selection
