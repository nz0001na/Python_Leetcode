'''
4. Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

Approach 1: brute-force method
Approach 2:
'''


def getM(la):
    count = len(la)
    if count % 2 == 0:
        a = la[int(count / 2) - 1]
        b = la[int(count / 2)]
        return (a + b) / 2
    else:
        return la[int(count / 2)]

# brute-force method
def findMedian(nums1,nums2):
    la = nums1 + nums2
    la.sort()
    return getM(la)

def findMedian2(nums1, nums2):
    i,j=0,0
    nums3 = []
    while(i<len(nums1) and j <len(nums2)):
        if nums1[i] < nums2[j]:
            nums3.append(nums1[i])
            i = i + 1
        else:
            nums3.append(nums2[j])
            j = j + 1
    if i < len(nums1):
        nums3 = nums3 + nums1[i:len(nums1)]
    if j < len(nums2):
        nums3 = nums3 + nums2[j:len(nums2)]
    return getM(nums3)





nums1 = [1,2]
nums2 = [3,4]
print(findMedian2(nums1, nums2))