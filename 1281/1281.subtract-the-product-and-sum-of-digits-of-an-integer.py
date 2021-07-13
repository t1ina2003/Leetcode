#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        while n>0:
            num = n % 10
            product *= num
            sum += num
            n = int(n/10)
        return product - sum
# @lc code=end

