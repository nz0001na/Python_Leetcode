'''
131. Palindrome Partitioning
Medium

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Example:
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]


definition::::
    pal·in·drome
    /ˈpalənˌdrōm/
    a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
'''

def isPalindrome(s, start, end):
    if start>end:
        return False
    # if start==end:
    #     return True

    while start<end:
        if s[start] is not s[end]:
            return False
        start=start+1
        end = end-1
    return True

import copy

def helper(s, start, out, res):
    if start == len(s):
        oo = copy.deepcopy(out)
        res.append(oo)
        return
    for i in range(start, len(s)):
        if isPalindrome(s, start, i) is False:
            continue
        out.append(s[start:i+1])
        helper(s, i+1, out, res)
        out.pop()



def partition(s):
    if len(s) == 0:
        return False
    # print(isPalindrome(s, 0, len(s)-1))
    res = []
    out = []
    helper(s, 0, out, res)
    return res







s = 'a'
print(partition(s))