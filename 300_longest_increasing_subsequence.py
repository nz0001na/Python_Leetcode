'''
Given an integer array nums, return the length of the longest strictly increasing
subsequence


'''

'''
create a array: trg, to store elements, maintain the current length that have found.
O(n^2)
O(n)
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


'''

'''