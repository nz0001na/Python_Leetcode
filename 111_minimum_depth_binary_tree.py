'''
111. Minimum Depth of Binary Tree
https://www.youtube.com/watch?v=hmWhJyz5kqc

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

'''

import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def miniDepth(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1

    left = sys.maxsize
    if root.left:
        left = miniDepth(root.left)

    right = sys.maxsize
    if root.right:
        right = miniDepth(root.right)

    return min(left, right) + 1






a = TreeNode(15,None, None)
b = TreeNode(7, None, None)
d = TreeNode(20, a, b)
c = TreeNode(9,None, None)
root = TreeNode(3, c, d)

a = TreeNode(2, None, None)
root = TreeNode(1, a, None)
print(miniDepth(root))