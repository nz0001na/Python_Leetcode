'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]


Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.

'''


'''
DFS:

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


