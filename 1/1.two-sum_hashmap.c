#include <stdio.h>
#include <stdlib.h>
/*
 * @lc app=leetcode id=1 lang=c
 *
 * [1] Two Sum
 */

// @lc code=start

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *twoSum(int *nums, int numsSize, int target, int *returnSize)
{
    // hash map method.
    int list[numsSize], result[2];
    for (int i = 0; i < numsSize; i++)
    {
        if (list[nums[i]] != NULL)
        {
            result[0] = list[nums[i]];
            result[1] = i;
            return result;
        }
        list[target - nums[i]] = i;
    }
    *returnSize = 0;
    return 0;
}

// @lc code=end
