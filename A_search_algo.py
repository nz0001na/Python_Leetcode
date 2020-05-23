'''
This provides several search algorithms used for searching target value in a sorted array, and return index:

1. Binary Search:  https://www.youtube.com/watch?v=zeULw-a7Mw8
2.
'''

# 1. Binary Search: recursive
def binary_search(nums, left, right, target):
    if left > right:
        return -1
    mid = (left + right) // 2
    val = nums[mid]
    if val == target:
        return mid
    elif val < target:
        return binary_search(nums, mid+1, right, target)
    else:
        return binary_search(nums, left, mid-1, target)


def binary_search_recursion(nums, target):
    return binary_search(nums, 0, len(nums)-1, target)


# 1. Binary Search: Iterative
def binary_search_iterative(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        val = nums[mid]
        if val == target:
            return mid
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1




nums = [2, 5, 7, 8, 12, 19, 30, 45, 59, 65]
target = 19
print(binary_search_recursion(nums, target))
print(binary_search_iterative(nums, target))