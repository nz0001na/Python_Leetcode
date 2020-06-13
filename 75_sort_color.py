'''
75. Sort Colors
Medium

Given an array with n objects colored red, white or blue, sort them in-place
so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total
number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

'''

def sortcolor(nums):
    r = 0
    w = 0
    b = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            r += 1
        if nums[i] == 1:
            w += 1
        if nums[i] == 2:
            b += 1
    for j in range(len(nums)):
        if j < r:
            nums[j] = 0
        elif j >= r+w:
            nums[j] = 2
        else:
            nums[j] = 1
    print(nums)


nums = [2,0,2,1,1,0,0,0]
print(sortcolor(nums))
# Output: [0,0,1,1,2,2]