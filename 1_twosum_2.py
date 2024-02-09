'''
brute force
'''
def twoSum_1(nums, target):
    if len(nums) == 0:
        return None
    if len(nums) == 1 and nums[0] != target:
        return None

    index_list = []
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                index_list.append(i)
                index_list.append(j)
    return index_list


'''
use dictionary with two-pass
'''
def twoSum_2(nums, target):
    count = len(nums)
    result = []

    dict_nums = {}
    for i in range(count):
        dict_nums[nums[i]] = i
    for j in range(count):
        ele = nums[j]
        rest = target - ele
        if rest in dict_nums.keys() and j != dict_nums[rest]:
            result = [j, dict_nums[rest]]
            break
    return result

'''
use disctionary with one-pass
'''
def twoSum_3(nums, target):
    count = len(nums)
    dict_nums = {}
    result = []
    for i in range(count):
        num1 = nums[i]
        num2 = target - num1
        if num2 in dict_nums.keys():
            result = [i, dict_nums[num2]]
        else:
            dict_nums[nums[i]] = i
    return result




nums= [3,2,4]
target=6
print(twoSum_1(nums, target))
print(twoSum_2(nums, target))
print(twoSum_3(nums, target))


