# Multiply Strings

- **Difficulty**: Medium
- **Topic**: 17_math_and_geometry
- **Pattern**: Grade-School String Multiplication
- **Companies**: Meta, Amazon, Google
- **LeetCode Link**: https://leetcode.com/problems/multiply-strings/
- **Date Solved**: 2026-09-06

---

## 💡 Core Insight
> Multiply the first number by each digit of the second from right to left, append the appropriate place-value zeroes, and add the partial products as strings.

---

## 🧠 Mental Model & Decision Matrix

| Decision / Step | Why / Rationale |
|-----------------|-----------------|
| Process multiplier digits from right to left | Each next digit represents the next higher place value. |
| Carry within one-digit multiplication | Every partial product is built without converting the full input to an integer. |
| Add partial products as strings | This supports inputs larger than built-in numeric types. |

---

## ⏱ Complexity Analysis
- **Time Complexity**: $O(N^2)$ — with $N$ as the maximum input length, all partial-product and addition work is quadratic.
- **Space Complexity**: $O(N)$ — the running result, partial product, and addition buffer are linear in the output length.

---

## 💻 C++ Optimal Solution

```cpp
// See ../topics/17_math_and_geometry/multiply_strings.cpp
```

---

## ⚠️ Common Pitfalls & Edge Cases
- [x] Return `"0"` immediately if either input is zero.
- [x] Append place-value zeroes to every partial product after the first.
- [x] Convert a carry back to a character with `'0' + carry`.
- [x] Keep helper parameters as `const string&` to avoid copies.

---

## 🔄 SRS Tracking
- **Stage**: 1
- **Review Date**: 2026-09-07
- **Last Rating**: Okay
- **Review Count**: 1
- **Graduated**: No
- **Pattern Tag**: grade-school-string-multiplication
