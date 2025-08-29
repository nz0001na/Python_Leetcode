class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0: return None
        dp = [0]*(n+1)
        if len(dp) == 2: return 1
        if len(dp) == 3: return 2
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3, len(dp), 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

        