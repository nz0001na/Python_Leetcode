'''
287. Find the Duplicate Number
Medium
https://www.cnblogs.com/grandyang/p/4843654.html

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist. Assume that there is only one duplicate number,
find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n**2).
There is only one duplicate number in the array, but it could be repeated more than once.

'''
# brute-force method
def duplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return nums[i]

# binary search between [1,n]
# search count of that <= mid
def duplicate2(nums):
    low = 1
    high = len(nums)-1
    while low < high:
        mid = (low + high)//2
        count = 0
        for i in range(len(nums)):
            if nums[i] <= mid:
                count += 1
        if count > mid:
            high = mid
        else:
            low = mid + 1
    return high
    # return low   #  ---both are OK


# slow and fast pointers
def duplicate3(nums):
    slow = 0
    fast = 0
    t = 0
    while 1:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    while 1:
        slow = nums[slow]
        t = nums[t]
        if slow == t:
            break
    return slow



nums = [1,3,4,2,2,2,6]
print(duplicate3(nums))