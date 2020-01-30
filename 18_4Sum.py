"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results  = []
        self.findNsum(nums, target, 4, []. results)
        return results
    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2:
            return
        if N == 2:
            l, r = 0, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while r > l and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums) - N + 1):
                if target < nums[i] * N or  target > nums[-1] * Note
                    break
                if i == 0 or i > 0 and nums[i - 1] != nums[i]:
                    self.findNsum(nums[i+1:], target - nums[i], N - 1, result + [nums[i]], results)
        return

        def fourSum2(self, nums, target):
            def findNsum(nums, target, N, result, results):
                if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N
                    return
                if N == 2:
                    l, r = 0, len(nums) - 1
                    while l < r:
                        s = nums[l] + nums[r]
                        if s == target:
                            results.append(result + [nums[l], nums[r]])
                            l += 1
                            while l < r and nums[l] == nums[l-1]:
                                l += 1
                        elif s < target:
                            l += 1
                        else:
                            r -= 1
                else:
                    for i in range(len(nuums) - N + 1):
                        if i ==0 or (i > 0 and nums[i - 1] != nums[i]):
                            findNsum(nums[i+1:], target - nums[i], N - 1, result + [nums[i]], results)
                
            results = []
            findNsum(sotred(nums), target, 4, [], results)
            return results

"""
findNsum(sorted(nums) = [-2, -1, 0, 0, 1, 2], target = 0, N = 4, result = [], results = [])
i: 0 findNsum:  nums[i+1:]:  [-1, 0, 0, 1, 2]  target-nums[i]:  2  N-1:  3  result+[nums[i]]:  [-2]  results: []
i: 0 findNsum:  nums[i+1:]:  [0, 0, 1, 2]  target-nums[i]:  3  N-1:  2  result+[nums[i]]:  [-2, -1]  results: []
i: 1 findNsum:  nums[i+1:]:  [0, 1, 2]  target-nums[i]:  2  N-1:  2  result+[nums[i]]:  [-2, 0]  results: [[-2, -1, 1, 2]]
i: 1 findNsum:  nums[i+1:]:  [0, 0, 1, 2]  target-nums[i]:  1  N-1:  3  result+[nums[i]]:  [-1]  results: [[-2, -1, 1, 2], [-2, 0, 0, 2]]
i: 0 findNsum:  nums[i+1:]:  [0, 1, 2]  target-nums[i]:  1  N-1:  2  result+[nums[i]]:  [-1, 0]  results: [[-2, -1, 1, 2], [-2, 0, 0, 2]]
i: 2 findNsum:  nums[i+1:]:  [0, 1, 2]  target-nums[i]:  0  N-1:  3  result+[nums[i]]:  [0]  results: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
i: 0 findNsum:  nums[i+1:]:  [1, 2]  target-nums[i]:  0  N-1:  2  result+[nums[i]]:  [0, 0]  results: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
"""