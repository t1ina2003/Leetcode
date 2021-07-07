/*
 * @lc app=leetcode id=1 lang=javascript
 *
 * [1] Two Sum
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  var result = [];
  for (let first = 0; first < nums.length - 1; first++) {
    for (let second = first + 1; second < nums.length; second++) {
      if (nums[first] + nums[second] == target) {
        result[0] = first;
        result[1] = second;
        return result;
      }
    }
  }
};
// @lc code=end
