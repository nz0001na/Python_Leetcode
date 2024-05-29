'''
179. Medium

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.



Example 1:

Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"


Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 109

'''

'''
*************************************************************
Solution:





'''

nums = [10, 4, 5]
res = ''
s = [str(c) for c in nums]
d = s.sort(reverse=True)
print(d)
for c in s:
    res += c

print(res)


str1 = '30'
str2 = '3'

if str1 > str2:
    print("str1 is bigger than str2")
elif str1 < str2:
    print("str2 is bigger than str1")
else:
    print("str1 and str2 are equal")