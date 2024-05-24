'''
1254: medium

Given a 2D grid consists of 0s (land) and 1s (water).
An island is a maximal 4-directionally connected group of 0s and
a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.


Example 1:
Input: grid = [[1,1,1,1,1,1,1,0],
               [1,0,0,0,0,1,1,0],
               [1,0,1,0,1,1,1,0],
               [1,0,0,0,0,1,0,1],
               [1,1,1,1,1,1,1,0]]
Output: 2
Explanation:
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:
Input: grid = [[0,0,1,0,0],
               [0,1,0,1,0],
               [0,1,1,1,0]]
Output: 1


Example 3:
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2



Constraints:
    1 <= grid.length, grid[0].length <= 100
    0 <= grid[i][j] <=1

'''


'''
***************************************************************
use DFS:
这道题给了一个只包含0和1的二维数组 grid，0代表陆地，1代表海洋，
现在定义了被海洋上下左右包围的陆地为岛屿，现在问有多少个岛屿，
注意岛屿必须被海洋完全包围，和边界相连的陆地不算是岛屿。
既然岛屿是多个为0相连而形成的，那么肯定是要用 BFS 或 DFS 来找到连通区域的，
难点是怎么确定找到的连通区域是不是一个岛屿，关键在于若某个连通区域和边界相连了，则其就不是岛屿了。
我们可以反过来操作一下，

(1) 首先把所有和边界相连的连通区域(0)都找出来并标记(to 2)，这样之后再找到的连通区域就一定是岛屿了。
所以先遍历一遍数组grid，遇到边界上的陆地(0)，则开始 DFS 遍历，并标记连通区域(as 2)，完成了之后，

(2) 再次遍历一遍数组，遇到非边界上的陆地(0)，则开始 DFS 遍历，并标记连通区域，此时找到一个连通区域之后就可以增加岛屿的个数了.

'''


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1 or n == 1:
            return 0

        # define DFS function
        def dfs(grid, m, n, i, j):
            # base case, stop condition: out of index range or not 0
            if i < 0 or j < 0 or i > m - 1 or j > n - 1 or grid[i][j] != 0:
                return
            # mark to 2 showing it has been already visited
            grid[i][j] = 2
            # DFS in four directions
            dfs(grid, m, n, i - 1, j)
            dfs(grid, m, n, i, j + 1)
            dfs(grid, m, n, i, j - 1)
            dfs(grid, m, n, i + 1, j)

        # 1st loop: find all 0s on the borders
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j] == 0:
                    dfs(grid, m, n, i, j)

        # 2nd loop: find all 0s inside
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                dfs(grid, m, n, i, j)
                res += 1

        return res

