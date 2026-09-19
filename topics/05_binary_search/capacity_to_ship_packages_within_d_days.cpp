/**
 * Problem: Capacity To Ship Packages Within D Days
 * Link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
 * Difficulty: Medium
 * Topic: 05_binary_search
 * Companies: Amazon, Google, Meta
 * Memory / Speed Optimization: Fast I/O included
 */

#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <climits>

using namespace std;

// Speed up standard I/O operations for competitive C++ speed
static const auto fast_io = []() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();

class Solution {
public:
    int requiredDays(const vector<int>& weights, int capacity) {
        int days = 1;
        int load = 0;

        for (int weight : weights) {
            if (load + weight > capacity) {
                ++days;
                load = 0;
            }
            load += weight;
        }

        return days;
    }

    int shipWithinDays(vector<int>& weights, int days) {
        int low = *max_element(weights.begin(), weights.end());
        int high = accumulate(weights.begin(), weights.end(), 0);

        while (low < high) {
            const int capacity = low + (high - low) / 2;
            if (requiredDays(weights, capacity) <= days) {
                high = capacity;
            } else {
                low = capacity + 1;
            }
        }

        return low;
    }
};
