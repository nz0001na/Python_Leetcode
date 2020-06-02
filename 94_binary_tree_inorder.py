'''
94. Binary Tree Inorder Traversal
Medium

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive method
def inorder(root, res):
    if not root:
        return
    if root.left:
        inorder(root.left, res)
    res.append(root.val)
    if root.right:
        inorder(root.right, res)


def inorder_recursive(root):
    if not root:
        return None

    res = []
    inorder(root, res)
    print(res)
    return res


# iterative method: stack
def inorder_iterative1(root):
    res = []
    stack = []
    cur = root
    while cur or len(stack)>0:
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack[len(stack)-1]
        stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res



def inorder_iterative2(root):
    res = []
    stack = []
    cur = root
    while cur or len(stack)>0:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack[len(stack)-1]
            stack.pop()
            res.append(cur.val)
            cur = cur.right
    return res









c = TreeNode(3,None, None)
b = TreeNode(2, c, None)
root = TreeNode(1,None, b)
print(inorder_iterative2(root))
