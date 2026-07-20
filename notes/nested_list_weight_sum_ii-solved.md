# Nested List Weight Sum II

- **Difficulty**: Medium
- **Topic**: 07_trees (Nested List / BFS level sum)
- **Pattern**: Reverse Depth Weighting via Running Cumulative Sum
- **Companies**: LinkedIn, Meta, Google
- **LeetCode Link**: [LeetCode 364](https://leetcode.com/problems/nested-list-weight-sum-ii/)
- **Date Solved**: 2026-07-20

---

## 💡 Core Insight
> Instead of calculating `max_depth` upfront to compute $(max\_depth - depth + 1) \times val$, maintain a **running cumulative sum** across BFS levels! Each level's sum is added to the running sum, effectively multiplying higher-level elements by larger weights as deeper levels are processed.

---

## 🧠 Mental Model & Decision Matrix

| Decision / Step | Why / Rationale |
|-----------------|-----------------|
| **Avoid 2-pass Depth Calculation** | Standard weighted sum uses depth from top down. Reverse variant needs weights scaled from bottom up. Computing max depth first requires 2 passes. |
| **Running Cumulative Sum (`unweighted += val`, `weighted += unweighted`)** | At each level, adding `unweighted` to `weighted` repeatedly accumulates previous levels' values $k$ times if there are $k$ levels remaining! |
| **Level-by-Level BFS Queue** | Process all elements at current depth together before advancing to nested sub-lists. |

---

## ⏱ Complexity Analysis
- **Time Complexity**: $O(N)$ where $N$ is the total number of nested integers/lists.
- **Space Complexity**: $O(N)$ for the queue storing elements per level.

---

## 💻 C++ Optimal Solution

```cpp
#include <vector>
#include <queue>

// Interface stub for NestedInteger
class NestedInteger {
public:
    bool isInteger() const;
    int getInteger() const;
    const std::vector<NestedInteger>& getList() const;
};

class Solution {
public:
    int depthSumInverse(const std::vector<NestedInteger>& nestedList) {
        std::queue<NestedInteger> q;
        for (const auto& ni : nestedList) {
            q.push(ni);
        }

        int unweighted = 0;
        int weighted = 0;

        while (!q.empty()) {
            int level_size = q.size();
            for (int i = 0; i < level_size; ++i) {
                NestedInteger curr = q.front();
                q.pop();

                if (curr.isInteger()) {
                    unweighted += curr.getInteger();
                } else {
                    for (const auto& next_ni : curr.getList()) {
                        q.push(next_ni);
                    }
                }
            }
            // Add current level's unweighted sum to weighted total
            // Elements at higher levels get added multiple times across outer loop iterations!
            weighted += unweighted;
        }

        return weighted;
    }
};
```

---

## ⚠️ Common Pitfalls & Edge Cases
- [x] Empty nested list returns 0.
- [x] Single nested integer with deep nesting.
- [x] Negative values inside nested integers.

---

## 🔄 SRS Tracking
- **Stage**: 1
- **Review Date**: 2026-07-21
- **Last Rating**: New
- **Review Count**: 0
- **Graduated**: No
- **Pattern Tag**: 07_trees
