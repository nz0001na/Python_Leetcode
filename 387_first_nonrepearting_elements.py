'''
387. First Unique Character in a String
https://www.youtube.com/watch?v=St47WCbQa9M

Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
'''

def finduniq(s):
    if len(s) == 0:
        return -1
    if len(s) == 1:
        return 0

    hashmap = {}
    for i in range(len(s)):
        if s[i] not in hashmap:
            hashmap[s[i]] = i

    for ch in hashmap:
        count = 0
        for i in range(len(s)):
            if s[i] == ch:
                count += 1
        if count == 1:
            return hashmap[ch]
    return -1






s = "leetcode"
s = 'ccddada'
s = ''
print(finduniq(s))