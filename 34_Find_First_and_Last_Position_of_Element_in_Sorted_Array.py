"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

class Solution:
    
    # binary scan
    # returns leftmost (or rightmost) index at which 'target' should be inserted in sorted array 'num' via binary search
    def extreme_insertion_index(self, nums, target, leftmost):
        low = 0
        high = len(nums)

        while low < high:
            mid = (low + high)  // 2

            if nums[mid] > target or (leftmost == True and nums[mid] == target):
                high = mid
            else:
                low = mid + 1

            print(high, low)

        
        return low




    
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_idx = self.extreme_insertion_index(nums, target, True)
        
        # assert that 'left_idx' is within the array bounds and that 'target' is actually in 'nums'
        if left_idx == len(nums) or nums[left_idx] != target:
            return[-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]
