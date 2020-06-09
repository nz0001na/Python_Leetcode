'''
215. Kth Largest Element in an Array
Medium

Find the kth largest element in an unsorted array. Note that it is the kth largest element
in the sorted order, not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''
# use reverse sort method in python, and return nums[k-1]
def kthlargest(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]


#     quick sort: reverse sort list, and return nums[k-1]
def Partition(nums, low, high):
    i = low - 1
    pivot = nums[high]
    for j in range(low, high, 1):
        if nums[j] >= pivot:
            i += 1
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
    p = i + 1
    tmp = nums[p]
    nums[p] = nums[high]
    nums[high] = tmp
    return p

def QuickSort(nums, low, high):
    if low < high:
        p = Partition(nums, low, high)
        QuickSort(nums, low, p-1)
        QuickSort(nums, p+1, high)


def kthlargest2(nums, k):
    low = 0
    high = len(nums)-1
    QuickSort(nums, low, high)
    print(nums)
    return nums[k-1]


# use Quick Sort, find partition p, if p== k-1, return
def PartitionFind(nums, low, high):
    print(str(low) + ' ' + str(high))
    i = low - 1
    pivot = nums[high]
    for j in range(low, high, 1):
        if nums[j] >= pivot:
            i += 1
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
    p = i+1
    tmp = nums[high]
    nums[high] = nums[p]
    nums[p] = tmp
    print(p)
    return p


def kthlargest3(nums, k):
    if len(nums) == 0:
        return None
    low = 0
    high = len(nums)-1
    while 1:
        p = PartitionFind(nums, low, high)
        if p == k-1:
            print(nums)
            return nums[p]
        elif p > k-1:
            high = p - 1
        else:
            low = p + 1



# nums = [3,2,3,1,2,4,5,5,6]
# nums = [3,2,1,5,6,4,3]
nums = [1]
k = 1
print(kthlargest3(nums, k))
