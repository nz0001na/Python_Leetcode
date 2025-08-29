class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 0: return None
        if n == 0: return 0
        if n == 1 or n == 2: return 1

        pre1 = 0
        pre2 = 1
        pre3 = 1
        cur = 0
        for i in range(3, n+1):
            cur = pre1 + pre2 + pre3
            pre1 = pre2
            pre2 = pre3
            pre3 = cur
            cur = 0
        return pre3
        