# Sum of Two Integers

- **Difficulty**: Medium
- **Topic**: 18_bit_manipulation
- **Pattern**: Bitwise Addition
- **Companies**: Meta, Google, Amazon
- **LeetCode Link**: https://leetcode.com/problems/sum-of-two-integers/
- **Date Solved**: 2026-09-06

---

## 💡 Core Insight
> XOR combines bits without carry, while AND identifies every carry bit. Shift the carries left and repeat until no carry remains.

---

## 🧠 Mental Model & Decision Matrix

| Decision / Step | Why / Rationale |
|-----------------|-----------------|
| XOR the current values | Produces the partial sum without carries. |
| AND then left-shift | Identifies and positions every carry for the next addition. |
| Use unsigned fixed-width arithmetic | Makes high-bit shifts well-defined while preserving the 32-bit bit pattern. |

---

## ⏱ Complexity Analysis
- **Time Complexity**: $O(1)$ — at most 32 carry-propagation iterations for 32-bit integers.
- **Space Complexity**: $O(1)$ — a constant number of integer variables.

---

## 💻 C++ Optimal Solution

```cpp
// See ../topics/18_bit_manipulation/sum_of_two_integers.cpp
```

---

## ⚠️ Common Pitfalls & Edge Cases
- [x] Stop only when the carry becomes zero.
- [x] Negative values use the same two's-complement bit operations.
- [x] Avoid signed left-shift overflow by using an unsigned fixed-width type.

---

## 🔄 SRS Tracking
- **Stage**: 1
- **Review Date**: 2026-09-07
- **Last Rating**: New
- **Review Count**: 0
- **Graduated**: No
- **Pattern Tag**: bitwise-addition
