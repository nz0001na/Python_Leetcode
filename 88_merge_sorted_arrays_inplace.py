'''
88. Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]

'''


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        count = m+n
        d1 = m-1
        d2 = n-1
        i = m+n-1
        while d1 >= 0 and d2 >= 0:
            if nums1[d1] >= nums2[d2]:
                nums1[i] = nums1[d1]
                d1 -= 1
            else:
                nums1[i] = nums2[d2]
                d2 -= 1
            i -= 1
        if d1 <0:
            while d2 >=0:
                nums1[i] = nums2[d2]
                i -= 1
                d2 -= 1

        print(nums1)

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
C= Solution()
C.merge(nums1, 3, nums2, 3)
