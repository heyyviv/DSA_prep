/**
 * Problem: Sum of Two Integers
 * Link: https://leetcode.com/problems/sum-of-two-integers/
 * Difficulty: Medium
 * Topic: 18_bit_manipulation
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
#include <cstdint>

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
    int getSum(int a, int b) {
        uint32_t left = static_cast<uint32_t>(a);
        uint32_t right = static_cast<uint32_t>(b);

        while (right != 0) {
            const uint32_t carry = (left & right) << 1;
            left ^= right;
            right = carry;
        }

        return static_cast<int>(left);
    }
};
