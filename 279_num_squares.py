'''
279. Perfect Squares
Medium
Given a positive integer n, find the least number of perfect square numbers
(for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

import math

def numSquares(n):
    if n <= 0:
        return False
    while n%4==0:
        n = n/4

    if n%8==7: return 4
    i=0
    while i*i<=n:
        a = i*i
        b = int(math.sqrt(n-a))
        if a+b*b == n:
            if b*a!=0:
                return 2
            else:
                return 1
            # return ~~a + ~~b

        i = i + 1
    return 3

n = 13
print(numSquares(n))