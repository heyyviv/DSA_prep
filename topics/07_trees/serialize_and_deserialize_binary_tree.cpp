/**
 * Problem: Serialize and Deserialize Binary Tree
 * Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
 * Difficulty: Hard
 * Topic: 07_trees
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
#include <sstream>

using namespace std;

// Speed up standard I/O operations for competitive C++ speed
static const auto fast_io = []() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();

class Codec {
public:
    string serialize(TreeNode* root) {
        if (root == nullptr) {
            return "null";
        }

        queue<TreeNode*> nodes;
        nodes.push(root);
        string data;

        while (!nodes.empty()) {
            TreeNode* current = nodes.front();
            nodes.pop();

            if (current == nullptr) {
                data += "null,";
                continue;
            }

            data += to_string(current->val) + ',';
            nodes.push(current->left);
            nodes.push(current->right);
        }

        return data;
    }

    TreeNode* deserialize(string data) {
        if (data == "null") {
            return nullptr;
        }

        stringstream stream(data);
        string token;
        getline(stream, token, ',');
        TreeNode* root = new TreeNode(stoi(token));
        queue<TreeNode*> nodes;
        nodes.push(root);

        while (!nodes.empty()) {
            TreeNode* current = nodes.front();
            nodes.pop();

            getline(stream, token, ',');
            if (token != "null") {
                current->left = new TreeNode(stoi(token));
                nodes.push(current->left);
            }

            getline(stream, token, ',');
            if (token != "null") {
                current->right = new TreeNode(stoi(token));
                nodes.push(current->right);
            }
        }

        return root;
    }
};
