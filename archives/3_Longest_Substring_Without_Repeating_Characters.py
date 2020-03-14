class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        
        hash_set = []
        
        ans = 0
        i = 0
        j = 0
        
        while i < n and j < n:
            if s[j] not in hash_set:
                hash_set.append(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                hash_set.remove(s[i])
                i+=1
                
        return ans