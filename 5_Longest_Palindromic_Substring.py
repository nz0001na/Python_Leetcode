'''
1
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(s):
            i = 0
            j = len(s) - 1
            while (i < j):
                if s[i] != s[j]:
                    return False
                else:
                    i += 1
                    j -= 1
            return True

        ml = 0
        result = None
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if check(s[i:j]):
                    if j - i > ml:
                        ml = j - i
                        result = s[i:j]
        return result


'''
DP
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for k in range(1, n + 1):
            for i in range(0, n - k + 1):
                if s[i] == s[i + k - 1] and (k <= 2 or dp[i + 1][i + k - 2] == 1):
                    dp[i][i + k - 1] = 1
                    result = s[i:i + k]
        return result



'''

'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(s):
            i = 0
            j = len(s) - 1
            while (i < j):
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        result = ''
        w = 0
        for i in range(len(s)):
            if i == 0:
                w = 1
                result = s[0]
            elif i >= w + 1 and check(s[i - w - 1:i + 1]):
                result = s[i - w - 1:i + 1]
                w += 2
            elif i >= w and check(s[i - w:i + 1]):
                result = s[i - w: i + 1]
                w += 1
        return result





