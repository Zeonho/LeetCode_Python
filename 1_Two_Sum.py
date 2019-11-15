"""
Given an array of integers, return indices of the two numbers such that they add up 
to a specific target.

You may assume that each input would have exactly one solution, and you may not use 
the same element twice.

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution 1 Brute Force:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    return [nums[i]] + [nums[j]]

