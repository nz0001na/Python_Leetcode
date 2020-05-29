'''
172. Factorial Trailing Zeroes
Easy
https://www.youtube.com/watch?v=wdz_KouqHx4

Given an integer n, return the number of trailing zeroes in n!.

Example 1:
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Note: Your solution should be in logarithmic time complexity.

'''


# time: O(n)
def factorial0(n):
    if n == 1:
        return 1
    faclist=[]
    faclist.append(1)
    for i in range(1,n):
        faclist.append(faclist[i-1]*(i+1))

    count = 0
    num = faclist[len(faclist)-1]
    while num%10 == 0:
        count += 1
        num /= 10
    return count


# time: O(logn)
def factorial0_2(n):

    res = 0
    while n:
        res += n//5
        n //= 5
    return res


n = 92
print(factorial0_2(n))