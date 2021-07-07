#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        old_biggest = sorted(candies)[-1]
        return [ True if (i+extraCandies)>=old_biggest else False for i in candies]
# @lc code=end

