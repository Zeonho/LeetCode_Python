"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

Backtracking
"""

"""
# Sliding window?
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        for i in range(1, len(s) + 1):
            # check sub list is equal to its reverse
            if s[:i] == s[i-1::-1]:
                for rest in self.partition(s[i:]):
                    ret.append([s[:i]] + rest)
        if not ret:
            return [[]]
        else:
            return ret