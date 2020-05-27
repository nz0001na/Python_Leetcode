'''
242. Valid Anagram
https://www.youtube.com/watch?v=IRN1VcA8CGc

Easy
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

Method 1: dictionary
Method 2: couter array
'''

# dictionary
def vanagram(s, t):
    hash1 = {}
    for i in range(len(s)):
        if s[i] not in hash1:
            hash1[s[i]] = 1
        else:
            count = hash1[s[i]]
            hash1[s[i]] = count + 1

    hash2 = {}
    for j in range(len(t)):
        if t[j] not in hash2:
            hash2[t[j]] = 1
        else:
            count = hash2[t[j]]
            hash2[t[j]] = count + 1

    if len(hash1.keys()) != len(hash2.keys()):
        return False
    for ch in hash1:
        if ch not in hash2 or hash2[ch] != hash1[ch]:
            return False

    return True

#
def vanagram2(s,t):
    if len(s) != len(t):
        return False
    hashmap = {}
    for i in range(len(s)):
        if s[i] not in hashmap:
            hashmap[s[i]] = 1
        else:
            hashmap[s[i]] += 1

        if t[i] not in hashmap:
            hashmap[t[i]] = -1
        else:
            hashmap[t[i]] -= 1

    for ch in hashmap:
        if hashmap[ch] != 0:
            return False
    return True






# counter array
def vanagram3(s, t):
    if len(s) != len(t):
        return False
    counter = [0 for i in range(26)]
    for i in range(len(s)):
        counter[ord(s[i])-ord('a')] += 1
        counter[ord(t[i])-ord('a')] -= 1

    for c in counter:
        if c != 0:
            return False
    return True




s = "anagram"
t = "nagaram"
print(vanagram2(s,t))