'''

74: medium    vs. 240

You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.



Example 1:
Input: matrix = [[1,3,5,7],
                 [10,11,16,20],
                 [23,30,34,60]],
       target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],
                [10,11,16,20],
                [23,30,34,60]],
      target = 13
Output: false



Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104


'''



'''
Solution 1:  two Binary search  
       1st: between 0 and m, to find the right row.
       2nd: between 0 and n, to find the right column of found row.      

'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m
        while (left < right):
            mid = int((left + right) / 2)
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid

        row = left
        if row > 0:
            row -= 1
        left = 0
        right = n
        while (left < right):
            mid = int((left + right) / 2)
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid
        return False




'''
Solution:  Binary search  between 0 and m*n
treat 2d array as a 1d array.
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n
        while (left < right):
            mid = (left + right) / 2
            i = int(mid / n)
            j = int(mid % n)
            if matrix[i][j] == target:
                return True
            if matrix[i][j] >= target:
                right = mid
            else:
                left = mid + 1
        return False





