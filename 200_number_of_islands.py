'''
200: (medium)  vs. 1254

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.


Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.


'''

'''
**************************************************************
use DFS: Depth-First Search (DFS) 

这道求岛屿数量的题的本质是求矩阵中连续区域('1')的个数，
很容易想到需要用深度优先搜索 DFS 来解:

遍历一遍数组，遇到陆地('1')，则开始 DFS 遍历(4 directions)，并标记连通区域(to '2')，此时找到一个连通区域之后就可以增加岛屿的个数了.

'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # define DFS function, stop at borders or not '1's
        def DFS(grid, m, n, i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
                return
            # mark as '2' if it has already visited
            grid[i][j] = '2'
            DFS(grid, m, n, i - 1, j)
            DFS(grid, m, n, i + 1, j)
            DFS(grid, m, n, i, j - 1)
            DFS(grid, m, n, i, j + 1)

        # loop for each '1'
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '1':
                    continue
                DFS(grid, m, n, i, j)
                res += 1
        return res




'Breadth-First Search (BFS)'