class Solution:
    def fib(self, n: int) -> int:
        if n < 0: return None
        if n == 0 or n == 1: return n
        
        pre1 = 0
        pre2 = 1
        cur = 0
        for i in range(2, n+1):
            cur = pre1 + pre2
            pre1 = pre2
            pre2 = cur
            cur = 0

        return pre2


        