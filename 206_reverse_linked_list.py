'''
206. Reverse Linked List
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

Methods:
    1. iterative
    2. recursive
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# iterative - use extra linked list
def reverse(head):
    if head is None:
        return
    cur = head
    p = ListNode(head.val, None)
    cur = cur.next
    while cur:
        p = ListNode(cur.val, p)
        cur = cur.next
    return p

# iterative - in place
def reverse2(head):
    if head is None:
        return None
    if head.next is None:
        return head

    cur = head
    pre = None
    next = cur
    while cur:
        next = next.next
        cur.next = pre
        pre = cur
        cur = next
    return pre


# recursive
def reverse_rec(head):
    if head is None or head.next is None:
        return head

    nh = reverse_rec(head.next)
    head.next.next = head
    head.next = None

    return nh


a = ListNode(5, None)
b = ListNode(4, a)
c = ListNode(3, b)
d = ListNode(2,c)
head = ListNode(1,d)

# head = ListNode(1,None)
ls = reverse_rec(head)
print(ls)