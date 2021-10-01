#
# @lc app=leetcode id=1720 lang=python3
#
# [1720] Decode XORed Array
#

# @lc code=start
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # arr = []*n
        # encoded = []*n-1
        # encoded[i] = arr[i] XOR arr[i + 1]
        ans = [first]
        for i in range(0,len(encoded)):
            ans.append(encoded[i] ^ ans[i])
        return ans
# @lc code=end

