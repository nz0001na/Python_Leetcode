'''
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
'''


def longprefix(strs):
    count = len(strs)
    if count == 0:
        return ''
    fst = strs[0]
    lp = ''
    for j in range(0, len(fst)+1):
        going = True
        prefix = fst[0:j]
        for i in range(0, count):
            if len(strs[i]) == 0:
                return ''
            if j > len(strs[i]) or not strs[i].startswith(prefix):
                going = False
                break
        if going and len(prefix) > len(lp):
            lp = prefix
    return lp


def longprefix2(strs):
    if len(strs) == 0:
        return ''
    minstr = strs[0]
    for i in range(len(strs)):
        if len(minstr) > len(strs[i]):
            minstr = strs[i]

    lenn = len(minstr)
    lp = ''
    for j in range(lenn+1):
        going = True
        prefix = minstr[0:j]
        for i in range(len(strs)):
            if len(strs[i]) == 0:
                return ''
            if j > len(strs[i]) or not strs[i].startswith(prefix):
                going = False
                break

        if going and len(lp) < len(prefix):
            lp = prefix
    return lp



# strs =["flower", "flow", "flight"]
# strs = ['c','c']
strs = ['ss']

print(longprefix2(strs))