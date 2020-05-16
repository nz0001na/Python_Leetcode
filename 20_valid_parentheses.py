'''
20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true

'''


def valid_parentheses(s):
    stack = []

    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')':
            if len(stack) > 0:
                if stack[len(stack) - 1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                return False
        if ch == '}':
            if len(stack) > 0:
                if stack[len(stack) - 1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                return False
        if ch == ']':
            if len(stack) > 0:
                if stack[len(stack)-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                return False

    if len(stack) == 0:
        return True


def valid_parentheses2(s):
    map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = []

    for ch in s:
        if ch=='(' or ch == '[' or ch=='{':
            stack.append(ch)
        else:
            if len(stack) > 0:
                if stack[len(stack)-1] == map.get(ch):
                    stack.pop()
                else:
                    return False
            else:
                return False
    if len(stack) ==0:
        return True
    else:
        return False


s = '{[]}'
print(valid_parentheses2(s))