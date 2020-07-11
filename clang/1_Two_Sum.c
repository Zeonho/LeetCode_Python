/*
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

#include <stdio.h>

#define RET_SIZE 2
typedef struct {
    int value;
    int position;
} NumStruct;
int compareFunction(const void *a, const void *b) {
    return ( ((NumStruct *)a)->value - ((NumStruct *)b)->value );
}

int compareIntFunction(const void *a, const void *b) {
    return ( *(int *)a - *(int *)b );
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    if (nums == NULL || numsSize <= 0) {
        returnSize = 0;
        return NULL;
    }
    *returnSize = (int)RET_SIZE;
    int *ret = (int *)malloc(sizeof(int) * (*returnSize));
    
    NumStruct *numStruct = (NumStruct *)malloc(sizeof(NumStruct) * numsSize);
    
    for (int i = 0; i < numsSize; i++) {
        numStruct[i].value = nums[i];
        numStruct[i].position = i;
    }
    
    qsort(numStruct, numsSize, sizeof(NumStruct), compareFunction);

    NumStruct *l, *r;
    l = numStruct;
    r = numStruct + (numsSize - 1);
    
    while (l < r) {
        int value = l->value + r->value;
        if (value == target) {
            ret[0] = l->position;
            ret[1] = r->position;
            qsort(ret, RET_SIZE, sizeof(int), compareIntFunction);
            return ret;
        } else if (value < target) {
            l++;
        } else {
            r--;
        }
    }
    
    return ret;
}