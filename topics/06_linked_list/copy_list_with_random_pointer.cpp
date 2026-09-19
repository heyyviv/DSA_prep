/**
 * Problem: Copy List with Random Pointer
 * Link: https://leetcode.com/problems/copy-list-with-random-pointer/
 * Difficulty: Medium
 * Topic: 06_linked_list
 * Companies: Meta, Amazon, Microsoft
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
    Node* copyRandomList(Node* head) {
        if (head == nullptr) {
            return nullptr;
        }

        unordered_map<Node*, Node*> clones;
        for (Node* original = head; original != nullptr; original = original->next) {
            clones[original] = new Node(original->val);
        }

        for (Node* original = head; original != nullptr; original = original->next) {
            Node* clone = clones[original];
            clone->next = clones[original->next];
            clone->random = clones[original->random];
        }

        return clones[head];
    }
};
