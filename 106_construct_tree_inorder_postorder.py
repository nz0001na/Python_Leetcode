'''
106. Construct Binary Tree from Inorder and Postorder Traversal
Medium

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary(postorder, inorder):
    cnt = len(postorder)
    if len(postorder) != len(inorder):
        return None
    if cnt <= 0:
        return None

    root = TreeNode(postorder[cnt-1], None, None)
    idx = inorder.index(postorder[cnt-1])
    root.left = binary(postorder[0:idx], inorder[0:idx])
    root.right = binary(postorder[idx:cnt-1], inorder[idx+1:cnt])
    return root

def construct_tree(postorder, inorder):
    cnt = len(postorder)
    if len(postorder) != len(inorder):
        return None
    if cnt <= 0:
        return None

    root = binary(postorder, inorder)
    return root

inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
l = construct_tree(postorder, inorder)
print(l)


