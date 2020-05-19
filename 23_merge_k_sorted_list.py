'''
23. Merge k Sorted Lists
https://www.youtube.com/watch?v=cyhLf-_PfkY

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


def merge2Lists(l1, l2):
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
        elif cur1.val < cur2.val:
            cur3.next = cur1
            cur1 = cur1.next
        cur3 = cur3.next
    if cur1:
        cur3.next = cur1
    if cur2:
        cur3.next = cur2
    return l3.next



def mergeKLists(lists):
    if len(lists) == 0:
        return None
    while len(lists) > 1:
        tmp_list = []
        for i in range(0, len(lists), 2):
            if i+1 < len(lists):
                tmp_list.append(merge2Lists(lists[i], lists[i+1]))
            elif i+1 == len(lists):
                tmp_list.append(lists[i])
        lists = tmp_list
    return lists[0]



lists = []
a = ListNode(5, None)
b = ListNode(4, a)
l1 = ListNode(1, b)
lists.append(l1)

c = ListNode(4, None)
d = ListNode(3, c)
l2 = ListNode(1, d)
lists.append(l2)

e = ListNode(6, None)
l3 = ListNode(2, e)
lists.append(l3)

# p = merge2Lists(l1, l2)
# print(p)

fl = mergeKLists(lists)
print(fl)

