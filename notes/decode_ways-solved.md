# Decode Ways

- **Difficulty**: Medium
- **Topic**: 13_1d_dynamic_programming
- **Pattern**: Top-Down Dynamic Programming
- **Companies**: Amazon, Meta, Google
- **LeetCode Link**: https://leetcode.com/problems/decode-ways/
- **Date Solved**: 2026-09-01

---

## 💡 Core Insight
> At each valid nonzero position, decode either one digit or a valid two-digit number from 10 to 26. Memoizing the number of ways from each index avoids re-solving overlapping suffixes.

---

## 🧠 Mental Model & Decision Matrix

| Decision / Step | Why / Rationale |
|-----------------|-----------------|
| Use index as the subproblem state | The remaining suffix fully determines the answer. |
| Reject a leading zero | Zero has no standalone letter mapping. |
| Try two digits only when the value is at most 26 | This enforces the encoding range without accepting invalid pairs. |

---

## ⏱ Complexity Analysis
- **Time Complexity**: $O(n)$ — each string index is computed once.
- **Space Complexity**: $O(n)$ — the memo table and recursion stack each use up to $n$ entries.

---

## 💻 C++ Optimal Solution

```cpp
// See ../topics/13_1d_dynamic_programming/decode_ways.cpp
```

---

## ⚠️ Common Pitfalls & Edge Cases
- [x] A leading `0` makes that suffix invalid.
- [x] `10` and `20` are valid pairs, but `30` is not.
- [x] A valid pair consumes two characters, so recurse to `index + 2`.
- [x] Pass the string by reference in recursive calls to avoid copies.

---

## 🔄 SRS Tracking
- **Stage**: 1
- **Review Date**: 2026-09-16
- **Last Rating**: Okay
- **Review Count**: 2
- **Graduated**: No
- **Pattern Tag**: top-down-dp
