"""
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.
Example 1:
Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:
Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        c = min(set(s), key = s.count)

        if s.count(c) >= k:
            return len(s)

        return max(self.longestSubstring(t, k) for t in s.split(c))


    def longestSubstring2(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        mydict, myset = {}, set()
        for c in s:
            if c in mydict.keys():
                mydict[c] += 1
            else:
                mydict[c] = 1
            if mydict[c] >= k:
                myset.discard(c)
            else:
                myset.add(c)

        if len(myset) == 0:
            return len(s)
        intervals, start  = [], 0
        while start < len(s):
            if s[start] not in myset:
                i = start
                while start < len(s):
                    if s[start] not in myset:
                        start += 1
                    else:
                        break
                intervals.append((i, start))
            else:
                start += 1
        gMax = 0
        for intervals in intervals:
            gMax = max(gMax, self.longestSubstring(s[intervals[0]:intervals[1]], k))
        return gMax

            
