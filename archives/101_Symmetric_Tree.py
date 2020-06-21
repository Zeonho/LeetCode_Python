"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up: Solve it both recursively and iteratively.
"""
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        q = collections.deque()
        q.append(root.left)
        q.append(root.right)

        """
        1. not left and not right --- true
        2. left and not right --- false
        3. left and right --- > left == right ? true : false
        4. not left and right --- false
        """
        while q:
            t1, t2 = q.popleft(), q.popleft()
            if t1 == None and t2 == None:
                continue
            if t1 == None or t2 == None:
                return False
            if t1 and t2 and t1.val != t2.val:
                return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True

