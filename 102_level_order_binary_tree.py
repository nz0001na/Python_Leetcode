'''
102. Binary Tree Level Order Traversal
Medium

https://github.com/grandyang/leetcode/issues/102


Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

import queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# nodes of all levels are put in one array
def levelorder_iterative(root):
    que = queue.Queue()
    que.put(root)
    res = []
    while not que.empty():
        cur = que.get()
        if cur.left:
            que.put(cur.left)
        if cur.right:
            que.put(cur.right)

        res.append(cur.val)
    return res


# nodes in each level are put in separate array
def levelorder_iterative2(root):
    if not root:
        return
    que = queue.Queue()
    res = []
    que.put(root)
    while not que.empty():
        size = que.qsize()
        subres = []
        for i in range(size):
            cur = que.get()
            subres.append(cur.val)
            if cur.left:
                que.put(cur.left)
            if cur.right:
                que.put(cur.right)
        res.append(subres)

    return res



# recursive
def levelorder(root, level, res):
    if not root:
        return
    if len(res) == level:
        res.append([])
    res[level].append(root.val)
    if root.left:
        levelorder(root.left, level+1, res)
    if root.right:
        levelorder(root.right, level+1, res)

def levelorder_recursive(root):
    res = []
    levelorder(root, 0, res)
    return res





  #
  #   3
  #  / \
  # 9  20
  #   /  \
  #  15   7

a = TreeNode(15, None, None)
b = TreeNode(7, None, None)
c = TreeNode(20, a, b)
d = TreeNode(9, None, None)
root = TreeNode(3, d, c)

print(levelorder_iterative(root))
print(levelorder_iterative2(root))
print(levelorder_recursive(root))