/**
 * Problem: Design Add and Search Words Data Structure
 * Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/
 * Difficulty: Medium
 * Topic: 08_tries
 * Companies: Meta, Amazon, Google
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

class WordDictionary {
public:
    struct Node {
        vector<Node*> children;
        bool isWord = false;

        Node() : children(26, nullptr) {}
    };

    WordDictionary() : root(new Node()) {}

    void addWord(string word) {
        Node* current = root;
        for (char c : word) {
            const int index = c - 'a';
            if (current->children[index] == nullptr) {
                current->children[index] = new Node();
            }
            current = current->children[index];
        }
        current->isWord = true;
    }

    bool search(string word) {
        return matches(word, 0, root);
    }

private:
    Node* root;

    bool matches(const string& word, int index, Node* current) {
        if (index == static_cast<int>(word.size())) {
            return current->isWord;
        }

        const char c = word[index];
        if (c != '.') {
            Node* next = current->children[c - 'a'];
            return next != nullptr && matches(word, index + 1, next);
        }

        for (Node* next : current->children) {
            if (next != nullptr && matches(word, index + 1, next)) {
                return true;
            }
        }
        return false;
    }
};
