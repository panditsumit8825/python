# def tail_fact(n, acc=1):
#     if n == 0:
#         return acc
#     else:
#         return tail_fact(n-1, acc * n)

# def nontail_fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * nontail_fact(n-1)
        
# print(tail_fact(5))  
# print(nontail_fact(5))

# def countdown(n):
#   if n <= 0:
#     print("Done!")
#   else:
#     print(n)
#     countdown(n - 1)

# countdown(5)
def print_board(board):
    """Renders the 3x3 game board in the console."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    """Checks if the given player has won the match."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def is_board_full(board):
    """Checks if all squares are filled (draw condition)."""
    return all(space in ['X', 'O'] for space in board)

def play_game():
    """Main game loop managing turns, inputs, and termination logic."""
    # Initialize board with positions numbered 1 through 9
    board = [str(i) for i in range(1, 10)]
    current_player = 'X'
    game_over = False

    print("--- Welcome to Tic-Tac-Toe! ---")
    print("To play, enter a number from 1 to 9 corresponding to the grid position.")

    while not game_over:
        print_board(board)
        
        try:
            choice = int(input(f"Player {current_player}, choose your spot (1-9): "))
            
            # Convert user entry to 0-indexed list pointer
            position = choice - 1
            
            if choice < 1 or choice > 9:
                print("❌ Invalid number! Please pick a number between 1 and 9.")
                continue
                
            if board[position] in ['X', 'O']:
                print("⚠️ That spot is already taken! Try another one.")
                continue
                
            # Execute move
            board[position] = current_player
            
            # Evaluate current game state
            if check_winner(board, current_player):
                print_board(board)
                print(f"🎉 Congratulations! Player {current_player} wins! 🎉")
                game_over = True
            elif is_board_full(board):
                print_board(board)
                print("🤝 It's a draw! Well played both!")
                game_over = True
            else:
                # Alternate turns
                current_player = 'O' if current_player == 'X' else 'X'
                
        except ValueError:
            print("❌ Input error! You must type a valid integer.")

if __name__ == "__main__":
    play_game()
