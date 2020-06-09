'''
49. Group Anagrams
Medium

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]


Note:
All inputs will be in lowercase.
The order of your output does not matter.

'''
# sort each str to compare
# use dictionary to store each group
def anagram(strs):
    cnt = len(strs)
    res = []
    hashset = {}
    for i in range(cnt):
        ns = ''.join(sorted(strs[i]))
        if ns not in hashset:
            hashset[ns] = []
        hashset[ns].append(strs[i])

    for ch in hashset:
        res.append(hashset[ch])
    return res


def anagram2(strs):
    cnt = len(strs)
    if cnt == 0:
        return None
    hashset = {}
    for i in range(cnt):
        s = strs[i]
        na = [0]*26
        for j in range(len(s)):
            asc = ord(s[j])
            na[asc-97] += 1
        ns = ''.join(str(e) for e in na)

        if ns not in hashset:
            hashset[ns] = []
        hashset[ns].append(strs[i])

    res = []
    for c in hashset:
        res.append(hashset[c])
    return res


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(anagram2(strs))

