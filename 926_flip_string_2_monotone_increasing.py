'''
926. (medium)

A binary string is monotone increasing if it consists of some number of 0's (possibly none),
followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
Return the minimum number of flips to make s monotone increasing.


Example 1:
Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.

Example 2:
Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.

Example 3:
Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.



Constraints:

    1 <= s.length <= 105
    s[i] is either '0' or '1'.

'''


'''
Solution 1:
    use for loop [0,1,....des_i, ... len(s)-1],  des_i as target index of dividing 0 and 1 strings.
    [0,1,....des_i-1]:    0 string
    [des_i, .... len(s)-1]:    1 string
    
    at des_i, count:
        flip0:  #flip 1->0 in [0,1,....des_i-1]
        flip1:  #flip 0->1 in [des_i, .... len(s)-1]
    add flip0 and flip1, and compare with the value of minflip.
    minflip stores the current minimum flips.
    

O(n*n)

'''
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        num = len(s)
        if num <= 0:
            return None

        flip0 = 0
        flip1 = 0
        minflip = 1000000
        allflip = 0
        for des_i in range(num + 1):
            if des_i == 0:
                flip0 = 0
                flip1 = s.count('0')
            elif des_i == num:
                flip0 = s.count('1')
                flip1 = 0
            else:
                flip0 = s[0:des_i].count('1')
                flip1 = s[des_i:num].count('0')

            allflip = flip0 + flip1
            if allflip < minflip:
                minflip = allflip

        return minflip


'''
Solution 2:
Dynamic Programming

Create two lists: flip0 and flip1.

flip0[i]: stores the flip numbers in substring [0,...i-1] of 1->0.
          flip0[i] = flip0[i - 1] + int(s[i-1] == '1')

flip1[j]: stores the flip numbers in substring [j, n-1] of 0->1.
          flip1[j] = flip1[j+1] + int(s[j] == '0')

for loop: 
   calculate the sum of flip0[i]+flip1[i], and get the minimum value.

time: O(n)
space: O(n)
'''

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        num = len(s)
        if num == 0:
            return None

        flip0 = [0 for _ in range(num + 1)]
        flip1 = [0 for _ in range(num + 1)]
        minflip = 1000000
        allflip = 0

        for des_i in range(num + 1):
            if des_i == 0:
                flip0[des_i] = 0
            else:
                flip0[des_i] = flip0[des_i - 1] + int(s[des_i - 1] == '1')

        for des_j in range(num, -1, -1):
            if des_j == num:
                flip1[des_j] = 0
            else:
                flip1[des_j] = flip1[des_j + 1] + int(s[des_j] == '0')

        for i in range(num + 1):
            allflip = flip0[i] + flip1[i]
            if allflip < minflip:
                minflip = allflip
        return minflip


'''
Solution 3:

create two variables: 
    presum: sum of '1' before j, [0, j-1]
    postsum: sum of '1' after j, [j, num]

for loop on list s, [0:len(s)]
    
    presum += int(s[j-1]=='1')
    postsum -= int(s[j-1]=='1')
    flip0 = presum
    flip1 = num-j-postsum


time: O(n)
space: O(1)
'''
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        num = len(s)
        if num ==0:
            return None

        postsum = 0
        presum = 0
        minFlip = num
        for i in range(num):
            postsum += int(s[i]=='1')

        for j in range(num+1):
            if j == 0:
                flip0 = 0
                flip1 = num - postsum
            elif j == num:
                presum += int(s[j-1] == '1')
                flip0 = presum
                flip1 = 0
            else:
                presum += int(s[j-1]=='1')
                postsum -= int(s[j-1]=='1')
                flip0 = presum
                flip1 = num-j-postsum

            allflip = flip0 + flip1
            if allflip < minFlip:
                minFlip = allflip
        return minFlip







