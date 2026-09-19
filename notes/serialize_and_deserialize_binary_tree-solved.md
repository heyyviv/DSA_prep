# Serialize and Deserialize Binary Tree

- **Difficulty**: Hard
- **Topic**: 07_trees
- **Pattern**: Level-Order Tree Encoding
- **Companies**: Meta, Google, Amazon
- **LeetCode Link**: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
- **Date Solved**: 2026-09-18

---

## 💡 Core Insight
> Encode every tree position in level order, including missing children as `null`. The decoder consumes those same tokens two children at a time for each queued real node.

---

## 🧠 Mental Model & Decision Matrix

| Decision / Step | Why / Rationale |
|-----------------|-----------------|
| Enqueue null child positions during serialization | This preserves true level order rather than interleaving null markers with later nodes. |
| Use one delimiter-separated token stream | Values and null markers can be read in the exact same order. |
| Dequeue one real node and consume two tokens | Those tokens uniquely identify its left and right children. |

---

## ⏱ Complexity Analysis
- **Time Complexity**: $O(n)$ — each real node and null child position is processed a constant number of times.
- **Space Complexity**: $O(n)$ — the queue and serialized string scale with tree size.

---

## 💻 C++ Optimal Solution

```cpp
// See ../topics/07_trees/serialize_and_deserialize_binary_tree.cpp
```

---

## ⚠️ Common Pitfalls & Edge Cases
- [x] A null root must round-trip to a null root.
- [x] Serialize and deserialize must use the identical traversal order.
- [x] Null markers are necessary to preserve the original tree shape.
- [x] Enqueue null positions only during serialization; the decoder queues real nodes only.

---

## 🔄 SRS Tracking
- **Stage**: 1
- **Review Date**: 2026-09-19
- **Last Rating**: New
- **Review Count**: 0
- **Graduated**: No
- **Pattern Tag**: level-order-tree-encoding
