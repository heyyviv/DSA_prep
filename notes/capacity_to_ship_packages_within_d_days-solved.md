# Capacity To Ship Packages Within D Days

- **Difficulty**: Medium
- **Topic**: 05_binary_search
- **Pattern**: Binary Search on Answer
- **Companies**: Amazon, Google, Meta
- **LeetCode Link**: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
- **Date Solved**: 2026-08-30

---

## 💡 Core Insight
> For a fixed capacity, greedily load as many consecutive packages as possible each day. If that requires at most the available days, every larger capacity also works; otherwise, the capacity is too small.

---

## 🧠 Mental Model & Decision Matrix

| Decision / Step | Why / Rationale |
|-----------------|-----------------|
| Search from the heaviest package to the total weight | These bounds are respectively the smallest possible and always-feasible capacities. |
| Simulate a capacity greedily | Starting a new day only when necessary minimizes the days needed for that capacity. |
| Keep searching left after a feasible result | The goal is the minimum feasible capacity. |

---

## ⏱ Complexity Analysis
- **Time Complexity**: $O(n \log S)$ — each candidate capacity requires one $O(n)$ scan; $S$ is the sum of all weights.
- **Space Complexity**: $O(1)$ — only scalar counters and bounds are used.

---

## 💻 C++ Optimal Solution

```cpp
// See ../topics/05_binary_search/capacity_to_ship_packages_within_d_days.cpp
```

---

## ⚠️ Common Pitfalls & Edge Cases
- [x] Capacity must be at least the heaviest single package.
- [x] A capacity equal to the total weight always ships everything in one day.
- [x] Start the simulator with one day to avoid an off-by-one count.
- [x] Use a wide enough sum type if the constraints can exceed `int`.

---

## 🔄 SRS Tracking
- **Stage**: 1
- **Review Date**: 2026-08-31
- **Last Rating**: New
- **Review Count**: 0
- **Graduated**: No
- **Pattern Tag**: binary-search-on-answer
