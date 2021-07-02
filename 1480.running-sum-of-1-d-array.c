/*
 * @lc app=leetcode id=1480 lang=c
 *
 * [1480] Running Sum of 1d Array
 */

// @lc code=start
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* runningSum(int* nums, int numsSize, int* returnSize){
    for (int i = 1; i < numsSize; i++)
    {
        nums[i] += nums[i-1];
    }
    *returnSize = numsSize;
    return nums;
}
// @lc code=end

