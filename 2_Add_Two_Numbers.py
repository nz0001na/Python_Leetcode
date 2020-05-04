'''
2. Add Two Numbers:
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def Add(self, data):
        new_node = Node(data)
        if self.head:
            p = self.head
            while (p.next):
                p = p.next
            p.next = new_node
        else:
            self.head = new_node

    def print_list(self):
        p = self.head
        stra = ''
        while(p.next):
            stra = stra + str(p.data) + ' -> '
            p = p.next
        print(stra + str(p.data))

def addTwoNumbers(l1, l2):
    l1.print_list()
    l2.print_list()
    p = l1.head
    q = l2.head

    l3 = LinkList()
    cur = l3.head

    flag = 0
    while(p and q):
        if flag == 1:
            sum = 1 + p.data + q.data
        else:
            sum = p.data + q.data
        if sum >= 10:
            flag = 1
            sum = sum -10
        else:
            flag = 0
        # print(node.data)
        l3.Add(sum)
        p = p.next
        q = q.next

    while(p):
        if flag == 0:
            sum = p.data
        else:
            sum = p.data + 1
        if sum >= 10:
            sum = sum - 10
            flag = 1
        else:
            flag = 0
        l3.Add(sum)
        p = p.next

    while(q):
        if flag == 0:
            sum = q.data
        else:
            sum = q.data + 1
        if sum >=10:
            sum = sum - 10
            flag = 1
        else:
            flag = 0
        l3.Add(sum)
        q = q.next

    if flag == 1:
        l3.Add(1)

    l3.print_list()





# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

Node1 = Node(2)
Node2 = Node(4)
# Node3 = Node(3)

NodeA = Node(5)
NodeB = Node(6)
NodeC = Node(4)

l1 = LinkList()
l1.head = Node1
Node1.next = Node2
Node2.next = None
# Node3.next = None

l2 = LinkList()
l2.head = NodeA
NodeA.next = NodeB
NodeB.next = NodeC
NodeC.next = None

addTwoNumbers(l1, l2)

