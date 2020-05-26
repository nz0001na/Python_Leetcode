'''
118. Pascal's Triangle
Easy
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''

def generate(numRows):
    if numRows == 0:
        return None
    res_list = []
    if numRows == 1:
        res_list.append([1])
        return res_list

    if numRows == 2:
        res_list.append([1])
        res_list.append([1,1])
        return res_list

    res_list.append([1])
    res_list.append([1,1])
    for i in range(2,numRows):
        lis = []
        for j in range(i+1):
            if j == 0 or j == i:
                lis.append(1)
            else:
                a = res_list[i-1][j-1]
                b = res_list[i-1][j]
                lis.append(a+b)
        res_list.append(lis)

    return res_list




numRows = 5
print(generate(numRows))