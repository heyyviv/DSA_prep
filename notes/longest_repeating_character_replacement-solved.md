# Longest Repeating Character Replacement

- **Difficulty**: Medium
- **Topic**: 03_sliding_window
- **Pattern**: Sliding Window (Variable Length) + Frequency Map
- **Companies**: Meta, Google, Amazon
- **LeetCode Link**: [LeetCode 424](https://leetcode.com/problems/longest-repeating-character-replacement/)
- **Date Solved**: 2026-07-22

---

## 💡 Core Insight
> A sliding window $[l, r]$ is valid if the window length minus the frequency of the most frequent character in that window is at most $k$: i.e., $(r - l + 1) - \text{max\_freq} \le k$.
> By maintaining the count of characters in the window and tracking the maximum frequency of any character seen in the window so far, we can expand the window to the right and shrink it from the left whenever this condition is violated.

---

## 🧠 Mental Model & Decision Matrix

| Decision / Step | Why / Rationale |
|-----------------|-----------------|
| **Optimize $O(26)$ Scan** | Instead of scanning a frequency array of size 26 in each step, we only track the historical maximum frequency (`max_freq`) seen within any window. We do not need to decrease `max_freq` when shrinking the window because we are only looking for a window larger than our current maximum. |
| **Use an Array for Frequencies** | Since the characters are only uppercase English letters ('A'-'Z'), a `vector<int>` of size 26 is much faster and has lower overhead than a general `std::unordered_map`. |
| **Shift/Shrink with `if` instead of `while`** | Because the right pointer moves by 1 step in each iteration, the window size can grow by at most 1. Hence, a single `if` check is sufficient to shift the window left when the condition is violated, preserving the maximum window size. |

---

## ⏱ Complexity Analysis
- **Time Complexity**: $O(N)$ — We traverse the string `s` exactly once with the right pointer `r`. All operations inside the loop (frequency map update, `max` check, pointer increments) are $O(1)$ constant time operations.
- **Space Complexity**: $O(1)$ — The frequency helper vector has a fixed size of 26, which is constant auxiliary space.

---

## 💻 C++ Optimal Solution

```cpp
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

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
```

---

## ⚠️ Common Pitfalls & Edge Cases
- [x] **Redundant helper function:** Scanning the frequency array of size 26 at each step results in a slow $O(26 \cdot N)$ runtime. Keeping a running `max_freq` avoids this.
- [x] **Off-by-one errors:** Calculating the window length should be `r - l + 1` instead of `r - l`.
- [x] **Character lookup offset:** Using `s[r] - 'A'` to map 'A'-'Z' to index ranges `0-25`.

---

## 🔄 SRS Tracking
- **Stage**: 1
- **Review Date**: 2026-07-23
- **Last Rating**: New
- **Review Count**: 0
- **Graduated**: No
- **Pattern Tag**: 03_sliding_window
- **Difficulty**: Medium
