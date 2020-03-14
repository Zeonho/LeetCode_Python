"""
The Hamming distance between two integers is the number of positions at which the 
corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.
"""

class Solution:
    def hammingDistance(self, x:int, y:int) -> int:
        d = 0
        while x > 0 or y > 0:
            d += (x % 2) ^ (y % 2)
            print("x % 2: ", x % 2)
            print("y % 2: ", y % 2)
            x = x >> 1
            y = y >> 1
        
        return d



s = Solution
s.hammingDistance(1, 4)