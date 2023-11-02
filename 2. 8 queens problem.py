#N defines the size of chessboard
N = 8

def NQueens(board, col):
    if col == N:
        print_board(board)
        return True

    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if NQueens(board, col + 1):
                return True
            board[i][col] = 0
    return False

def isSafe(board, row, col):
    for x in range(col):
        if board[row][x] == 1:
            return False

    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    for x, y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    for x, y in zip(range(row, -1, -1), range(col, N, 1)):
        if board[x][y] == 1:
            return False

    return True

def print_board(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

board = [[0 for x in range(N)] for y in range(N)]
if not NQueens(board, 0):
    print("No solution found")
