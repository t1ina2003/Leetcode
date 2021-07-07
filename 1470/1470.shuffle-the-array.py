#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(0,len(nums)//2):
            result.append(nums[i])
            result.append(nums[i+len(nums)//2])
        return result
# @lc code=end

