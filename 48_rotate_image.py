'''
48. Rotate Image
Medium
https://github.com/grandyang/leetcode/issues/48

You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''

# use extra matrix
def rotate(matrix):
    print(matrix)
    row = len(matrix)
    if row == 0:
        return
    res = [[None for i in range(row)] for j in range(row)]
    for i in range(row):
        for j in range(row):
            res[j][row-1-i] = matrix[i][j]

    print(res)


# # swap
# # (i,j) --> (j, i)  --> (j, n-1-i)
# # 1. swap [i,j] and [j, i]
# # 2. swap [i, j] and [i, n-1-j]
def rotate2(matrix):
    print(matrix)
    n = len(matrix)
    if n == 0 or n == 1:
        return
    for i in range(0, n):
        for j in range(i+1, n):
            t = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = t
    print(matrix)

    for i in range(0, n):
        for j in range(0, n//2):
            t = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = t

    print(matrix)



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]
rotate2(matrix)