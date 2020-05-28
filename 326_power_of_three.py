'''
326. Power of Three
Easy
https://github.com/grandyang/leetcode/issues/326

Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Example 4:
Input: 45
Output: false

Follow up:
Could you do it without using any loop / recursion?

'''

# brute-force
def isPower3(n):
    if n == 0:
        return False
    if n == 1:
        return True

    pow = 0
    re = 3**pow
    while re < n:
        re = 3 ** pow
        pow += 1

    return re == n

# max:3**19
def isPower3_2(n):
    if n>0 and 1162261467%n == 0:
        return True
    return False




import math
def isPower3_3(n):
    a = round(math.log(n,10)/math.log(3,10))
    b = math.log(n,10)/math.log(3,10)
    return n > 0 and a - b==0

n = 27
print(isPower3_3(n))