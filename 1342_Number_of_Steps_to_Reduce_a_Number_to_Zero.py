"""
1342. Number of Steps to Reduce a Number to Zero
Easy

86

7

Add to List

Share
Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

 """

class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while num:
            if (num != 1) and (num & 1 == 1):
                count += 1
            num = num >> 1
            count += 1
        return count