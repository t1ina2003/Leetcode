#
# @lc app=leetcode id=1528 lang=python3
#
# [1528] Shuffle String
#

# @lc code=start
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [None]*len(s)
        for i in range(0,len(s)):
            result[indices[i]] = s[i] 
        return ''.join(result)
# @lc code=end

