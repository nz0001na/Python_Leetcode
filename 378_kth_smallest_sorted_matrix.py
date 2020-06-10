'''
378. Kth Smallest Element in a Sorted Matrix
Medium

Given a n x n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
return 13.

Note:
You may assume k is always valid, 1 ≤ k ≤ n**2.

'''

# brute-force method: O(n**2)
def kthsmall(marix, k):
    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            res.append(matrix[i][j])

    res.sort()
    return res[k-1]

# quick sort
def Partition(res, low, high):
    i = low - 1
    pivot = res[high]
    for j in range(low, high, 1):
        if res[j] <= pivot:
            i += 1
            tmp = res[j]
            res[j] = res[i]
            res[i] = tmp

    p = i+1
    tmp = res[high]
    res[high] = res[p]
    res[p] = tmp
    return p

def kthsmall2(matrix, k):
    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            res.append(matrix[i][j])

    low = 0
    high = len(res)-1
    while 1:
        p = Partition(res, low, high)
        if p == k-1:
            return res[p]
        elif p > k-1:
            high = p - 1
        else:
            low = p + 1

# min heap, get the kth pop value
def kthsmall3(matrix, k):
    if len(matrix) <=0:
        return None
    from heapq import heapify, heappush, heappop
    heap = []
    heapify(heap)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            heappush(heap, matrix[i][j])

    for i in range(k):
        t = heappop(heap)
    return t


# use max heap, return kth pop??????
def kthsmall4(matrix, k):
    cnt = len(matrix)
    if cnt <= 0:
        return None
    from heapq import heapify, heappush, heappop
    heap = []
    heapify(heap)
    for i in range(cnt):
        for j in range(cnt):
            heappush(heap, -matrix[i][j])
            if len(heap) > k:
                return -heappop(heap)



matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
print(kthsmall3(matrix, k))



