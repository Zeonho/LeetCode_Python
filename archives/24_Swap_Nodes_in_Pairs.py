"""
24. Swap Nodes in Pairs
Medium

1720

152

Add to List

Share
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return
        if head.next == None:
            return head
        
        node_lst = []
        ptr = head
        while ptr != None:
            node_lst.append(ptr)
            ptr = ptr.next
            
        node_lst_length = len(node_lst)

        if node_lst_length % 2 == 0:
            for i in range(0, node_lst_length - 1, 2):
                node_lst[i], node_lst[i+1] = node_lst[i+1], node_lst[i]
        else:
            for i in range(0, node_lst_length - 2, 2):
                node_lst[i], node_lst[i+1] = node_lst[i+1], node_lst[i]

        for i in range(0, node_lst_length - 1):
            node_lst[i].next = node_lst[i+1]
            
        node_lst[-1].next = None
        head = node_lst[0]
        return head