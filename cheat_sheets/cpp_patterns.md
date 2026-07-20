# C++ Big Tech DSA Pattern & STL Master Cheat Sheet

Essential reference for Big Tech coding rounds (Meta, Google, Amazon, Uber, Microsoft). Focuses on optimal Modern C++ (C++17/20), STL efficiency, memory management, and pattern templates.

---

## ⚡ C++ Performance & Memory Best Practices

### 1. Fast I/O Boilerplate
```cpp
static const auto fast_io = []() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    return 0;
}();
```

### 2. Passing Parameters: Value vs Reference
- `const string& s` or `const vector<int>& nums`: **Pass by const reference** to prevent expensive deep copies ($O(N)$ overhead).
- `int val`, `double x`: Pass primitive types by value.
- `vector<int>&& nums`: Use move semantics when transferring ownership.

### 3. Vector Capacity Pre-allocation
Avoid dynamic re-allocations during push_back:
```cpp
vector<int> result;
result.reserve(N); // Reserves memory upfront
```

### 4. Custom Comparators in `std::sort` & `std::priority_queue`
```cpp
// Sort pairs by first element asc, second element desc
sort(vec.begin(), vec.end(), [](const pair<int,int>& a, const pair<int,int>& b) {
    if (a.first != b.first) return a.first < b.first;
    return a.second > b.second;
});

// Min-Heap of custom struct
struct Event {
    int time, type;
    bool operator>(const Event& other) const {
        return time > other.time;
    }
};
priority_queue<Event, vector<Event>, greater<Event>> min_heap;
```

---

## 🧩 18 Core DSA Pattern Blueprints

### 1. Two Pointers (Opposite Direction)
**Used for**: Sorted arrays, Pair Sum, Palindromes.
```cpp
int left = 0, right = nums.size() - 1;
while (left < right) {
    int current_sum = nums[left] + nums[right];
    if (current_sum == target) return {left, right};
    else if (current_sum < target) ++left;
    else --right;
}
```

### 2. Sliding Window (Variable Length)
**Used for**: Longest substring/subarray with condition.
```cpp
unordered_map<char, int> counts;
int left = 0, max_len = 0;
for (int right = 0; right < s.length(); ++right) {
    counts[s[right]]++;
    while (!isValid(counts)) { // Condition violated
        counts[s[left]]--;
        if (counts[s[left]] == 0) counts.erase(s[left]);
        ++left;
    }
    max_len = max(max_len, right - left + 1);
}
```

### 3. Monotonic Stack (Next Greater Element)
**Used for**: Daily Temperatures, Next Greater Element, Largest Rectangle in Histogram.
```cpp
stack<int> st; // Stores indices
vector<int> res(n, -1);
for (int i = 0; i < n; ++i) {
    while (!st.empty() && nums[i] > nums[st.top()]) {
        res[st.top()] = nums[i];
        st.pop();
    }
    st.push(i);
}
```

### 4. Binary Search (Find Lower Bound Boundary)
**Used for**: Search in rotated sorted array, Capacity To Ship Packages, Koko Eating Bananas.
```cpp
int low = min_val, high = max_val, ans = -1;
while (low <= high) {
    int mid = low + (high - low) / 2;
    if (isFeasible(mid)) {
        ans = mid;
        high = mid - 1; // Try smaller valid answer
    } else {
        low = mid + 1;
    }
}
```

### 5. BFS Graph Traversal (Shortest Path in Unweighted Graph)
```cpp
queue<int> q;
unordered_set<int> visited;
q.push(start_node);
visited.insert(start_node);
int steps = 0;

while (!q.empty()) {
    int sz = q.size();
    for (int i = 0; i < sz; ++i) {
        int curr = q.front(); q.pop();
        if (curr == target) return steps;
        for (int neighbor : adj[curr]) {
            if (!visited.count(neighbor)) {
                visited.insert(neighbor);
                q.push(neighbor);
            }
        }
    }
    steps++;
}
```

### 6. Topological Sort / Kahn's Algorithm (DAG Cycle Detection)
**Used for**: Course Schedule I & II, Alien Dictionary.
```cpp
vector<int> inDegree(n, 0);
for (int u = 0; u < n; ++u)
    for (int v : adj[u]) inDegree[v]++;

queue<int> q;
for (int i = 0; i < n; ++i)
    if (inDegree[i] == 0) q.push(i);

vector<int> topoOrder;
while (!q.empty()) {
    int curr = q.front(); q.pop();
    topoOrder.push_back(curr);
    for (int neighbor : adj[curr]) {
        if (--inDegree[neighbor] == 0) q.push(neighbor);
    }
}
bool hasCycle = topoOrder.size() != n;
```

### 7. Dijkstra's Algorithm (Shortest Path in Weighted Graph)
```cpp
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq; // {dist, u}
vector<int> dist(n, INT_MAX);
dist[start] = 0;
pq.push({0, start});

while (!pq.empty()) {
    auto [d, u] = pq.top(); pq.pop();
    if (d > dist[u]) continue;
    for (auto& [v, w] : adj[u]) {
        if (dist[u] + w < dist[v]) {
            dist[v] = dist[u] + w;
            pq.push({dist[v], v});
        }
    }
}
```

### 8. Disjoint Set Union (DSU / Union-Find)
```cpp
class DSU {
    vector<int> parent, rank;
public:
    DSU(int n) : parent(n), rank(n, 0) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]); // Path compression
    }
    bool unite(int i, int j) {
        int root_i = find(i), root_j = find(j);
        if (root_i != root_j) {
            if (rank[root_i] < rank[root_j]) swap(root_i, root_j);
            parent[root_j] = root_i;
            if (rank[root_i] == rank[root_j]) rank[root_i]++;
            return true;
        }
        return false; // Already connected
    }
};
```
