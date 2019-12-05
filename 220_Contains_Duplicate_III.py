"""
Given an array of integers, find out whether there are two distinct indices i and j in the array 
such that the absolute difference between nums[i] and nums[j] is at most t and the absolute 
difference between i and j is at most k.
"""

"""
abs(nums[i] - nums[j]) = t
abs(i - j) = k
"""

class Solution:
    # Idea of Bucket Sort
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0 or k < 0:
            return False

        # Bucket sort. Each bucket has size of t. For each number, the possible
        # candidate can only be in the same bucket or the two buckets besides.
        # Keep as many as k buckets to ensure that the difference is at most k.
        buckets = {}
        for i, v in enumerate(nums):
            # t == 0 is a special case where we only have to check the bucket
            # that v is in.
            bucketNum, offset = (v / t, 1) if t else (v, 0)
            for idx in range(bucketNum - offset, bucketNum + offset + 1):
                if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                    return True

            buckets[bucketNum] = nums[i]
            if len(buckets) > k:
                # Remove the bucket which is too far away. Beware of zero t.
                del buckets[nums[i - k] / t if t else nums[i - k]]

        return False


s = Solution()
nums = [1,2,3,1]
k = 3
t = 0
print(s.containsNearbyAlmostDuplicate(nums, k, t))