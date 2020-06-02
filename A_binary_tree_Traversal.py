'''
Traversal Binary Tree Methods:

** Depth-first Traversal
1. inorder  -- leetcode 94
2. preorder -- leetcode 144
3. postorder -- leetcode 145

-- time complexity: O(n)
-- space complexity: best O(h)
                     worst O(n)
                     average O(logn)


** Breadth-first Traversal
4. level-order -- leetcode 102


https://www.youtube.com/watch?v=A6iCX_5xiU4

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ## 1. inorder
# (1) recursive
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
        return
    res = []
    inorder(root,res)
    return res

# (2) iterative
def inorder_iterative(root):
    if not root:
        return
    res = []
    stack = []
    cur = root
    while cur or len(stack) > 0:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack[len(stack)-1]
        stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res


# ## 2. preorder
# (1) recursive
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

# (2) iterative
def preorder_iterative(root):
    if not root:
        return
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


# ## 3. postorder
# (1) recursive
def postorder(root, res):
    if not root:
        return
    if root.left:
        postorder(root.left, res)
    if root.right:
        postorder(root.right, res)
    res.append(root.val)

def postorder_recursive(root):
    if not root:
        return
    res = []
    postorder(root, res)
    return res

# (2) iterative
def postorder_iterative(root):
    if not root:
        return

    res = []
    stack = []
    stack.append(root)
    while len(stack) > 0:
        cur = stack[len(stack)-1]
        stack.pop()
        res.insert(0, cur.val)
        if cur.left:
            stack.append(root.left)
        if cur.right:
            stack.append(root.right)

    return res


# ## 4. level
# (1) recursive

# (2) iterative
def levelorder_iterative(root):
    import queue

    que = queue.Queue()
    res = []
    que.put(root)
    while que.qsize() > 0:
        cur = que.get()
        res.append(cur.val)

        if cur.left:
            que.put(cur.left)
        if cur.right:
            que.put(cur.right)

    return res






# Input: [1,null,2,3]
#    4
#   /  \
#  1    3
#      /
#     2
# inorder: 1423
# preorder: 4132
# postorder: 1234

a = TreeNode(2, None, None)
b = TreeNode(3, a, None)
c = TreeNode(1, None, None)
root = TreeNode(4, c, b)

print(inorder_recursive(root))
print(inorder_iterative(root))
print(preorder_recursive(root))
print(preorder_iterative(root))
print(postorder_recursive(root))
print(postorder_iterative(root))
print(levelorder_iterative(root))