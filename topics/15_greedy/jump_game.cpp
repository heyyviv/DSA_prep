/**
 * Problem: Jump Game
 * Link: https://leetcode.com/problems/jump-game/
 * Difficulty: Medium
 * Topic: 15_greedy
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
    bool canJump(vector<int>& nums) {
        int goal = static_cast<int>(nums.size()) - 1;

        for (int index = goal - 1; index >= 0; --index) {
            if (index + nums[index] >= goal) {
                goal = index;
            }
        }

        return goal == 0;
    }
};
