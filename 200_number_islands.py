'''
200. Number of Islands
Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3

'''

# DFS
def DFS(grid, visit, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0' or visit[i][j] == 1:
        return
    visit[i][j] = 1
    DFS(grid, visit, i, j-1)
    DFS(grid, visit, i-1, j)
    DFS(grid, visit, i, j+1)
    DFS(grid, visit, i+1, j)


def findisland(grid):
    row = len(grid)
    if row <= 0:
        return None
    col = len(grid[0])
    if col <= 0:
        return None
    visit = [[[0] for m in range(col)] for n in range(row)]
    res = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '0' or visit[i][j] == 1:
                continue
            DFS(grid, visit, i, j)
            res += 1
    return res


# BFS
def findisland2()


grid = [
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
grid = [
    ["0","1","0"],
    ["1","0","1"],
    ["0","1","0"]]
print(findisland(grid))