'''
Leetcode: Problems
1. twoSum:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


Approach 1: Brute Force
Approach 2: Two-pass hash table
Approach 3: One-pass hash table
'''


# Approach 1: Brute Force
def twoSum(nums, target):
    count = len(nums)
    for i in range(count):
        for j in range(i+1, count):
            summ = nums[i] + nums[j]
            if summ == target:
                print(i)
                print(j)
                return [i,j]


# two-pass hashtable
def twoSum1(nums, target):
    new_nums = {}
    for i in range(len(nums)):
        new_nums[nums[i]] = i
    for j in range(len(nums)):
        num1 = nums[j]
        num2 = target - num1
        i = new_nums.get(num2)
        if num2 in new_nums.keys() and i != j:
            return [j, i]

# one-pass hash table
def twoSum2(nums, target):
    new_nums = {}
    for i in range(len(nums)):
        num1 = nums[i]
        num2 = target - num1
        if num2 in new_nums.keys():
            j = new_nums.get(num2)
            return [i,j]
        else:
            new_nums[num1] = i


nums = [3, 3]
target = 6
print(twoSum2(nums, target))