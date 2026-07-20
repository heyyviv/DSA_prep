# Subarray Sum Equals K

- **Difficulty**: Medium
- **Topic**: 01_arrays_and_hashing
- **Pattern**: Prefix Sum + Hash Map Frequency Tracking
- **Companies**: Meta, Google, Amazon
- **LeetCode Link**: [LeetCode 560](https://leetcode.com/problems/subarray-sum-equals-k/)
- **Date Solved**: 2026-07-20

---

## 💡 Core Insight
> A continuous subarray from index $i$ to $j$ has a sum equal to $k$ if $\text{prefix\_sum}[j] - \text{prefix\_sum}[i-1] = k$. Rearranging this yields $\text{prefix\_sum}[i-1] = \text{prefix\_sum}[j] - k$. By maintaining a **hash map of running prefix sum frequencies**, we can find all matching target subarrays in a single $O(N)$ pass!

---

## 🧠 Mental Model & Decision Matrix

| Decision / Step | Why / Rationale |
|-----------------|-----------------|
| **Avoid $O(N^2)$ Nested Loops** | Brute force checks all pairs $(i, j)$ using prefix array. In Big Tech rounds ($N = 2 \times 10^4$), $O(N^2)$ gets TLE or fails optimal criteria. |
| **Base Case: `prefix_counts[0] = 1`** | A prefix sum of `0` exists before element 0. Ensures subarrays starting at index 0 whose sum equals $k$ are counted. |
| **Single-Pass Hash Map Lookup (`curr_sum - k`)** | At index $j$, any previous prefix sum matching `curr_sum - k` represents a valid starting index $i$. |

---

## ⏱ Complexity Analysis
- **Time Complexity**: $O(N)$ — Single pass through `nums` with $O(1)$ average hash map lookup.
- **Space Complexity**: $O(N)$ — Up to $N$ unique prefix sums stored in `unordered_map`.

---

## 💻 C++ Optimal Solution

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> prefix_counts;
        prefix_counts[0] = 1; // Base case
        
        int curr_sum = 0, count = 0;
        for (int num : nums) {
            curr_sum += num;
            if (prefix_counts.count(curr_sum - k)) {
                count += prefix_counts[curr_sum - k];
            }
            prefix_counts[curr_sum]++;
        }
        return count;
    }
};
```

---

## ⚠️ Common Pitfalls & Edge Cases
- [x] Negative numbers in array (Sliding window fails here; Prefix Sum + Hash Map is required!).
- [x] Base case `prefix_counts[0] = 1` omitted causes missing subarrays starting at index 0.
- [x] $O(N^2)$ nested loop TLE on large $N$.

---

## 🔄 SRS Tracking
- **Stage**: 1
- **Review Date**: 2026-07-21
- **Last Rating**: Okay
- **Review Count**: 1
- **Graduated**: No
- **Pattern Tag**: 01_arrays_and_hashing
