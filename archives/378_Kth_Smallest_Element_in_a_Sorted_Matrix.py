"""
378. Kth Smallest Element in a Sorted Matrix
Medium

1750

105

Add to List

Share
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
"""
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or k < 1:
            return
        
        s = set()
        s.add((0, 0))
        heap = [(matrix[0][0], 0, 0)]

        while k > 1:
            top = heapq.heappop(heap)
            row, col = top[1], top[2]

            if col + 1 < len(matrix[0]) and (row, col + 1) not in s:
                heapq.heappush(heap, (matrix[row][col+1], row, col + 1))
                s.add((row, col + 1))

            if row + 1 < len(matrix) and (row + 1, col) not in s:
                heapq.heappush(heap, (matrix[row+1][col], row + 1, col))
                s.add((row+1, col))
            k -= 1

        return heap[0][0]

    def find_Kth_smallest(matrix, k):
        minHeap = []

        # put the 1st element of each row in the min heap
        # we don't need to push more than 'k' elements in the heap

        for i in range(min(k, len(matrix))):
            heappush(minHeap, (matrix[i][0], 0, matrix[i]))

        # take the smallest element from the min heap, if the runnign count is equal to k' return the number
        #  if the row of the top element has more elements, add the next element to the heap
        numberCount, number = 0, 0
        while minHeap:
            number, i, row = heappop(minHeap)
            nunberCount += 1
            if numberCount == k:
                break
            if len(row) > i + 1
                heappush(minHeap, (row[i+1], i+1, row))
        return number

