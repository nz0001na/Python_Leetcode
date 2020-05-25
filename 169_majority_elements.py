'''
169. Majority Element
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2

'''

def majority(nums):
    if len(nums) == 1:
        return nums[0]
    n = len(nums)//2
    hashmap = {}
    for i in range(len(nums)):
        if nums[i] not in hashmap:
            hashmap[nums[i]] = i

    maxcount = 0
    maxele = nums[0]
    for ch in hashmap:
        count = 0
        for i in range(len(nums)):
            if nums[i] == ch:
                count += 1

        if count > maxcount:
            maxcount = count
            maxele = ch
    if maxcount > n:
        return maxele


# nums = [2, 2, 1, 1, 1, 2, 2]
nums = [3, 2, 3]
print(majority(nums))