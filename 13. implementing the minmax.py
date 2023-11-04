board = [[" " for _ in range(3)] for _ in range(3)]

def winner(b, p): 
    return any(p*3 in r for r in b + list(zip(*b)) + [b[i][i] for i in range(3)])

def minimax(b, d, m):
    s = 1 if winner(b, 'X') else (-1 if winner(b, 'O') else 0)
    if s != 0 or not any(' ' in r for r in b): return s

    v, f = (max, -float('inf')) if m else (min, float('inf'))
    for i in range(3):
        for j in range(3):
            if b[i][j] == " ":
                b[i][j] = 'X' if m else 'O'
                f = v(f, minimax(b, d + 1, not m))
                b[i][j] = " "
    return f

while not (winner(board, 'X') or winner(board, 'O') or not any(' ' in r for r in board)):
    if any(' ' in r for r in board): 
        bm = max(((i, j) for i in range(3) for j in range(3) if board[i][j] == " "), key=lambda x: minimax([r[:] for r in board], 0, False))
        board[bm[0]][bm[1]] = 'X'

print("\n".join(" | ".join(row) for row in board))
if winner(board, 'X'): print("AI wins!")
elif winner(board, 'O'): print("Player wins!")
elif not any(' ' in row for row in board): print("It's a draw!")
