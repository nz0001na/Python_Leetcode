'''
347. Top K Frequent Elements
Medium

https://www.geeksforgeeks.org/max-heap-in-python/
https://www.geeksforgeeks.org/min-heap-in-python/


Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.

'''

# use sort method of list in python
def topk(nums, k):
    hashset = {}
    for i in range(len(nums)):
        if nums[i] not in hashset:
            hashset[nums[i]] = 1
        else:
            c = hashset[nums[i]]
            hashset[nums[i]] = c + 1

    key = [[None for i in range(2)] for j in range(len(hashset))]
    i = 0
    for ch in hashset:
        key[i][0] = ch
        key[i][1] = hashset[ch]
        i += 1
    key.sort(key=lambda x:x[1], reverse=True)

    res = []
    for j in range(k):
        res.append(key[j][0])
    print(res)


# use heap in python
from heapq import heapify, heappop, heappush
def topk2(nums, k):
    hashset = {}
    for i in range(len(nums)):
        if nums[i] not in hashset:
            hashset[nums[i]] = 1
        else:
            hashset[nums[i]] += 1

    heap = []
    heapify(heap)

    for ch in hashset:
        heappush(heap, [(-1)*hashset[ch], ch])

    res = []
    for i in range(k):
        res.append(heappop(heap)[1])
    print(heap)
    return res







nums = [4, 5, 1, 5, 4, 4, 1, 2, 2 ,3, 5,5]
nums = [1,1,1,2,2,3]
k = 2
print(topk2(nums, k))