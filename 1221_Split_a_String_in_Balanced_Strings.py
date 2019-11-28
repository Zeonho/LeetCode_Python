"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        match = 0
        counter = 0
        for c in s:
            if c == 'L': 
                counter += 1
            if c == 'R': 
                counter -= 1
            if counter == 0: 
                match += 1
        return match