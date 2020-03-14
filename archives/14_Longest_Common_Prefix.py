"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution:
    
    def longestCommonPrefixRec(self, strs: List[str], common_str: str, index: int) -> str:
        same_len_mark = False
        
        
        
       

        for s in strs:
            if index > len(s) - 1:
                return common_str[:index]
            
             # [a, a]
            if index == len(s) - 1:
                same_len_mark = True
                
            if s[index] != common_str[index]:
                return common_str[:index]
            
            
        
        if same_len_mark:
            return common_str
       
        
        
        return self.longestCommonPrefixRec(strs, common_str + strs[0][index + 1], index + 1)

        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs[0]) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        return self.longestCommonPrefixRec(strs, strs[0][0], 0)
        