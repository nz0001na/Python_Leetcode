'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.


Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

    1 <= nums.length <= 8
    -10 <= nums[i] <= 10


'''


'''
sort nums first.
DFS
deep copy out, to append into res.

'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def DFS(nums, level, out, res, visited):
            if level == len(nums):
                o = deepcopy(out)
                res.append(o)
                return
            for i in range(len(nums)):
                if visited[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == 1:
                    continue
                visited[i] = 1
                out.append(nums[i])
                DFS(nums, level + 1, out, res, visited)
                out.pop()
                visited[i] = 0

        res = []
        out = []
        nums.sort()
        visited = [0 for i in range(len(nums))]
        level = 0
        DFS(nums, level, out, res, visited)
        return res


