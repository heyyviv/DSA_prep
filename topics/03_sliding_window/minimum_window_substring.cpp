/**
 * Problem: Minimum Window Substring
 * Link: https://leetcode.com/problems/minimum-window-substring/
 * Difficulty: Hard
 * Topic: 03_sliding_window
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
    string minWindow(string s, string t) {
        constexpr int kAlphabetRange = 'z' - 'A' + 1;
        vector<int> required(kAlphabetRange, 0);
        vector<int> window(kAlphabetRange, 0);

        for (char c : t) {
            ++required[c - 'A'];
        }

        int bestStart = -1;
        int bestLength = INT_MAX;
        int left = 0;

        for (int right = 0; right < static_cast<int>(s.size()); ++right) {
            ++window[s[right] - 'A'];

            while (covers(window, required)) {
                const int length = right - left + 1;
                if (length < bestLength) {
                    bestStart = left;
                    bestLength = length;
                }
                --window[s[left] - 'A'];
                ++left;
            }
        }

        return bestStart == -1 ? "" : s.substr(bestStart, bestLength);
    }

private:
    bool covers(const vector<int>& window, const vector<int>& required) {
        for (int index = 0; index < static_cast<int>(required.size()); ++index) {
            if (window[index] < required[index]) {
                return false;
            }
        }
        return true;
    }
};
