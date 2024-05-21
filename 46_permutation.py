'''
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.
'''

'''
deep copy out, to append into res.


'''

from copy import deepcopy

def DFS(nums, level, out, res, visited):
    # base
    if level == len(nums):
        o = deepcopy(out)
        res.append(o)
        return
    # recursion
    for i in range(len(nums)):
        if visited[i] == 1:
            continue
        visited[i] = 1
        out.append(nums[i])
        DFS(nums, level + 1, out, res, visited)
        out.pop()
        visited[i] = 0

nums = [1,2,3]
res = []
out = []
visited = [0 for i in range(len(nums))]
level = 0
DFS(nums, level, out, res, visited)

print(res)


