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
    // brute method
    int *ret = (int *)malloc(sizeof(int) * 2);
    for (ret[0] = 0; ret[0] < numsSize - 1; ret[0]++)
    {
        for (ret[1] = ret[0] + 1; ret[1] < numsSize; ret[1]++)
        {
            if (ret[0] + ret[1] == target)
            {
                *returnSize = 2;
                return ret;
            }
        }
    }
    *returnSize = 0;
    return NULL;
}

// @lc code=end
