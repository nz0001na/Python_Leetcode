'''
des_i as target index of dividing 0 and 1 strings.
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
'''


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        num = len(s)
        if num == 0:
            return None

        minFlip = num
        flip0 = 0
        flip1 = 0
        for i in range(num + 1):
            if i == 0:
                flip0 = 0
                flip1 = s.count('0')
            elif i == num:
                flip0 = s.count('1')
                flip1 = 0
            else:
                flip0 = s[0:i].count('1')
                flip1 = s[i:num].count('0')
            if flip0 + flip1 < minFlip:
                minFlip = flip0 + flip1
        return minFlip




'''
用动态规划 Dynamic Programming 来做，需要使用两个 dp 数组，其中 
flip0[i] 表示将范围是 [0, i-1] 的子串内最小的将1转为0的个数，从而形成单调字符串。
同理，flip1[j] 表示将范围是 [j, n-1] 的子串内最小的将0转为1的个数，从而形成单调字符串。
这样最终在某个位置使得 flip0[i]+flip1[i] 最小的时候，就是变为单调串的最优解，

O(n)
O(n)
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
presum: sum of '1' before j, [0, j-1]
postsum: sum of '1' after j, [j, num]
O(n)
O(1)
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







