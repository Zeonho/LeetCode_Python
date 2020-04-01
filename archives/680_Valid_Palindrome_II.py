"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""
class Solution:
#     def check(self, s: str) -> bool:
#         return s[::-1] == s
#     def validPalindrome(self, s: str) -> bool:
#         # Brute Force (Time limit exit)
#         if len(s) == 0:
#             return True
#         if len(s) == 1:
#             return True
#         if self.check(s):
#             return True
        
        
#         for i in range(len(s)):
#             if self.check(s[:i] + s[i + 1:]):
#                 return True
            
#         return False
    def validPalindrome(self, s):
        if s == s[::-1]:
            return True
        for i in range(len(s) - 1):
            if s[i] != s[-i-1]:
                return s[i:-i-2] == s[i+1:-i-1][::-1] or s[i+1:-i-1] == s[i+2:len(s)-i][::-1]
        return False