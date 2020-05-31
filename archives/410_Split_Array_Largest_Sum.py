"""
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.
Note:
If n is the length of array, assume the following constraints are satisfied:
1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:
Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""
from collections import defaultdict
class Solution:
    # Brute Force
    def helper1(self, nums, m):
        if nums == []:
            return 0
        elif m == 1:
            return sum(nums)
        else:
            min_result = float('inf')
            for j in range(1, len(nums) + 1):
                left, right = sum(nums[:j]), self.helper1(nums[j:], m - 1)
                min_result = min(min_result, max(left, right))
            return min_result
    def splitArray1(self, nums: List[int], m: int) -> int:
        return self.helper1(nums, m)
    # Memoization
    def helper2(self, i, nums, m, cache):
        if i == len(nums):
            return 0
        elif m == 1:
            return sum(nums[i:])
        else:
            if i in cache and m in cache[i]:
                return cache[i][m]
            cache[i][m] = float('inf')
            for j in range(1, len(nums) + 1):
                left, right = sum(nums[ i : i + j ]), self.helper(i + j, nums, m - 1, cache)
                cache[i][m] = min(cache[i][m], max(left, right))
                if left > right:
                    break
            return cache[i][m]
    def splitArray2(self, nums, m):
        cache = defaultdict(dict)
        return self.helper(0, nums, m, cache)

    def splitArray(self, nums: List[int], m: int) -> int:
        """
        First, understand WHAT we are binary searching over
        we are doing a binary search over the *search space of possible results*
        What is the search space - what are all possible results?
        For this, We need to know the minimum and maximum possible result
        minimum possible result - largest element in array. Since each element needs
        to be part of some subarray, the smallest we can go is by taking the largest element
        in a subarray by itself 
        a subarray larger than the array itself
        Compute minResult and maxResult boundaries
        """
        low, high, res = max(nums), sum(nums), -1
        while low <= high:
            pivot=(low+high)//2
            if self.isValid(nums,m,pivot):
                res, high = pivot, pivot - 1
            else:
                low = pivot + 1
        return res
    
    def isValid(self, nums, m, pivot):
        chunk, current = 0, 0
        for n in nums:
            current += n
            if current > pivot:
                chunk, current = chunk + 1, n
        return chunk + 1 <= m