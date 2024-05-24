'''
143: medium

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes.
Only nodes themselves may be changed.


Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:
    The number of nodes in the list is in the range [1, 5 * 10^4].
    1 <= Node.val <= 1000

'''

'''
**********************************************************************
Solution:

define 4 pointers:  cur, post; q, p;
   cur: current node
   post: cur.next
   
   p: last node of current linked list
   q: previous node of p
   
(1) outer while loop:
    deal with the whole linked list
    
(2) inner while loop:
    search from node 'post', to the end.
    set p as last node, q as last second node
    
    then, cur points to p, p points to post, q becomes the last node of list (q.next=None),
        and cur points to post, post points to post.next.
    

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return

        cur = head
        post = cur.next
        while (cur and cur.next):
            p = cur.next
            q = cur.next
            while (p and p.next):
                q = p
                p = p.next

            cur.next = p
            p.next = post
            q.next = None
            cur = post
            post = post.next

        return head

