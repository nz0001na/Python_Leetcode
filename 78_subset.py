'''
78. Subsets
Medium

https://www.cnblogs.com/grandyang/p/4309345.html


Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

#  add item to subet
def subset(nums):
    if nums is None:
        return None
    if len(nums) == 0:
        return [[]]
    res = [[]]
    from copy import deepcopy
    for i in range(len(nums)):
        tmp = deepcopy(res)
        for j in range(len(tmp)):
            tmp[j].append(nums[i])

        res += tmp
    print(res)
    return res


# # DFS
# from copy import deepcopy
# def DFS(nums, pos, out, res):
#     res.append(deepcopy(out))
#     for i in range(pos, len(nums)):
#         out.append(nums[pos])
#         DFS(nums, pos+1, out, res)
#         out.pop()
#
# def subset2(nums):
#     nums.sort()
#     res = []
#     out = []
#     pos = 0
#     DFS(nums, pos, out, res)
#     return res


# use binary number
def subset3(nums):
    if nums is None:
        return None
    if len(nums) == 0:
        return [[]]

    res = []
    max = 2**(len(nums))
    for i in range(max):
        j = 0
        out = []
        index = 0
        while j < len(nums):
            if i & 1 == 1:
                out.append(nums[index])
            index +=1
            i >>= 1
            j += 1
        res.append(deepcopy(out))
    return res


nums = [1,2,3]
print(subset2(nums))