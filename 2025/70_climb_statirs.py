def climbStairs(n):
    if n <= 0: return None
    if n == 1: return 1
    if n == 2: return 2

    return climbStairs(n-1) + climbStairs(n-2)



def climnStairs_topdown(n):
    dp = [0 for _ in range(n+1)]
    if n <= 1: return 1
    if n == 2: return 2

    if dp[n] == 0:
        dp[n] = climnStairs_topdown(n-1) + climnStairs_topdown(n-2)

    return dp[n]

def_climbStairs_bottomup(n):




n = 6
print(climbStairs(n))
print(climnStairs_topdown(n))