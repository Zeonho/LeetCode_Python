"""
Given an n-ary tree, return the postorder traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
  Follow up:
Recursive solution is trivial, could you do it iteratively?
  Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
  Constraints:
The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack = [root]
        counters = [0]
        retList = []

        while stack:
            # while the current top of the stacck has unseen child
            while counters[-1] < len(stack[-1].children):
                # Add the child to the top of the stack, with a new corresponding counter to the other stack
                stack.append(stack[-1].children[counters[-1]])
                counters.append(0)
            # If the current top of the stack has reached the end of its children list, then we pop it, it's done
            retList.append(stack.pop().val)
            # Pop its counter as well
            counters.pop()
            # Increment the counter of the next top of the stack to begin that search
            if counters:
                counters[-1] += 1
            
        return retList
