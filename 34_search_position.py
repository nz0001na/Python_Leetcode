'''
34. Find First and Last Position of Element in Sorted Array
https://www.youtube.com/watch?v=dVXy6hmE_0U

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]


'''


#  iterative binary search
def findposition(nums, target):
    left = 0
    right = len(nums) - 1
    # find first position
    first_pos = -1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            first_pos = mid
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    # find last position
    last_pos = -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            last_pos = mid
            left = mid + 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    ls = [first_pos, last_pos]
    return ls




nums = [5,7,7,8,8,10]
target = 89

print(findposition(nums, target))