'''
28. Implement strStr()
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

def strStr(haystack, needle):
    count = len(needle)
    if count == 0:
        return 0
    if len(haystack)==0 or len(haystack) < len(needle):
        return -1


    for i in range(len(haystack)-count+1):
        s = haystack[i:i+count]
        if s == needle:
            return i
    if i >= len(haystack) -count :
        return -1



haystack = "aa"
needle = "aaa"
print(strStr(haystack, needle))