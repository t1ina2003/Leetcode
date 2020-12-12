// @before-stub-for-debug-begin
#include <vector>
#include <string>
#include <algorithm>
#include "commoncppproblem242.h"

using namespace std;
// @before-stub-for-debug-end

/*
 * @lc app=leetcode id=242 lang=cpp
 *
 * [242] Valid Anagram
 */

// @lc code=start
class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        // 很奇怪empty居然判定為正確
        // if (s.empty() || t.empty())
        //     return false;
        if (s.size() != t.size())
            return false;
        std::sort(s.begin(), s.end());
        std::sort(t.begin(), t.end());
        return s == t;
    }
};
// @lc code=end
