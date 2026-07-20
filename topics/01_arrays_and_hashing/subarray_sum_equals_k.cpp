/**
 * Problem: Subarray Sum Equals K
 * Link: https://leetcode.com/problems/subarray-sum-equals-k/
 * Difficulty: Medium
 * Topic: 01_arrays_and_hashing (Prefix Sum + Hash Map)
 * Companies: Meta, Google, Amazon
 */

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

static const auto fast_io = []() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    return 0;
}();

class Solution {
public:
    // Optimal O(N) Time | O(N) Space
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> prefix_counts;
        prefix_counts[0] = 1; // Base case: prefix sum of 0 occurs 1 time before array starts
        
        int curr_sum = 0;
        int count = 0;
        
        for (int num : nums) {
            curr_sum += num;
            
            // Check if (curr_sum - k) exists in hash map
            if (prefix_counts.count(curr_sum - k)) {
                count += prefix_counts[curr_sum - k];
            }
            
            // Record current prefix sum frequency
            prefix_counts[curr_sum]++;
        }
        
        return count;
    }
};
