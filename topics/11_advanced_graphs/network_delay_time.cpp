/**
 * Problem: Network Delay Time
 * Link: https://leetcode.com/problems/network-delay-time/
 * Difficulty: Medium
 * Topic: 11_advanced_graphs (Dijkstra's Algorithm / Shortest Path)
 * Companies: Uber, Google, TikTok
 */

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

static const auto fast_io = []() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    return 0;
}();

class Solution {
public:
    // Optimal Dijkstra's Algorithm O(E log V) Time | O(V + E) Space
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // Adjacency List: node -> list of {neighbor, weight}
        vector<vector<pair<int,int>>> g(n + 1);
        for (const auto& edge : times) {
            g[edge[0]].push_back({edge[1], edge[2]});
        }
        
        vector<int> vis(n + 1, 0);
        // Min-Heap using negated distances: {-dist, node}
        priority_queue<pair<int,int>> pq;
        pq.push({0, k});
        
        int ans = 0;
        while (!pq.empty()) {
            int time = -pq.top().first;
            int node = pq.top().second;
            pq.pop();
            
            if (vis[node] != 0) {
                continue; // Skip already visited nodes (lazy deletion)
            }
            vis[node] = 1;
            ans = max(ans, time);
            
            for (const auto& neighbor : g[node]) {
                int next_node = neighbor.first;
                int weight = neighbor.second;
                if (vis[next_node] == 0) {
                    pq.push({-(time + weight), next_node});
                }
            }
        }
        
        // Ensure all n nodes were reached
        for (int i = 1; i <= n; i++) {
            if (vis[i] == 0) return -1;
        }
        
        return ans;
    }
};
