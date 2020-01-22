"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, 
switching the row and column indices of the matrix.


"""

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        R, C = len(A), len(A[0])
        ans = [[None] * R for _ in range(C)]
        print ans
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val
            return ans