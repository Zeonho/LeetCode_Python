"""
In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position you can walk one step to the left, right, up or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.

Too hard.. 
Solution with explaination:
https://leetcode.com/problems/path-with-maximum-gold/discuss/398282/JavaPython-3-BFS-and-DFS-w-comment-brief-explanation-and-analysis.
"""

class Solution:
    def getMaximumGold(self, grid,: List[List[int]]) -> int:
        def dfs(row, col, curgold):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] > 0:
                temp = grid[row][col]
                # Change to 0 so you wont repeat the process
                grid[row][col] = 0
                dfs(row+1, col, curgold + temp)
                dfs(row-1, col, curgold + temp)
                dfs(row, col+1, curgold + temp)
                dfs(row, col-1, curgold + temp)
                # Once you explore all your choices, calculate the max gold you have collected so far
                self.maxgold = max(self.maxgold, curgold + temp)
                grid[row][col] = temp
                
        self.maxgold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    dfs(i, j, 0)
                    
        return self.maxgold
