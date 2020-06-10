'''
108. Convert Sorted Array to Binary Search Tree
Easy

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth
of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

# binary search: recursive method
def buildtree(nums, low, high):
    if low > high:
        return None

    mid = (low + high) // 2
    cur = TreeNode(nums[mid], None, None)
    cur.left = buildtree(nums, low, mid-1)
    cur.right = buildtree(nums, mid+1, high)
    return cur

def array2BST(nums):
    low = 0
    high = len(nums)-1
    root = buildtree(nums, low, high)
    return root


# binary search: recursive method two
def array2BST2(nums):
    if len(nums) <= 0:
        return None
    low = 0
    high = len(nums)-1
    mid = (low+high)//2
    root = TreeNode(nums[mid], None, None)
    root.left = array2BST2(nums[:mid])
    root.right = array2BST2(nums[mid+1:])
    return root





nums = [-10,-3,0,5,9]
r = array2BST2(nums)
print(r)