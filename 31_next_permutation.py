'''
31. Next Permutation
Medium
https://github.com/grandyang/leetcode/issues/31

Implement next permutation, which rearranges numbers into the lexicographically next
greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible
order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding
outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

def nextPermutation(nums):
    i = len(nums)-2
    j = len(nums)-1
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1

    if i >= 0:
        while nums[j] <= nums[i]:
            j -= 1
        t = nums[j]
        nums[j] = nums[i]
        nums[i] = t
    left = i+1
    right = len(nums)-1
    while left <= right:
        p = nums[left]
        nums[left] = nums[right]
        nums[right] = p
        left += 1
        right -= 1
    print(nums)



nums = [3, 2, 1]
# nums = [1, 2, 7, 4, 3, 1]
# 1　　3　　1　　2　　4　　7
print(nextPermutation(nums))