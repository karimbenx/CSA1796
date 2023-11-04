import math

def evaluate(board):
    # Check rows, columns, and diagonals for a win/loss
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != '-':
            return 1 if board[row][0] == 'X' else -1
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            return 1 if board[0][col] == 'X' else -1
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return 1 if board[0][0] == 'X' else -1
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return 1 if board[0][2] == 'X' else -1
    return 0  # If no winner yet

def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board)

    if score != 0:
        return score

    if depth == 0:
        return 0

    if is_maximizing:
        best_val = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    value = minimax(board, depth - 1, False, alpha, beta)
                    best_val = max(best_val, value)
                    alpha = max(alpha, best_val)
                    board[i][j] = '-'
                    if beta <= alpha:
                        break
        return best_val
    else:
        best_val = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    value = minimax(board, depth - 1, True, alpha, beta)
                    best_val = min(best_val, value)
                    beta = min(beta, best_val)
                    board[i][j] = '-'
                    if beta <= alpha:
                        break
        return best_val

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    alpha = -math.inf
    beta = math.inf

    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'X'
                move_val = minimax(board, 4, False, alpha, beta)
                board[i][j] = '-'
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

# Example of using alpha-beta pruning in a Tic-Tac-Toe game
board_state = [
    ['X', '-', 'O'],
    ['O', 'X', '-'],
    ['-', '-', 'X']
]

best_move = find_best_move(board_state)
print("Best Move:", best_move)
