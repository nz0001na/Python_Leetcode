'''
125. Valid Palindrome
Easy

Given a string, determine if it is a palindrome, considering only alphanumeric characters
and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false

'''

def validpalindrome(s):
    if len(s)==0:
        return True

    stack = []
    ss = ''
    for ch in s:
        if ch.isalnum():
            ss += ch
            stack.append(ch)

    res = ''
    while len(stack):
        res += stack.pop()

    return ss.lower() == res.lower()


def validpalindrome2(s):
    left = 0
    right = len(s)-1
    while left < right:
        if not s[left].isalnum():
            left +=1
        if not s[right].isalnum():
            right -= 1
        if s[left].isalnum() and s[right].isalnum():
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
    return True




s = "A man, a plan, a canal: Panamaa"
s = ''
print(validpalindrome2(s))