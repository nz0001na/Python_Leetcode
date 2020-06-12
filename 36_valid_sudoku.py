'''
36. Valid Sudoku
Medium

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according
to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
'''

# directly check
def validsudoku(board):
    row = len(board)
    col = len(board[0])
    if row != 9 or col != 9:
        return None
    # rule 1
    for i in range(row):
        hashmap = {}
        for j in range(col):
            if board[i][j] == ".":
                continue
            if board[i][j] not in hashmap:
                hashmap[board[i][j]] = 1
            else:
                return False

    # rule 2
    for j in range(col):
        hashmap = {}
        for i in range(row):
            if board[i][j] == ".":
                continue
            if board[i][j] not in hashmap:
                hashmap[board[i][j]] = 1
            else:
                return False

    # rule 3
    point = [1, 4, 7]
    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    for i in point:
        hashmap = {}
        for j in range(9):
            x = i + dx[j]
            y = i + dy[j]
            if board[x][y] == ".":
                continue
            if board[x][y] not in hashmap:
                hashmap[board[x][y]] = 1
            else:
                return False
    return True


# check simultaneously, use set
def validsudoku2(board):
    kmap = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ".":
                continue
            s = (i // 3) * 3 + (j // 3)
            row = str(i) + "+" + str(board[i][j])
            col = str(j) + "-" + str(board[i][j])
            grd = str(s) + "=" + str(board[i][j])
            if row in kmap: return False
            if col in kmap: return False
            if grd in kmap: return False
            kmap.add(row)
            kmap.add(col)
            kmap.add(grd)
    return True

# check use hashmap
def validsudoku3(board):
    hashmap = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                continue
            k = (i // 3) * 3 + (j // 3)
            row = 'row:' + str(i) + ', value:' + board[i][j]
            col = 'col:' + str(j) + ', value:' + board[i][j]
            sub = 'sub:' + str(k) + ', value:' + board[i][j]
            if row in hashmap: return False
            if col in hashmap: return False
            if sub in hashmap: return False
            hashmap[row] = 1
            hashmap[col] = 1
            hashmap[sub] = 1
    return True


board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
board1 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(validsudoku3(board))
print(validsudoku3(board1))
