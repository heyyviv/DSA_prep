# Copy List with Random Pointer

- **Difficulty**: Medium
- **Topic**: 06_linked_list
- **Pattern**: Hash Map Clone Mapping
- **Companies**: Meta, Amazon, Microsoft
- **LeetCode Link**: https://leetcode.com/problems/copy-list-with-random-pointer/
- **Date Solved**: 2026-08-30

---

## 💡 Core Insight
> Create a clone for every original node before connecting pointers. The original-to-clone map lets `next` and `random` always refer to cloned nodes, including when `random` is `nullptr`.

---

## 🧠 Mental Model & Decision Matrix

| Decision / Step | Why / Rationale |
|-----------------|-----------------|
| Map every original node to a new node | Guarantees deep-copy ownership and provides pointer translation. |
| Create all nodes before assigning relationships | A random pointer can reference any node, including a later one. |
| Look up `nullptr` in the map | `unordered_map::operator[]` supplies a null pointer value for this safe case. |

---

## ⏱ Complexity Analysis
- **Time Complexity**: Expected $O(n)$ — two passes over the list with expected $O(1)$ hash-map operations.
- **Space Complexity**: $O(n)$ — one clone node and one hash-map entry per original node.

---

## 💻 C++ Optimal Solution

```cpp
// See ../topics/06_linked_list/copy_list_with_random_pointer.cpp
```

---

## ⚠️ Common Pitfalls & Edge Cases
- [x] An empty input must return `nullptr`.
- [x] `random` may be `nullptr`.
- [x] `random` may point to the node itself or a later node.
- [x] The copy must not share nodes with the original list.

---

## 🔄 SRS Tracking
- **Stage**: 1
- **Review Date**: 2026-08-31
- **Last Rating**: New
- **Review Count**: 0
- **Graduated**: No
- **Pattern Tag**: hash-map-clone-mapping
