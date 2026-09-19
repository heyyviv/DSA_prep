# Jump Game

- **Difficulty**: Medium
- **Topic**: 15_greedy
- **Pattern**: Greedy Goal Tracking
- **Companies**: Meta, Google, Amazon
- **LeetCode Link**: https://leetcode.com/problems/jump-game/
- **Date Solved**: 2026-09-05

---

## 💡 Core Insight
> Work backward from the last index. Whenever an index can reach the current goal, it becomes the new goal; reaching goal zero proves the end is reachable.

---

## 🧠 Mental Model & Decision Matrix

| Decision / Step | Why / Rationale |
|-----------------|-----------------|
| Start the goal at the final index | The last index is trivially reachable from itself. |
| Scan from right to left | Each index can be judged by whether it reaches the latest known good position. |
| Move the goal left when reachable | This maintains the leftmost position known to reach the end. |

---

## ⏱ Complexity Analysis
- **Time Complexity**: $O(n)$ — each index is inspected once.
- **Space Complexity**: $O(1)$ — only the goal index is stored.

---

## 💻 C++ Optimal Solution

```cpp
// See ../topics/15_greedy/jump_game.cpp
```

---

## ⚠️ Common Pitfalls & Edge Cases
- [x] A one-element array is already at the destination.
- [x] A zero only blocks progress if no earlier index can jump past it.
- [x] Do not confuse maximum jump length with an exact jump requirement.

---

## 🔄 SRS Tracking
- **Stage**: 1
- **Review Date**: 2026-09-06
- **Last Rating**: New
- **Review Count**: 0
- **Graduated**: No
- **Pattern Tag**: greedy-goal-tracking
