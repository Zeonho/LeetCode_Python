"""
Sort a linked list in O(n log n) time using constant space complexity.
Example 1:
Input: 4->2->1->3
Output: 1->2->3->4
Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                # tail.next, tail, h1 = h1, h1, h1.next
                tail = h1
                tail.next = h1
                h1 = h1.next
            else:
                # tail.next, tail, h2 = h2, h2, h2.next
                tail = h2
                tail.next = h2
                h2 = h2.next

        tail.next = h1 or h2
        return dummy.next
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        # pre, slow, fast = None, head, head
        pre = None
        slow = head
        fast = head
        while fast and fast.next:
            # pre, slow, fast = slow, slow.next, fast.next.next
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None

        return self.merge(self.sortList(head),self.sortList(slow))




        
