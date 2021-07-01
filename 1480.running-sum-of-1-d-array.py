#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        list = []
        for i, v in enumerate(nums):
            list.append(sum(nums[0:i+1]))
        return list
# @lc code=end

