"""
Given a 2D grid of 0s and 1s, return the number of elements in the largest square 
subgrid that has all 1s on its border, or 0 if such a subgrid doesn't exist in the 
grid.
"""


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        
        
        
        Max = 0
        M = len(grid)
        N = len(grid[0])
        there_is_one = False
        

        hor = [[0 for i in range(N)] for i in range(M)]
        ver = [[0 for i in range(N)] for i in range(M)]

        if grid[0][0] == 1:
            hor[0][0] = 1
            ver[0][0] = 1
        
        

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    there_is_one = True
                    if not i == j == 0:
                        # skip [0][0]
                        ver[i][j], hor[i][j] = ver[i - 1][j] + 1, hor[i][j - 1] + 1
                    
                    
        print(ver)
        print(hor)
        
        for i in range(M - 1, 0, -1):
            for j in range(N - 1, 0, -1):
                small = min(hor[i][j], ver[i][j])
                while small > Max:
                    if ver[i][j - small + 1] >= small and hor[i - small + 1][j] >= small:
                        Max = small  
                    small -= 1
        
        if there_is_one and Max == 0:
            Max = 1
        
        return Max*Max
