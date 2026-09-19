/**
 * Problem: Multiply Strings
 * Link: https://leetcode.com/problems/multiply-strings/
 * Difficulty: Medium
 * Topic: 17_math_and_geometry
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

class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") {
            return "0";
        }

        string result = "0";
        string suffix;
        for (int index = static_cast<int>(num2.size()) - 1; index >= 0; --index) {
            result = addStrings(result, multiplyByDigit(num1, num2[index]) + suffix);
            suffix += '0';
        }

        return result;
    }

private:
    string multiplyByDigit(const string& value, char digit) {
        int carry = 0;
        string product;

        for (int index = static_cast<int>(value.size()) - 1; index >= 0; --index) {
            const int current = (value[index] - '0') * (digit - '0') + carry;
            product += static_cast<char>('0' + current % 10);
            carry = current / 10;
        }
        if (carry != 0) {
            product += static_cast<char>('0' + carry);
        }

        reverse(product.begin(), product.end());
        return product;
    }

    string addStrings(const string& a, const string& b) {
        int left = static_cast<int>(a.size()) - 1;
        int right = static_cast<int>(b.size()) - 1;
        int carry = 0;
        string sum;

        while (left >= 0 || right >= 0 || carry != 0) {
            int current = carry;
            if (left >= 0) {
                current += a[left--] - '0';
            }
            if (right >= 0) {
                current += b[right--] - '0';
            }
            sum += static_cast<char>('0' + current % 10);
            carry = current / 10;
        }

        reverse(sum.begin(), sum.end());
        return sum;
    }
};
