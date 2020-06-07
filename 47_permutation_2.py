'''
47. Permutations II
Medium
https://www.youtube.com/watch?v=snAviXjcfpY

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

'''

def permutation(nums):
    if len(nums) == 0:
        return
    if len(nums) == 1:
        return [nums]
    # sort first
    nums.sort()
    res = []
    out = []
    level = 0
    visit = [False for i in range(len(nums))]
    # DFS then
    DFS(nums, level, res, out, visit)
    return res

from copy import deepcopy
def DFS(nums, level, res, out, visit):
    if level == len(nums):
        p = deepcopy(out)
        res.append(p)
        return

    for i in range(len(nums)):
        if visit[i] == True:
            continue
        if i > 0 and visit[i-1] == False and nums[i] == nums[i-1]:
            continue
        visit[i] = True
        out.append(nums[i])
        DFS(nums, level+1, res, out, visit)
        out.pop()
        visit[i] = False




nums = [1]
print(permutation(nums))