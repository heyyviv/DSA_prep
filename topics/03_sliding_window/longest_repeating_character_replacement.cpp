/**
 * Problem: Longest Repeating Character Replacement
 * Link: [LeetCode/Platform Link]
 * Difficulty: [Easy / Medium / Hard]
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
    int characterReplacement(string s, int k) {
        int n = s.length();
        int l = 0;
        int ans = 0;
        vector<int> freq(26, 0);
        int max_freq = 0;
        
        for (int r = 0; r < n; ++r) {
            freq[s[r] - 'A']++;
            max_freq = max(max_freq, freq[s[r] - 'A']);
            
            // If the current window size minus the frequency of the most frequent
            // character in the window exceeds k, then we shrink the window.
            if ((r - l + 1) - max_freq > k) {
                freq[s[l] - 'A']--;
                l++;
            }
            ans = max(ans, r - l + 1);
        }
        return ans;
    }
};

int main() {
    Solution sol;
    cout << "Test 1: " << sol.characterReplacement("ABAB", 2) << " (Expected: 4)\n";
    cout << "Test 2: " << sol.characterReplacement("AABABBA", 1) << " (Expected: 4)\n";
    return 0;
}
