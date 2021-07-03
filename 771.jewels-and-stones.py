# @before-stub-for-debug-begin
from python3problem771 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in list(stones):
            if i in set(jewels):
                count += 1
        return count 
# @lc code=end

