'''
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

def maxSubarray(nums):
    lens = len(nums)
    maxv = nums[0]
    dp = [None for i in range(lens)]
    for i in range(0,lens):
        if i == 0:
            dp[i] = nums[i]
        else:
            a = nums[i]
            b = nums[i] + dp[i-1]
            dp[i] = max(a, b)

        if dp[i] > maxv:
            maxv = dp[i]

    return maxv





nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubarray(nums))