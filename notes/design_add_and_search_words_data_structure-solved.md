# Design Add and Search Words Data Structure

- **Difficulty**: Medium
- **Topic**: 08_tries
- **Pattern**: Trie with DFS Wildcard Search
- **Companies**: Meta, Amazon, Google
- **LeetCode Link**: https://leetcode.com/problems/design-add-and-search-words-data-structure/
- **Date Solved**: 2026-09-03

---

## 💡 Core Insight
> Store each word character-by-character in a prefix tree. A normal search character follows one child; a dot must recursively try every existing child at that position.

---

## 🧠 Mental Model & Decision Matrix

| Decision / Step | Why / Rationale |
|-----------------|-----------------|
| Mark terminal nodes with one boolean | A node needs only to record whether a complete word ends there. |
| Follow one child for a letter | An ordinary character has exactly one possible continuation. |
| Try all existing children for `.` | The wildcard represents any one character and needs branching search. |

---

## ⏱ Complexity Analysis
- **Add Time Complexity**: $O(L)$ — one node lookup or creation per character.
- **Search Time Complexity**: $O(26^L)$ worst case — wildcards can branch up to 26 ways at each depth.
- **Search Auxiliary Space**: $O(L)$ — maximum recursive call depth.

---

## 💻 C++ Optimal Solution

```cpp
// See ../topics/08_tries/design_add_and_search_words_data_structure.cpp
```

---

## ⚠️ Common Pitfalls & Edge Cases
- [x] A prefix alone is not a match unless its node is terminal.
- [x] A dot branches only to existing child nodes.
- [x] Return early when any wildcard branch finds a match.
- [x] Pass the search word by const reference during recursion.

---

## 🔄 SRS Tracking
- **Stage**: 1
- **Review Date**: 2026-09-04
- **Last Rating**: Okay
- **Review Count**: 1
- **Graduated**: No
- **Pattern Tag**: trie-wildcard-dfs
