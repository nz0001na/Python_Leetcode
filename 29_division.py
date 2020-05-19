'''
29. Divide Two Integers
https://www.youtube.com/watch?v=htX69j1jf5U

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero, which means losing its fractional part.
For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.


'''
import sys


# subtraction - big O is too big!!!
def division(dividend, divisor):
    if divisor == 0:
        return None
    if dividend >= 0 and divisor > 0 or dividend < 0 and divisor < 0:
        same = 1
    else:
        same = 0
    dividend = abs(dividend)
    divisor = abs(divisor)
    count = 0
    while dividend >= divisor:
        count += 1
        dividend -= divisor
    if same == 1:
        return count
    else:
        return -count



def division2(dividend, divisor):
    if dividend == -2**31 and divisor == -1:
        return 2**31-1
    # if divisor == 0:
    #     return sys.maxsize
    if dividend > 0 and divisor > 0 or dividend <0 and divisor<0:
        sign = 1
    else:
        sign = -1
    if dividend == 0:
        return 0

    dividend = abs(dividend)
    divisor = abs(divisor)

    res = 0
    while dividend >= divisor:

        p = divisor
        count = 1
        while dividend >= p<<1:
            p <<= 1
            count <<=1
        res += count
        dividend -= p

    if sign == 1:
        return res
    elif sign == -1:
        return -res
    return res


# print(2**63-1)
dividend = 10
divisor = 3
print(division2(dividend, divisor))