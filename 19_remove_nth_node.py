'''
19. Remove Nth Node From End of List
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?


'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def removeNthFromEnd(head, n):
    end = head
    len = 1
    while(end.next):
        end = end.next
        len += 1
    # end.next = head

    index = len - n + 1
    cur = head
    i = 1
    if index == 1:
        head = head.next
        cur.next = None
    else:
        while(cur.next and i < index-1):
            cur = cur.next
            i += 1
        if i + 1 == index:
            remove = cur.next
            if remove.next:
                cur.next = remove.next
                remove.next = None
            else:
                cur.next = None

    return head









a = ListNode(5, None)
b = ListNode(4, a)
c = ListNode(3, b)
d = ListNode(2, c)
head = ListNode(1, d)
# print(head)
p = removeNthFromEnd(head, 1)
print('d')
