'''
350. Intersection of Two Arrays II
Easy
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''

def intersection(nums1, nums2):
    if len(nums1) == 0:
        return nums1
    if len(nums2) == 0:
        return nums2

    hashmap1 = {}
    for i in range(len(nums1)):
        if nums1[i] not in hashmap1:
            hashmap1[nums1[i]] = 1
        else:
            count = hashmap1[nums1[i]]
            hashmap1[nums1[i]] = count + 1

    hashmap2 = {}
    for j in range(len(nums2)):
        if nums2[j] not in hashmap2:
            hashmap2[nums2[j]] = 1
        else:
            count = hashmap2[nums2[j]]
            hashmap2[nums2[j]] = count + 1

    if len(hashmap1) < len(hashmap2):
        A = hashmap1
        B = hashmap2
    else:
        A = hashmap2
        B = hashmap1

    final_list = []
    for a in A:
        if a in B:
            num = min(A[a], B[a])
            while num:
                final_list.append(a)
                num -= 1
    return final_list




nums1 = []
nums2 = [0]
print(intersection(nums1, nums2))
