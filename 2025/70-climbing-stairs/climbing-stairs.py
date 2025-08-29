class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0: return None
        if n == 1: return 1
        if n == 2: return 2

        prev1 = 1
        prev2 = 2
        curr = 0
        for i in range(3, n+1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
            curr = 0
        return prev2
     

        