'''
Question:  (medium)
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.

'''


'''
Solution 1: 
brute-force

Use two loops:
 outer loop i: begin index of substring, [0,len(s)-1]
   inner loop j: end index of substring, [i+1, len(s)]
      loop body: check s[i,j] if it is a palindromic string
                 if yes, check size of it, and update maxLen and result.

how to check if it is a palindromic string?
    use while loop with condition (i<j): i is left point, j is right point.

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
create a 2-d array, initialized with 0, the values in it means: dp[i][j], if the substring s[i:j] is palindromic.

theory: 
    for string s : E_i E_(i+1) ..... E_{i+k-2} E_{i+k-1}
    if substring E_(i+1) ..... E_{i+k-2} is palindromic and E_i == E_{i+k-1},
    s is palindromic too.

here, k: the length of substring
      i: beginning index

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





