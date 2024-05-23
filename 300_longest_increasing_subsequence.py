'''
Given an integer array nums, return the length of the longest strictly increasing
subsequence


Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
    1 <= nums.length <= 2500
    -104 <= nums[i] <= 104

'''


'''
create a array: trg, to store elements, maintain the current length that have found.


space: O(n^2)
time: O(n)
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return

        trg = []
        for i in range(len(nums)):
            cur = nums[i]
            if i == 0:
                trg.append(cur)
                continue
            if cur <= trg[0]:
                trg[0] = cur
            elif cur > trg[len(trg) - 1]:
                trg.append(cur)
            else:
                # find and search : O(n)
                for j in range(len(trg) + 1):
                    if cur > trg[j] and cur <= trg[j + 1]:
                        trg[j + 1] = cur
                        break
        return len(trg)
