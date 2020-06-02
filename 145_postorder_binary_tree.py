'''
145. Binary Tree Postorder Traversal
Hard

https://www.youtube.com/watch?v=A6iCX_5xiU4

Given a binary tree, return the postorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder(root, res):
    if not root:
        return None
    if root.left:
        postorder(root.left, res)
    if root.right:
        postorder(root.right, res)
    res.append(root.val)


def postorder_recursive(root):
    if not root:
        return None
    res = []
    postorder(root,res)
    return res


# iterative using stack
def postorder_iterative1(root):
    if not root:
        return None
    res = []
    stack = []
    stack.append(root)
    while len(stack) > 0:
        cur = stack[len(stack)-1]
        stack.pop()
        res.insert(0,cur.val)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)

    return res



c = TreeNode(3,None, None)
b = TreeNode(2, c, None)
root = TreeNode(1,None, b)
# print(postorder_recursive(root))
print(postorder_iterative1(root))