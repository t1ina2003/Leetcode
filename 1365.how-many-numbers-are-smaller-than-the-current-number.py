#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # init var
        result = []
        numsLength = len(nums)
        # check each position in nums
        for i in range(0,numsLength):
            count = 0
            for j in range(0,numsLength):
                if nums[j]<nums[i]:
                    count += 1
            result.append(count)
        return result
# @lc code=end

