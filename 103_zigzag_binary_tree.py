'''
103. Binary Tree Zigzag Level Order Traversal
Medium

Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

'''
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def zigzagbinary(root):
    if not root:
        return None
    from copy import deepcopy
    q = []
    res = []
    flag = 1
    q.insert(0,root)
    while len(q) > 0:
        li = deepcopy(q)
        subres = []
        for i in range(len(li)):
            t = li[i]
            q.pop()
            if flag == -1:
                if t.right: q.insert(0,t.right)
                if t.left: q.insert(0, t.left)
            else:
                if t.left: q.insert(0,t.left)
                if t.right: q.insert(0,t.right)
            subres.append(t.val)
        flag = -flag
        res.append(subres)
    return res



a = TreeNode(4, None, None)
a1 = TreeNode(6, None, None)
b = TreeNode(2, a, a1)
c = TreeNode(5, None, None)
c1 = TreeNode(7, None, None)
d = TreeNode(3, c1, c)
root = TreeNode(1, b, d)
print(zigzagbinary(root))

#  3
# / \
# 9  20
#    / \
#   15 7