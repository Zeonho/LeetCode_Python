"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node
 differ in height by no more than 1.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Maximum Depth
class Solution:
    def check(self, root):
            if root is None:
                return 0
            left  = self.check(root.left)
            right = self.check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        
    def isBalanced(self, root: TreeNode) -> bool:
        return self.check(root) != -1

n = TreeNode(3)
n.left = TreeNode(9)
n.right = TreeNode(20)
n.right.left = TreeNode(15)
n.right.right = TreeNode(7)        
s = Solution().isBalanced(n)
print(s)