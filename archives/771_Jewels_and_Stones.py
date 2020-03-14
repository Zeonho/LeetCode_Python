"""
You're given strings J representing the types of stones that are jewels, 
and S representing the stones you have.  Each character in S is a type of stone you have.  
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Note:
    * S and J will consist of letters and have length at most 50.
    * The characters in J are distinct.
"""



class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # First thought: Brute Force
        result = 0
        for c in S:
            if c in J:
                result += 1
        return result
