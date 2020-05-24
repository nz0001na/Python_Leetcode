'''
104. Maximum Depth of Binary Tree
(1) https://www.youtube.com/watch?v=to2XMEXE1ms
    https://www.youtube.com/watch?v=D2cFSDfg0So
    https://www.youtube.com/watch?v=YT1994beXn0
    https://www.youtube.com/watch?v=jN7xVW2Qtbs
(2)
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# top-down method
def maxDepth(root):
    if root == None:
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return max(left, right) + 1



a = TreeNode(15,None,None)
b = TreeNode(7,None, None)
c = TreeNode(20, a, b)
d = TreeNode(9,None,None)
root = TreeNode(3, d, c)
print(maxDepth(root))