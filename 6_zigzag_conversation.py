'''
6. ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

Approach 1: O(n)

'''

import math

def convert(s, numRows):
    count = len(s)
    if count == 0:
        return ""
    if numRows == 1:
        return s
    numCols = numRows - 1
    numZig = math.ceil(count/(2*numRows-2))
    allCols = numZig * numCols
    new_array = ['']*numRows*numCols*numZig
    for k in range(count):
        ch = s[k]
        index = k
        y = index//(2*numRows-2)
        z = index%(2*numRows-2)
        if z < numRows:
            i = z
            j = y*numCols
            # print('c')
        else:
            i = numRows - (z - numRows + 1) - 1
            j = y*numCols + (z - numRows) + 1
            # print('d')

        new_array[i* allCols + j] = ch
        # print('d')

    # for j in range(numRows):
    #     print(''.join(new_array[j*allCols:(j+1)*allCols]))
    final_s = ''
    for p in new_array:
        final_s += p
    return final_s.replace(' ', '')


s = 'A'
numRows = 1
print(convert(s, numRows))
# print('d')