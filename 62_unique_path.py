'''
62. Unique Paths
Medium

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach
the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28

Constraints:
1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

'''

# 2d array DP
def uniquepath(m,n):
    if m <0 or n < 0:
        return None
    dp = [[0]*n]*m
    for i in range(m):
        for j in range(n):
            if i == 0 or j==0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return dp[m-1][n-1]

# 1d array DP
def uniquepath2(m,n):
    dp = [0]*n
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[j] = 1
            else:
                dp[j] = dp[j] + dp[j-1]
    return dp[n-1]

# Combination C(m+n-2, min(m-1,n-1))
def uniquepath3(m, n):
    if m <= 0 or n <= 0:
        return None
    num = 1
    denom = 1
    b = min(m-1, n-1)
    for i in range(b):
        denom *= i+1
        num *= m + n -2 - i
    return num // denom


m = 4
n = 4
print(uniquepath3(m,n))