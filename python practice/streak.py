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
# def print_board(board):
#     """Renders the 3x3 game board in the console."""
#     print("\n")
#     print(f" {board[0]} | {board[1]} | {board[2]} ")
#     print("---|---|---")
#     print(f" {board[3]} | {board[4]} | {board[5]} ")
#     print("---|---|---")
#     print(f" {board[6]} | {board[7]} | {board[8]} ")
#     print("\n")

# def check_winner(board, player):
#     """Checks if the given player has won the match."""
#     win_conditions = [
#         [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
#         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
#         [0, 4, 8], [2, 4, 6]              # Diagonals
#     ]
#     return any(all(board[i] == player for i in condition) for condition in win_conditions)

# def is_board_full(board):
#     """Checks if all squares are filled (draw condition)."""
#     return all(space in ['X', 'O'] for space in board)

# def play_game():
#     """Main game loop managing turns, inputs, and termination logic."""
#     # Initialize board with positions numbered 1 through 9
#     board = [str(i) for i in range(1, 10)]
#     current_player = 'X'
#     game_over = False

#     print("--- Welcome to Tic-Tac-Toe! ---")
#     print("To play, enter a number from 1 to 9 corresponding to the grid position.")

#     while not game_over:
#         print_board(board)
        
#         try:
#             choice = int(input(f"Player {current_player}, choose your spot (1-9): "))
            
#             # Convert user entry to 0-indexed list pointer
#             position = choice - 1
            
#             if choice < 1 or choice > 9:
#                 print("❌ Invalid number! Please pick a number between 1 and 9.")
#                 continue
                
#             if board[position] in ['X', 'O']:
#                 print("⚠️ That spot is already taken! Try another one.")
#                 continue
                
#             # Execute move
#             board[position] = current_player
            
#             # Evaluate current game state
#             if check_winner(board, current_player):
#                 print_board(board)
#                 print(f"🎉 Congratulations! Player {current_player} wins! 🎉")
#                 game_over = True
#             elif is_board_full(board):
#                 print_board(board)
#                 print("🤝 It's a draw! Well played both!")
#                 game_over = True
#             else:
#                 # Alternate turns
#                 current_player = 'O' if current_player == 'X' else 'X'
                
#         except ValueError:
#             print("❌ Input error! You must type a valid integer.")

# if __name__ == "__main__":
#     play_game()


# import turtle
# import time
# import random

# # Game Configuration
# DELAY = 0.1
# SCORE = 0
# HIGH_SCORE = 0

# # Set up the screen
# screen = turtle.Screen()
# screen.title("Snake Game")
# screen.bgcolor("black")
# screen.setup(width=600, height=600)
# screen.tracer(0)  # Turns off automatic screen updates for smooth animation

# # Snake Head
# head = turtle.Turtle()
# head.speed(0)
# head.shape("square")
# head.color("green")
# head.penup()
# head.goto(0, 0)
# head.direction = "stop"

# # Snake Food
# food = turtle.Turtle()
# food.speed(0)
# food.shape("circle")
# food.color("red")
# food.penup()
# food.goto(0, 100)

# # Snake Body Segments
# segments = []

# # Score Display
# pen = turtle.Turtle()
# pen.speed(0)
# pen.shape("square")
# pen.color("white")
# pen.penup()
# pen.hideturtle()
# pen.goto(0, 260)
# pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# # Movement Functions
# def go_up():
#     if head.direction != "down":
#         head.direction = "up"

# def go_down():
#     if head.direction != "up":
#         head.direction = "down"

# def go_left():
#     if head.direction != "right":
#         head.direction = "left"

# def go_right():
#     if head.direction != "left":
#         head.direction = "right"

# def move():
#     if head.direction == "up":
#         y = head.ycor()
#         head.sety(y + 20)
#     if head.direction == "down":
#         y = head.ycor()
#         head.sety(y - 20)
#     if head.direction == "left":
#         x = head.xcor()
#         head.setx(x - 20)
#     if head.direction == "right":
#         x = head.xcor()
#         head.setx(x + 20)

# def reset_game():
#     global SCORE, DELAY
#     time.sleep(1)
#     head.goto(0, 0)
#     head.direction = "stop"
    
#     # Hide and clear segments
#     for segment in segments:
#         segment.goto(1000, 1000)
#     segments.clear()
    
#     SCORE = 0
#     DELAY = 0.1
#     update_score_display()

# def update_score_display():
#     pen.clear()
#     pen.write(f"Score: {SCORE}  High Score: {HIGH_SCORE}", align="center", font=("Courier", 24, "normal"))

# # Keyboard Bindings
# screen.listen()
# screen.onkeypress(go_up, "Up")
# screen.onkeypress(go_down, "Down")
# screen.onkeypress(go_left, "Left")
# screen.onkeypress(go_right, "Right")

# # Main Game Loop
# while True:
#     screen.update()

#     # Check for wall collisions
#     if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
#         reset_game()

#     # Check for food collisions
#     if head.distance(food) < 20:
#         # Move food to a random position
#         x = random.randint(-280, 280)
#         y = random.randint(-280, 280)
#         food.goto(x, y)

#         # Add a new segment to the snake body
#         new_segment = turtle.Turtle()
#         new_segment.speed(0)
#         new_segment.shape("square")
#         new_segment.color("lightgreen")
#         new_segment.penup()
#         segments.append(new_segment)

#         # Shorten delay to slightly speed up the game
#         DELAY -= 0.003

#         # Update scoring
#         SCORE += 10
#         if SCORE > HIGH_SCORE:
#             HIGH_SCORE = SCORE
#         update_score_display()

#     # Move body segments in reverse order (tail follows body)
#     for index in range(len(segments) - 1, 0, -1):
#         x = segments[index - 1].xcor()
#         y = segments[index - 1].ycor()
#         segments[index].goto(x, y)

#     # Move segment 0 to where the head is
#     if len(segments) > 0:
#         x = head.xcor()
#         y = head.ycor()
#         segments[0].goto(x, y)

#     move()

#     # Check for self collisions
#     for segment in segments:
#         if segment.distance(head) < 20:
#             reset_game()

#     time.sleep(DELAY)

# screen.mainloop()

