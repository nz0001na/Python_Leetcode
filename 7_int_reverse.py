'''
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''


def reverse(x):
    neg = 0
    if x <0:
        neg = 1
        x = -x
    digs = len(str(x))
    rever = 0
    for i in range(digs):
        d = x // (10**(digs-i-1))
        x = x % (10**(digs-i-1))
        rever += d * (10**i)
        print(rever)

    if neg == 1:
        rever = (-1)*rever
        if rever < (-1)*2**(31):
            rever = 0
    else:
        if rever > 2**(31)-1:
            rever = 0
    return rever

x = -321
print(reverse(x))