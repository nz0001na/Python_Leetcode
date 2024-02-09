'''
string comparison
'''

def LongestCommonPre(strs):
    if len(strs) == 0:
        return ''
    ele1 = strs[0]
    re = ''
    for i in range(len(ele1)):
        for j in range(1, len(strs)):
            if strs[j][i] != ele1[i]:
                return re
        re = re + ele1[i]
    return re

strs = ["flower","flow","flight"]
print(LongestCommonPre(strs))