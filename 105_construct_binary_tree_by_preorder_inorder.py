'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = None
        self.right = None

def binary(preorder, inorder):
    cnt = len(preorder)
    if len(preorder) != len(inorder):
        return None
    if cnt <= 0:
        return None

    root = TreeNode(preorder[0], None, None)
    rdx = inorder.index(preorder[0])
    root.left = binary(preorder[1:rdx+1], inorder[0:rdx])
    root.right = binary(preorder[rdx+1:cnt], inorder[rdx+1:cnt])
    return root


def construct_tree(preorder, inorder):
    cnt = len(preorder)
    if len(preorder) != len(inorder):
        return None
    if cnt <= 0:
        return None

    root = binary(preorder, inorder)
    return root




preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = construct_tree(preorder, inorder)
print(root)
