from itertools import accumulate

"""
Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] 
interpreted as a binary number (from most-significant-bit to least-significant-bit.)

Return a list of booleans answer, where answer[i] is true if and only if N_i is 
divisible by 5.

"""

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        return [x == 0 for x in accumulate(A, lambda x, y: (2*x+y)%5)]

    # def prefixesDivBy5(self, A: List[int]) -> List[bool]:
    #     for i in range(1, len(A)):
    #             A[i] += A[i - 1] * 2 % 5
    #     print(A)
    #     return [a % 5 == 0 for a in A]

"""
[0,1,1] -> 0 1 3
[1,0,1,1]
9


[1,0] =  2
[1,0,1] = 5
"""