'''
144. Binary Tree Preorder Traversal
Medium

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root, res):
    if not root:
        return
    res.append(root.val)
    if root.left:
        preorder(root.left, res)
    if root.right:
        preorder(root.right, res)


def preorder_recursive(root):
    if not root:
        return

    res = []
    preorder(root, res)
    return res


def preorder_iterative1(root):
    res = []
    stack = []
    cur = root
    while cur or len(stack) > 0:
        while cur:
            res.append(cur.val)
            stack.append(cur)
            cur = cur.left

        cur = stack[len(stack)-1]
        stack.pop()
        cur = cur.right
    return res


def preorder_iterative2(root):
    if not root:
        return None

    res = []
    stack = []
    cur = root
    while cur or len(stack)>0:
        if cur:
            res.append(cur.val)
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack[len(stack)-1]
            stack.pop()
            cur = cur.right
    return res








c = TreeNode(3,None, None)
b = TreeNode(2, c, None)
root = TreeNode(1,None, b)
# print(preorder_recursive(root))
print(preorder_iterative2(root))