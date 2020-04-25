"""
On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.

 

Example 1:

Input: [[2]]
Output: 10
Example 2:

Input: [[1,2],[3,4]]
Output: 34
Example 3:

Input: [[1,0],[0,2]]
Output: 16
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46
 

Note:

1 <= N <= 50
0 <= grid[i][j] <= 50
"""
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)
        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r - 1, c), (r + 1, c),  (r,  c - 1), (r, c + 1)):
                        if 0  <= nr < N and 0 <=  nc  < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0
                        ans += max(grid[r][c] - nval, 0)

        return ans

        def surfaceArea2(self, grid: List[List[int]]) -> int:
            n, res = len(grid), 0
            print(n)
            for i in range(n):
                for j in range(n):
                    print(i, j)
                    if grid[i][j]: res += 2 + grid[i][j] * 4
                    if i: res -= min(grid[i][j], grid[i - 1][j]) * 2
                    if j: res -= min(grid[i][j], grid[i][j - 1]) * 2
            return res