"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        
        
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1
            
            
        tail, con = cur, prev
        
        while n:
            third = cur.next
            
            cur.next = prev
            prev = cur
            cur = third
            n -= 1
            
        """
        1(cur) | 2(third) | 3
        1 -> 2 -> 3
        
        prev <- 1(prev)  | 2(cur) | 3
        
        """
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head
        """
        prev(con) | 1(m tail) | 2 | 3 | 4 | 5(n)
        """

"""
Normal Version of reverse linked list
"""

def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        
        while (cur != None):
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp
        
        return prev