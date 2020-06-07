"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.
However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.
You need to return the least number of intervals the CPU will take to finish all the given tasks.
  Example:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
  Constraints:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""

from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        for task, freq in Counter(tasks).items():
            heapq.heappush(heap, (-freq, task))
        steps = 0
        while heap:
            add_back = []
            for _ in range(n + 1):
                steps += 1
                if heap:
                    priority, task = heapq.heappop(heap)
                    if priority != -1:
                        heapq.heappush(add_back, (priority + 1, task))
                if not heap and not add_back:
                    break
                    
            for i in add_back:
                heapq.heappush(heap, i)
        return steps
