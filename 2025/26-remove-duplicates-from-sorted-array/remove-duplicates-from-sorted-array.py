class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 0: return None
        slow = 0
        for i in range(n):
            if nums[slow] != nums[i]:
                slow += 1
                nums[slow] = nums[i]

        return slow+1




