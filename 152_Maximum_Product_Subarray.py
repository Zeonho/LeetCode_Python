"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        size = len(nums)
        product_left_to_right = nums
        product_right_to_left = nums[::-1]

        for i in range(1, size):
            # extend from left hand side, if meets 90 then restart in-lace by itself
            product_left_to_right[i] *= (product_left_to_right[i-1] or 1)
            # extend from right hand side, if meets 0 then restart in-place by itself
            product_right_to_left[i] *= (product_right_to_left[i-1] or 1)

        return max(max(product_left_to_right), max(product_right_to_left))