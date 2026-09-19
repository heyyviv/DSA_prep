# Minimum Window Substring

- **Difficulty**: Hard
- **Topic**: 03_sliding_window
- **Pattern**: Variable-Size Sliding Window
- **Companies**: Meta, Google, Amazon
- **LeetCode Link**: https://leetcode.com/problems/minimum-window-substring/
- **Date Solved**: 2026-09-16

---

## 💡 Core Insight
> Expand the right boundary until the window covers every required character count, then shrink the left boundary as far as possible while it remains valid. Track the shortest valid window seen.

---

## 🧠 Mental Model & Decision Matrix

| Decision / Step | Why / Rationale |
|-----------------|-----------------|
| Count required characters from `t` | Duplicate requirements must be preserved. |
| Expand until the window covers `t` | No valid answer can end before all requirements are met. |
| Shrink while coverage remains true | Produces the shortest valid window for the current right endpoint. |

---

## ⏱ Complexity Analysis
- **Time Complexity**: $O(n)$ — each boundary advances at most `n` times; the alphabet-size coverage scan is constant.
- **Space Complexity**: $O(1)$ — fixed-size frequency arrays are used.

---

## 💻 C++ Optimal Solution

```cpp
// See ../topics/03_sliding_window/minimum_window_substring.cpp
```

---

## ⚠️ Common Pitfalls & Edge Cases
- [x] Character frequencies, not just presence, must be tracked.
- [x] Return an empty string when no valid window exists.
- [x] Shrink only while the window still covers every requirement.

---

## 🔄 SRS Tracking
- **Stage**: 1
- **Review Date**: 2026-09-17
- **Last Rating**: Okay
- **Review Count**: 1
- **Graduated**: No
- **Pattern Tag**: variable-size-sliding-window
