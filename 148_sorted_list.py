'''
148. Sort List
Medium
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?



Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []


Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge(l1,l2):
    if l1 is None: return l2
    if l2 is None: return l1
    if l1 is None and l2 is None: return None

    cur1 = l1
    cur2 = l2
    l3 = ListNode(0,None)
    cur3 = None
    if l1.val > l2.val:
        l3=l2
        cur2=cur2.next
    else:
        l3=l1
        cur1=cur1.next
    cur3 = l3


    while cur1 and cur2:
        if cur1.val < cur2.val:
            cur3.next = cur1
            cur1 = cur1.next
        else:
            cur3.next = cur2
            cur2 = cur2.next
        cur3 = cur3.next

    if cur1 is None: cur3.next=cur2
    if cur2 is None: cur3.next = cur1

    return l3


def sort(li):
    if li is None or li.next is None: return li
    fast = li
    slow = li
    tail = li

    while fast and fast.next:
        tail = slow
        fast = fast.next.next
        slow = slow.next
    tail.next=None
    l1 = sort(li)
    l2 = sort(slow)
    return merge(l1, l2)



a1 = ListNode(5,None)
a2 = ListNode(3, a1)
l1 = ListNode(1, a2)

b1 = ListNode(6, None)
b2 = ListNode(4, b1)
l2 = ListNode(2, b2)
l3 = merge(None,l2)



a = ListNode(3,None)
b = ListNode(1, a)
c = ListNode(2, b)
head = ListNode(4, c)



p = sort(head)
print('finished')


