/**
 * Problem: Decode Ways
 * Link: https://leetcode.com/problems/decode-ways/
 * Difficulty: Medium
 * Topic: 13_1d_dynamic_programming
 * Companies: Amazon, Meta, Google
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
    int countDecodings(const string& s, int index, vector<int>& memo) {
        if (index == static_cast<int>(s.size())) {
            return 1;
        }
        if (memo[index] != -1) {
            return memo[index];
        }
        if (s[index] == '0') {
            return memo[index] = 0;
        }

        int ways = countDecodings(s, index + 1, memo);
        if (index + 1 < static_cast<int>(s.size())) {
            const int twoDigit = (s[index] - '0') * 10 + (s[index + 1] - '0');
            if (twoDigit <= 26) {
                ways += countDecodings(s, index + 2, memo);
            }
        }

        return memo[index] = ways;
    }

    int numDecodings(string s) {
        vector<int> memo(s.size(), -1);
        return countDecodings(s, 0, memo);
    }
};
