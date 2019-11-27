"""
Assume you are an awesome parent and want to give your children some cookies. 
But, you should give each child at most one cookie. 
Each child i has a greed factor gi, which is the minimum size of a cookie that 
the child will be content with; 
and each cookie j has a size sj. 
If sj >= gi, we can assign the cookie j to the child i, 
and the child i will be content. Your goal is to maximize the number of your 
content children and output the maximum number.

Note:
You may assume the greed factor is always positive. 
You cannot assign more than one cookie to one child.
"""

# Thoughts:
# Sort Both list
# Match both list
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # in case there isn't any cookies or kids
		if not g or not s:
			return 0

        # both lists are sorted for simplicity
		g.sort()
		s.sort()        
		res = 0

		while len(s) > 0 and len(g) > 0:        # as long as there's cookie or kid 
			if s[0] >= g[0]:        # check whether the smallest cookie can be given to the least greedy kid
				res += 1        # if so increment res by 1, remove kid and cookie from the list
				s = s[1:]
				g = g[1:]
			else:
				s = s[1:]       # otherwise it means cookie won't be useful

		return res      # when there isn't cookies or kids just return the result