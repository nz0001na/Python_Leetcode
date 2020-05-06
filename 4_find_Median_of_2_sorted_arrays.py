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
Approach 2: merge
Approach 3: bst O（log(min(m,n))）
  solution: array1, array2
            ensure: len(array1) < len(array2)

            while(start <= end):
                for array1:
                    set start=0, end = len(array1)
                    partirion1 = (start + end)/2
                for array2:
                    partition2 = (len(array1)+len(array2)+1 )/2 - partition1

                get four sub arrays: array1[0: partirion1-1]   and  array1[partition1, end]
                                     array2[0:partition2-1] and array2[partition2, end]
                        (left1max = array1[partition1-1]:   if partition1==0, left1max = -sys.maxsize-1
                         right1min = array1[partition1]:   if partition1==len(array1), left1max = sys.maxsize
                         left2max = array2[partition2-1]:  if partition2==0, left2max = -sys.maxsize-1
                         right2min = array2[partition2]：  if partition2==len(array2), right2min = sys.maxsize
                        )
                check:
                    if left1max <= right2min and right1min >= left2max:
                        if len(array1)+len(array2) is odd:
                            median = max(left1max, left2max)
                        if is even:
                            median = average(max(left1max, left2max),  min(right1min, right2min))
                    if left1max > right2min:
                        end = partition1 -1
                    if left2max > right1min:
                        start = partition1 + 1

'''

import sys

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

# merge
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



def Partition(start, end, fp, nums1, nums2):
    if start <= end:
        xp = int((start + end)/2)
        yp = int(fp - xp)
        if xp==0:
            leftxmax = -sys.maxsize - 1
        else:
            leftxmax = nums1[xp-1]
        if yp == 0:
            leftymax = -sys.maxsize - 1
        else:
            leftymax = nums2[yp-1]
        if xp == len(nums1):
            rightxmin = sys.maxsize
        else:
            rightxmin = nums1[xp]
        if yp == len(nums2):
            rightymin = sys.maxsize
        else:
            rightymin = nums2[yp]

        if leftxmax <= rightymin and rightxmin >= leftymax:
            if (len(nums1) + len(nums2)) % 2 == 0:
                median = (max(leftxmax, leftymax) + min(rightxmin, rightymin))/2
            else:
                median = max(leftxmax, leftymax)
            print(median)
        if leftxmax > rightymin:
            Partition(start, xp-1, fp, nums1, nums2)
        if rightxmin < leftymax:
            Partition(xp+1, end, fp, nums1, nums2)


# BST search
def findMedian3(nums1, nums2):
    fp = int((len(nums1) + len(nums2) + 1) / 2)
    if len(nums1) > len(nums2):
        Partition(0, len(nums2), fp, nums2, nums1)
    else:
        Partition(0, len(nums1), fp, nums1, nums2)



def findMedian4(nums1, nums2):
    fp = int((len(nums1) + len(nums2) + 1) / 2)
    if len(nums1) > len(nums2):
        T = nums1
        nums1 = nums2
        nums2 = T

    start = 0
    end = len(nums1)
    while(start <=end):
        xp = int((start + end)/2)
        yp = int(fp - xp)
        if xp==0:
            leftxmax = -sys.maxsize - 1
        else:
            leftxmax = nums1[xp-1]
        if yp == 0:
            leftymax = -sys.maxsize - 1
        else:
            leftymax = nums2[yp-1]
        if xp == len(nums1):
            rightxmin = sys.maxsize
        else:
            rightxmin = nums1[xp]
        if yp == len(nums2):
            rightymin = sys.maxsize
        else:
            rightymin = nums2[yp]

        if leftxmax <= rightymin and rightxmin >= leftymax:
            if (len(nums1) + len(nums2)) % 2 == 0:
                median = (max(leftxmax, leftymax) + min(rightxmin, rightymin))/2
            else:
                median = max(leftxmax, leftymax)
            print(median)
            break
        if leftxmax > rightymin:
            end = xp-1
        if rightxmin < leftymax:
            start = xp+1




nums1 = [1,2,5]
nums2 = [3,4]
findMedian4(nums1, nums2)