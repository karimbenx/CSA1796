import math

# Function to find the best move using Minimax algorithm
def find_best_move(piles):
    max_depth = 5  
    best_val = -math.inf
    best_move = -1

    for i in range(len(piles)):
        if piles[i] > 0:
            piles[i] -= 1  # Try a move
            value = minimax(piles, max_depth, False)  

            # Revert the move
            piles[i] += 1

            if value > best_val:
                best_val = value
                best_move = i

    return best_move

# Minimax algorithm
def minimax(piles, depth, is_maximizing):
    if depth == 0 or sum(piles) == 0:  
        return 1 if is_maximizing else -1

    if is_maximizing:
        best_val = -math.inf
        for i in range(len(piles)):
            if piles[i] > 0:
                piles[i] -= 1  # Try a move
                value = minimax(piles, depth - 1, False)  
                piles[i] += 1  
                best_val = max(best_val, value)
        return best_val
    else:
        best_val = math.inf
        for i in range(len(piles)):
            if piles[i] > 0:
                piles[i] -= 1  
                value = minimax(piles, depth - 1, True)  # Call Minimax for opponent
                piles[i] += 1  
                best_val = min(best_val, value)
        return best_val


game_piles = [3, 4, 5]  
player_turn = True  

while sum(game_piles) > 0:
    print("Current piles:", game_piles)
    if player_turn:
        pile_choice = find_best_move(game_piles)
        print("Player 1 takes", game_piles[pile_choice], "from pile", pile_choice + 1)
    else:
        pile = int(input("Player 2: Enter pile number: ")) - 1
        stones = int(input("Enter stones to remove: "))
        while stones > game_piles[pile]:
            stones = int(input("Invalid input. Enter stones to remove: "))
        game_piles[pile] -= stones
        print("Player 2 takes", stones, "from pile", pile + 1)

    player_turn = not player_turn

if player_turn:
    print("Player 2 wins!")
else:
    print("Player 1 wins!")

  
