"""
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
"""
class Solution:
    # Brute Force from end of list
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        for i in range(0, m):
            for j in range(n - 1, -1, -1):
                if grid[i][j] < 0:
                    count += 1
                    
                    
        return count

    #  O(m+n) from disscussion
    def countNegatives2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        r = m - 1
        c = 0
        count = 0

        while r >= 0 and c < n:
            if grid[r][c] < 0:
                count += n - c
                r -= 1
            else:
                c += 1
        return count