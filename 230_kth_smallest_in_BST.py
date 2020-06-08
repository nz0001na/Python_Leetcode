'''
230. Kth Smallest Element in a BST
Medium

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth
smallest frequently? How would you optimize the kthSmallest routine?

Constraints:
The number of elements of the BST is between 1 to 10^4.
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#  use inorder travesal, get a ascending sort array, return the kth element
#  iterative method
def kthsmall(root, k):
    if not root:
        return None
    # res = []
    stack = []
    cur = root
    timer = 0
    while cur or len(stack) > 0:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack[len(stack)-1]
        # res.append(cur.val)
        timer += 1
        if timer == k:
            return cur.val
        stack.pop()
        cur = cur.right

# recursive, get res[k-1]
def inorder(root, res):
    if not root:
        return
    if root.left:
        inorder(root.left, res)
    res.append(root.val)
    if root.right:
        inorder(root.right, res)

def kthsmall2(root, k):
    if not root:
        return
    res = []
    inorder(root, res)
    return res[k-1]


# recursive, get kth
def inorder3(root, k, res):
    if not root:
        return
    if root.left:
        inorder3(root.left, k, res)
    res.append(root.val)
    if len(res) == k:
        return
    if root.right:
        inorder3(root.right, k, res)


def kthsmall3(root, k):
    if not root:
        return
    res = []
    inorder3(root, k, res)
    return res[k-1]

# root = [3, 1, 4, null, 2]
# k = 1
   #   3
   #  / \
   # 1   4
   #  \
   #   2
# Output: 1
a = TreeNode(2, None, None)
b = TreeNode(1, None, a)
c = TreeNode(4, None, None)
root = TreeNode(3, b, c)
k = 1
print(kthsmall3(root, k))