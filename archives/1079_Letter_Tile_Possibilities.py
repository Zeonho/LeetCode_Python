"""
You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

 

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: "AAABBC"
Output: 188
"""

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = []

        def helper(tiles, curr, k):
            if k == len(curr):
                res.append(curr)
                return
            
            for i in range(len(tiles)):
                helper(tiles[:i] + tiles[i+1:], curr + tiles[i], k)

        for i in range(1, len(tiles) + 1):
            helper(tiles, '', i)

        return len(set(res))