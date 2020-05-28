'''
155. Min Stack
Easy
https://github.com/grandyang/leetcode/issues/155
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:

Methods pop, top and getMin operations will always be called on non-empty stacks.
'''


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.len = 0
        self.min = []

    def push(self, x: int) -> None:
        if self.len == 0:
            self.min.append(x)
        else:
            self.min.append(min(self.min[self.len-1], x))
        self.len += 1
        self.items.append(x)

    def pop(self) -> None:
        if self.len > 0:
            self.min.pop()
            self.items.pop()
            self.len -= 1

    def top(self) -> int:
        return self.items[self.len-1]

    def getMin(self) -> int:
        return self.min[self.len-1]




# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(4)
obj.push(3)
obj.push(8)
obj.push(1)

obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)