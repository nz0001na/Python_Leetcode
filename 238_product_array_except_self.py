'''
238. Product of Array Except Self
Medium

Given an array nums of n integers where n > 1,  return an array output such that
output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or suffix
of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''


def product(nums):
    count = len(nums)
    if count < 2:
        return None

    res = [None]*count
    preproduct = [None] * count
    preproduct[0] = nums[0]
    postproduct = [None] * count
    postproduct[count-1] = nums[count-1]

    for i in range(1,count):
        preproduct[i] = preproduct[i-1] * nums[i]

    res[count-1] = preproduct[count-2]
    for j in range(count-2, -1, -1):
        postproduct[j] = postproduct[j+1] * nums[j]
        if j == 0:
            res[j] = postproduct[j+1]
        else:
            res[j] = preproduct[j-1] * postproduct[j+1]

    return res


#  constant space
def product2(nums):
    cnt = len(nums)
    if cnt < 2:
        return None

    res = [0]*cnt
    res[0] = 1
    for i in range(1,cnt):
        res[i] = res[i-1]* nums[i-1]

    right = nums[cnt-1]
    for j in range(cnt-2,-1,-1):
        res[j] = res[j]* right
        right *= nums[j]
    return res



nums = [1,2,3,4]
print(product2(nums))