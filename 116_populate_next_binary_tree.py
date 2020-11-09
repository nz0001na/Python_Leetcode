'''
116. Populating Next Right Pointers in Each Node
Medium
You are given a perfect binary tree where all leaves are on the same level,
and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node,
the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


Example 1:



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val=val
        self.left=left
        self.right=right
        self.next = next

def populatetree(root):
    if root is None: return None
    root.next=None
    # import queue
    # que = queue.Queue()

    from collections import deque
    que = deque()
    que.append(root)

    print(len(que))
    while len(que)>0:
        size = len(que)
        for i in range(0,size):
            cur = que.popleft()
            if i<size-1:
                cur.next=que[0]
            if cur.left: que.append(cur.left)
            if cur.right: que.append(cur.right)

    return root



def recur2(root):
    if root is None: return None
    if root.left:
        root.left.next=root.right
        if root.next:
            root.right.next=root.next.left
        else:
            root.right.next=None
        recur2(root.left)
        recur2(root.right)

    return root








a = TreeNode(4,None,None,None)
b = TreeNode(5,None,None,None)
c = TreeNode(2,a,b,None)

d = TreeNode(6,None,None,None)
e = TreeNode(7,None,None,None)
f = TreeNode(3,d,e,None)
root = TreeNode(1,c,f,None)

p = populatetree(root)
# p=recur2(root)
print('finish')
