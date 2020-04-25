"""
Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.

 

Example 1:

Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"
Example 2:

Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
"   T"
Example 3:

Input: s = "CONTEST IS COMING"
Output: ["CIC","OSO","N M","T I","E N","S G","T"]
"""

class Solution:
    def printVertically(self, s: str) -> List[str]:
        if len(s) == 0:
            return
        if len(s) == 1:
            return [s]
        ans = []
        words = s.split(' ')
        maxLen = max(len(word) for word in words)
        for i in range(maxLen):
            l = []
            for word in words:
                l.append(word[i] if i < len(word) else ' ')
            ans.append(''.join(l).rstrip())
        return ans
        