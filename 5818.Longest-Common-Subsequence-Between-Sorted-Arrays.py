#
# @lc app=leetcode id=5818 lang=python3
#
# [5818] Longest Common Subsequence Between Sorted Arrays
#

# @lc code=start
class Solution:
    def longestCommomSubsequence(self, arrays: List[List[int]]) -> List[int]:
        result = arrays[0]
        for i in range(1,len(arrays)):
            result = set(result) & set(arrays[i])
        return sorted(result)
# @lc code=end

