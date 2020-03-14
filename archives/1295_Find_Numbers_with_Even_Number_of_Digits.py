"""
1295. Find Numbers with Even Number of Digits
Easy

145

23

Add to List

Share
Given an array nums of integers, return how many of them contain an even number of digits.
 

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
 

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 10^5
"""


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        ret = 0
        
        for n in nums:
            str_n = str(n)
            if n != 0 and len(str_n) %2 == 0:
                ret += 1
                
        
        return ret