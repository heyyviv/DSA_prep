/**
 * Problem: Non-overlapping Intervals
 * Link: https://leetcode.com/problems/non-overlapping-intervals/
 * Difficulty: Medium
 * Topic: 16_intervals
 * Companies: Meta, Google, Amazon
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
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });

        int removals = 0;
        int lastEnd = intervals[0][1];

        for (int i = 1; i < static_cast<int>(intervals.size()); ++i) {
            if (intervals[i][0] < lastEnd) {
                ++removals;
            } else {
                lastEnd = intervals[i][1];
            }
        }

        return removals;
    }
};
