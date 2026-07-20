# Network Delay Time

- **Difficulty**: Medium
- **Topic**: 11_advanced_graphs
- **Pattern**: Single-Source Shortest Path (Dijkstra's Algorithm via Min-Heap)
- **Companies**: Uber, Google, TikTok
- **LeetCode Link**: [LeetCode 743](https://leetcode.com/problems/network-delay-time/)
- **Date Solved**: 2026-07-20

---

## 💡 Core Insight
> Signal propagation in a weighted graph is equivalent to finding the **single-source shortest path** from starting node `k` to all other nodes. Using **Dijkstra's Algorithm** with a priority queue (min-heap), we extract nodes in increasing order of cumulative delay. The answer is the maximum shortest path time among all nodes, or `-1` if any node remains unvisited.

---

## 🧠 Mental Model & Decision Matrix

| Decision / Step | Why / Rationale |
|-----------------|-----------------|
| **Dijkstra's vs BFS** | Edges have non-negative weights (`w_i >= 0`). Standard BFS only works for unweighted graphs; Dijkstra with priority queue guarantees optimal shortest distances. |
| **Negated Priority Queue Trick (`{-dist, node}`)** | Standard C++ `std::priority_queue` is a max-heap. Negating values (`-dist`) turns it into an efficient min-heap without custom comparator boilerplate. |
| **Lazy Deletion (`if (vis[node]) continue;`)** | Avoids redundant edge relaxations when multiple paths push the same node to the queue. |
| **`ans = max(ans, time)`** | The total delay for the signal to reach *all* nodes is determined by the node that takes the *longest* to receive the signal. |

---

## ⏱ Complexity Analysis
- **Time Complexity**: $O(E \log V)$ — Each edge is processed at most once, and priority queue operations take $O(\log V)$ time (where $V = n$ and $E = \text{times.length}$).
- **Space Complexity**: $O(V + E)$ — $O(V + E)$ for adjacency list graph `g`, $O(V)$ for visited array `vis`, and $O(E)$ for the priority queue.

---

## 💻 C++ Optimal Solution

```cpp
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int,int>>> g(n + 1);
        for (const auto& edge : times) {
            g[edge[0]].push_back({edge[1], edge[2]});
        }
        
        vector<int> vis(n + 1, 0);
        priority_queue<pair<int,int>> pq; // {-dist, node}
        pq.push({0, k});
        
        int ans = 0;
        while (!pq.empty()) {
            int time = -pq.top().first;
            int node = pq.top().second;
            pq.pop();
            
            if (vis[node] != 0) continue;
            vis[node] = 1;
            ans = max(ans, time);
            
            for (const auto& neighbor : g[node]) {
                if (vis[neighbor.first] == 0) {
                    pq.push({-(time + neighbor.second), neighbor.first});
                }
            }
        }
        
        for (int i = 1; i <= n; i++) {
            if (vis[i] == 0) return -1;
        }
        return ans;
    }
};
```

---

## ⚠️ Common Pitfalls & Edge Cases
- [x] 1-based indexing (`n+1` array size allocated).
- [x] Unreachable nodes (returns `-1` when `vis[i] == 0`).
- [x] Duplicate nodes pushed into Priority Queue handled gracefully with `if (vis[node]) continue;`.

---

## 🔄 SRS Tracking
- **Stage**: 1
- **Review Date**: 2026-07-21
- **Last Rating**: Strong
- **Review Count**: 1
- **Graduated**: No
- **Pattern Tag**: 11_advanced_graphs
