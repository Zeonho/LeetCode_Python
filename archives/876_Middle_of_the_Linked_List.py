"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        #  Number of Nodes between 1 and 100
        if head.next == None:
            return head
        lst = []
        ptr = head
        while ptr is not None:
            lst.append(ptr)
            ptr = ptr.next
            
        return lst[len(lst) // 2]