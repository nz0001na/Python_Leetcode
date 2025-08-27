def lcs_native(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 0

    if s1[-1] == s2[-1]:
        return 1 + lcs_native(s1[:-1], s2[:-1])
    else:
        return max(lcs_native(s1[:-1], s2), lcs_native(s1, s2[:-1]))


def lcs_memoization(s1, s2, tab):
    if len(s1) == 0 or len(s2) == 0: return 0
    if tab[len(s1)][len(s2)] != -1: return tab[len(s1)][len(s2)]

    if s1[-1] == s2[-1]:
        tab[len(s1)][len(s2)] = 1 + lcs_memoization(s1[:-1], s2[:-1], tab)
    else:
        tab[len(s1)][len(s2)] = max(lcs_memoization(s1[:-1],s2,tab), lcs_memoization(s1, s2[:-1], tab))
    return tab[len(s1)][len(s2)]



def lcs_tabulation(s1, s2):
    dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]

    for i in range(1,len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[len(s1)][len(s2)]


def lcs_tabulation_space(s1, s2):
    prev = [0 for _ in range(len(s2)+1)]
    curr = [0 for _ in range(len(s2)+1)]

    for i in range(1, len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                curr[j] = 1 + prev[j-1]
            else:
                curr[j] = max(curr[j-1], prev[j])
        prev = curr
        curr = [0 for _ in range(len(s2) + 1)]
    return prev[len(s2)]


def lcs_tabulation_space2(s1, s2):
    curr = [0 for _ in range(len(s2)+1)]
    for i in range(1,len(s1)+1):
        prev = curr[0]
        for j in range(1,len(s2)+1):
            temp = curr[j]
            if s1[i-1] == s2[j-1]:
                curr[j] = 1 + prev
            else:
                curr[j] = max(curr[j-1], curr[j])
            prev = temp
    return curr[len(s2)]





s1 = "AGGTAB"
s2 = "GXTXAYB"
rows = len(s1) + 1
cols = len(s2) + 1
tab = [[-1 for _ in range(cols)] for _ in range(rows) ]
# print(lcs_native(s1, s2))
print(lcs_memoization(s1, s2, tab))
print(lcs_tabulation(s1, s2))
print(lcs_tabulation_space(s1,s2))
print(lcs_tabulation_space2(s1,s2))



