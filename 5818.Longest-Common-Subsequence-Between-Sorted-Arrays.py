#
# @lc app=leetcode id=5818 lang=python3
#
# [5818] Longest Common Subsequence Between Sorted Arrays
#

# @lc code=start
class Solution:
    def longestCommomSubsequence(self, arrays: List[List[int]]) -> List[int]:
        # result [7,8] will error in [8,7] without sorted function.
        return sorted(set(arrays[0]).intersection(*arrays[1:]))
# @lc code=end

