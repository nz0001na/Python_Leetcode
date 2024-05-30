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
Solution: Bubble sort
    for string, if a+b > b+a, a>b

    (1) outer loop: for 0 to len(nums)-1
    (2) inner loop: for 0 to len(nums)-1-i (for each loop, the last element is set in place)
        compare two adjacent elements,
        put smaller one at the location after the bigger one.
    
'''

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = [str(c) for c in nums]
        for i in range(len(s)-1):
            # last element is alreay in place
            for j in range(0, len(s)-1-i):
                if s[j]+s[j+1] < s[j+1]+s[j]:
                    tmp = s[j+1]
                    s[j+1] = s[j]
                    s[j] = tmp
        res = ''
        for c in s:
            res += c

        if res[0] == '0':
            return '0'
        return res
