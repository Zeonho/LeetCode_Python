"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
 
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
 
The largest rectangle is shown in the shaded area, which has area = 10 unit.
  Example:
Input: [2,1,5,6,2,3]
Output: 10
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        maxarea = 0
        for i in range(len(heights)):
            while (len(stack) > 1 and heights[stack[-1]] >= heights[i]):
                maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        
        while (stack[-1] != -1):
            maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        
        return maxarea
        
