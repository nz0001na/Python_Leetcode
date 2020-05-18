'''
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4


'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# create another new linklist
def mergeTwoLists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    cur1 = l1
    cur2 = l2
    l3 = ListNode('h', None)
    pre3 = l3
    while cur1 and cur2:
        if cur1.val >= cur2.val:
            pre3.next = ListNode(cur2.val, None)
            pre3 = pre3.next
            cur2 = cur2.next
        elif cur1.val < cur2.val:
            pre3.next = ListNode(cur1.val, None)
            pre3 = pre3.next
            cur1 = cur1.next
    if cur1:
        while cur1:
            pre3.next = ListNode(cur1.val, None)
            pre3 = pre3.next
            cur1 = cur1.next
    if cur2:
        while cur2:
            pre3.next = ListNode(cur2.val,None)
            pre3 = pre3.next

    return l3.next


def mergeTwoLists2(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    cur1 = l1
    cur2 = l2
    l3 = ListNode('h',None)
    cur3 = l3
    while cur1 and cur2:
        if cur1.val >= cur2.val:
            cur3.next = cur2
            cur2 = cur2.next
            cur3 = cur3.next
        elif cur1.val < cur2.val:
            cur3.next = cur1
            cur1 = cur1.next
            cur3 = cur3.next
    if not cur1:
        cur3.next = cur2
        # cur3 = cur3.next
    if not cur2:
        cur3.next = cur1
        # cur3 = cur3.next
    return l3.next


a = ListNode(4, None)
b = ListNode(2, a)
head1 = ListNode(1, b)


c = ListNode(4, None)
d = ListNode(2, c)
head2 = ListNode(1, d)

# head2 = ListNode(2,None)
# head1 = ListNode(5,None)
# head2 = None
# head1 = None

l3 = mergeTwoLists2(head1, head2)
print(l3)