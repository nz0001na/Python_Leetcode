class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n <=0:
            return None

        if nums[0] > target: return 0
        if nums[n-1] < target: return n

        left = 0
        right = n-1
        
        while(left <= right):
            middle = left + (right - left)//2
            if nums[middle] == target: return middle
            if target < nums[middle]:
                right = middle - 1
            if target > nums[middle]:
                left = middle + 1

        return right + 1

    
    