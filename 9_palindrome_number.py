'''
9. Palindrome Number
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?


Approach 1: convert to string
Approach 2: convert last half of input number, and compare with the first half of the number
'''


# convert to string
def isPalindrome(x):
    if x < 0:
        return False
    s = str(x)
    i = 0
    j = len(s)-1
    while(i<j):
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True


def isPalindrome2(x):
    if x < 0: return False
    if x%10 == 0 and x != 0: return False

    revert = 0
    while(revert < x):
        dig = x%10
        revert = revert*10 + dig
        x = x//10

    if x == revert or x == revert//10:
        print(revert)
        return True
    else:
        return False




x = 456541
print(isPalindrome2(x))