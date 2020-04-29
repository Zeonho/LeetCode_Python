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
Note:
All given inputs are in lowercase letters a-z.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None or len(strs) == 0: return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(len(strs)):
                if i == len(strs[j]) or strs[j][i]!= c:
                    return strs[0][:i]           
            
        
        return strs[0]

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        def longestCommonPrefix(strs,  l,  r) :
            if l == r:
                return strs[l]
            else:
                mid = (l + r)/2
                lcpLeft = longestCommonPrefix(strs, l , mid)
                lcpRight = longestCommonPrefix(strs, mid + 1,r)
                return commonPrefix(lcpLeft, lcpRight)
   


        def commonPrefix(left, right):
            minL = min(len(left), len(right));       
            for i in range(minL):
                if left[i] != right[i]:
                    return left[:i]
            
            return left.substring[:minL]


        if strs == None or len(strs) == 0: return "";    
        return longestCommonPrefix(strs, 0 , strs.length - 1)




