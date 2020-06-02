'''
107. Binary Tree Level Order Traversal II
Easy

Share
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelorder_bottom_up(root):
    import queue

    q = queue.Queue()
    res = []
    q.put(root)
    while not q.empty():
        subres = []
        for i in range(0, q.qsize()):
            cur = q.get()
            subres.append(cur.val)
            if cur.left:
                q.put(cur.left)
            if cur.right:
                q.put(cur.right)
        res.insert(0, subres)

    return res


#    3
#   / \
#  9  20
#    / \
#   15  7
#

a = TreeNode(15, None, None)
b = TreeNode(7, None, None)
c = TreeNode(20, a, b)
d = TreeNode(9, None, None)
root = TreeNode(3, d, c)

print(levelorder_bottom_up(root))