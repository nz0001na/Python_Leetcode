'''
20. (easy)

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false


Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

'''

'''
Solution:




'''


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return

        keys = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c in ['{', '(', '[']:
                stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] != keys[c]:
                    return False
                # or stack.pop()
                del stack[-1]


        if len(stack) == 0:
            return True


