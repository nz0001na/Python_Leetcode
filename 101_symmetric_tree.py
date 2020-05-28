'''
101. Symmetric Tree
Easy
https://github.com/grandyang/leetcode/issues/101

Share
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Follow up: Solve it both recursively and iteratively.



'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checksub(left, right):
    if left is None and right is None:
        return True
    if left and right is None or left is None and right or left.val != right.val:
        return False
    return checksub(left.left, right.right) and checksub(left.right, right.left)

# recursive
def isSymmetric(root):
    if root is None:
        return True
    return checksub(root.left, root.right)



# iterative
from queue import Queue
def isSymmetric2(root):
    if root is None:
        return True

    q1 = Queue()
    q2 = Queue()
    q1.put(root.left)
    q2.put(root.right)
    while not q1.empty() and not q2.empty():
        r1 = q1.get()
        r2 = q2.get()
        if r1 is None and r2 or r1 and r2 is None:
            return False
        if r1 and r2 and r1.val != r2.val:
            return False
        if r1 and r2:
            q1.put(r1.left)
            q1.put(r1.right)
            q2.put(r2.right)
            q2.put(r2.left)
    return True


a = TreeNode(3,None,None)
b = TreeNode(4, None,None)
c = TreeNode(2,a,b)
d = TreeNode(4, None, None)
e = TreeNode(3, None, None)
f = TreeNode(2, d, e)
root = TreeNode(1, c, f)

print(isSymmetric2(root))
