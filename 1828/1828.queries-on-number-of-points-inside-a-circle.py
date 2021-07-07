#
# @lc app=leetcode id=1828 lang=python3
#
# [1828] Queries on Number of Points Inside a Circle
#

# @lc code=start
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        for i in queries:
            result.append(self.countInCircle(points,i))
        return result
    def countInCircle(self, points: List[List[int]], queries: List[int]) -> int:
        count = 0
        for i in points:
            if ((i[0]-queries[0])**2 + (i[1]-queries[1])**2)**0.5 <= queries[2]:
                count += 1
        return count
# @lc code=end

