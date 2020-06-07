'''
46. Permutations
Medium

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

def permutation(nums):
    if len(nums) <= 0:
        return
    res = []
    level = 0
    out = []
    visited = [False for i in range(len(nums))]
    permuteDFS(nums, level, visited, res, out)
    return res

# https://docs.python.org/3/library/copy.html
# shallow copy: just copy values, do not copy objects, they create bindings between a target and an object.
# deep copy:
# A shallow copy constructs a new compound object and then (to the extent possible)
# inserts references into it to the objects found in the original.
# # A deep copy constructs a new compound object and then, recursively, inserts
# copies into it of the objects found in the original.
from copy import deepcopy
def permuteDFS(nums, level, visited, res, out):
    if level == len(nums):
        p = deepcopy(out)
        res.append(p)
        return
    for i in range(len(nums)):
        if visited[i]== True:
            continue
        visited[i] = True
        out.append(nums[i])
        permuteDFS(nums, level+1, visited, res, out)
        out.pop()
        visited[i] = False



nums = [1,2,3,4]
print(permutation(nums))
