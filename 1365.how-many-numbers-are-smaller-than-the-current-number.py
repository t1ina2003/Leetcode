#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # init var
        map = {}
        numsLength = len(nums)
        # sort nums
        sortNums = sorted(nums)
        # record sorted position (which happened to be numbers)
        for i in range(0,numsLength):
            if sortNums[i] not in map:
                map[sortNums[i]] = i
        # rewrite nums according to map.
        for j in range(0,numsLength):
            nums[j] = map[nums[j]]
        return nums
# @lc code=end

