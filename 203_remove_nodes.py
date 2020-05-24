'''
203. Remove Linked List Elements
https://www.youtube.com/watch?v=gfFn-OXxcgU

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# add an extra node
def remove(head, val):
    if head is None:
        return None

    cur = head
    p = ListNode('h', head)
    pre = p
    while cur:
        if cur.val == val:
            pre.next = cur.next
        else:
            pre = pre.next
        cur = cur.next
    return p.next

#
def remove2(head, val):
    while head and head.val == val:
        head = head.next

    cur = head
    while cur and cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head



a = ListNode(5, None)
b = ListNode(3,a)
c = ListNode(2, b)
head = ListNode(1,c)

ls = remove2(head, 1)
print(ls)