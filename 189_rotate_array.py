'''
189. Rotate Array
Easy
https://github.com/grandyang/leetcode/issues/189

Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:
1 <= nums.length <= 2 * 10^4
It's guaranteed that nums[i] fits in a 32 bit-signed integer.
k >= 0

'''

# use extra array
def rotatearray(nums, k):
    if k >= len(nums):
        k %= len(nums)

    right = []
    for i in range(len(nums)-k, len(nums)):
        right.append(nums[i])

    for j in range(len(nums)-k-1, -1, -1):
        nums[j+k] = nums[j]

    for p in range(k):
        nums[p] = right[p]

    print(nums)



# swap array
def swap(left, right, nums):
    while left < right:
        t = nums[left]
        nums[left] = nums[right]
        nums[right] = t
        left+= 1
        right -= 1

def rotatearray2(nums,k):
    if k >= len(nums):
        k %= len(nums)

    swap(0, len(nums)-k-1, nums)
    swap(len(nums)-k, len(nums)-1, nums)
    swap(0, len(nums)-1, nums)
    print(nums)



def rotatearray(nums, k):
    if k >= len(nums):
        k %= len(nums)
    



nums = [1,2,3,4,5,6,7]
k = 3
print(rotatearray2(nums, k))