'''
44. Reverse String
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


'''


def reverse(s):
    if len(s) > 1:
        mid = (len(s)-1) // 2
        for i in range(mid+1):
            t = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = t
    print(s)

def reverse2(s):
    left = 0
    right = len(s)-1
    while left <= right:
        t = s[left]
        s[left] = s[right]
        s[right] = t
        left += 1
        right -= 1
    print(s)

s = ["h","e","l","l","o"]
print(reverse2(s))