'''
283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of
it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.


'''

def remove(nums):
    is0 = 0
    not0 = 0
    while not0 < len(nums) and is0 < len(nums):
        while is0 < len(nums) and nums[is0]:
            is0 += 1
        while not0 < len(nums) and not nums[not0]:
            not0 += 1

        if not0 < len(nums) and is0 < len(nums):
            if is0 < not0:
                t = nums[not0]
                nums[not0] = nums[is0]
                nums[is0] = t
                is0 += 1
                not0 += 1
            else:
                not0 += 1

    return nums


def remove2(nums):
    is0, not0 = 0,0
    while not0 < len(nums):
        if nums[not0] == 0:
            not0 += 1
        else:
            t = nums[not0]
            nums[not0] = nums[is0]
            nums[is0] = t
            is0 += 1
            not0 += 1


    return nums



nums = [1]
remove2(nums)
print(nums)