'''
5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

Approach 1: brute-force method  O(n^3)
Approach 2: slide windows
'''


# brute-force method
def longestPalindromic(s):
    count = len(s)
    maxstr = ''
    if count == 0 or count == 1:
        maxstr = s

    for i in range(count):
        for j in range(i+1, count+1):
            subs = s[i:j]
            resubs = subs[len(subs)::-1]
            if subs == resubs and len(subs) > len(maxstr):
                maxstr = subs
    return maxstr


# slide windows
def longestPalindromic2(s):
    count = len(s)

    def getLength(l, r):
        leng=0
        while(l>=0 and r < count and s[l] == s[r]):
            leng = r - l +1
            l = l -1
            r = r + 1
        return leng

    max_len = 0
    start = 0
    for i in range(0,count):
        cur_len = max(getLength(i,i), getLength(i, i+1))
        if cur_len > max_len:
            max_len = cur_len
            start = int(i-(cur_len - 1)//2)
    return s[start:start+max_len]











s = 'cbbd'
print(longestPalindromic2(s))