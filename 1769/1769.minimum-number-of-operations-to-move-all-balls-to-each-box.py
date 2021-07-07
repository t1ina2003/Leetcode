#
# @lc app=leetcode id=1769 lang=python3
#
# [1769] Minimum Number of Operations to Move All Balls to Each Box
#

# @lc code=start
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # init
        result = []
        boxesList = list(map(int, boxes))
        boxesLength = len(boxesList)
        # each answer
        for i in range(0,boxesLength):
            count = 0
            # each box in boxes
            for j in range(0,boxesLength):
                # count distance if the box isn't empty
                if boxesList[j]==1:
                    count += abs(j-i)
            result.append(count)
        return result
# @lc code=end

