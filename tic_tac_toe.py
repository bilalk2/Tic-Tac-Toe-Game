import os

# Function to load wins from the file
def load_wins(file_path):
    if not os.path.exists(file_path):  # If file doesn't exist, return 0 wins for both players
        return {"Player X": 0, "Player O": 0}
    
    with open(file_path, 'r') as file:
        data = file.read().strip().split(',')
        return {"Player X": int(data[0]), "Player O": int(data[1])}

# Function to save wins to the file
def save_wins(file_path, wins):
    with open(file_path, 'w') as file:
        file.write(f"{wins['Player X']},{wins['Player O']}")

# Function to display the Tic Tac Toe board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if there's a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if row == [player, player, player]:
            return True
    for col in range(3):
        if [board[0][col], board[1][col], board[2][col]] == [player, player, player]:
            return True
    if [board[0][0], board[1][1], board[2][2]] == [player, player, player]:
        return True
    if [board[0][2], board[1][1], board[2][0]] == [player, player, player]:
        return True
    return False

# Function to check if the board is full (a draw)
def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

# Main function to play Tic Tac Toe
def play_game():
    # file_path = input ("Enter File path : ")
    file_path = "tic_tac_toe_wins.txt"
    wins = load_wins(file_path)

    print(f"Player X Wins: {wins['Player X']}")
    print(f"Player O Wins: {wins['Player O']}\n")

    board = [[" " for _ in range(3)] for _ in range(3)]  # Initialize empty board
    current_player = "X"  # Player X starts

    while True:
        display_board(board)
        print(f"\nPlayer {current_player}'s turn.")

        try:
            row, col = map(int, input("Enter row and column (0, 1, or 2) separated by space: ").split())
        except ValueError:
            print("Invalid input. Please enter two integers separated by space.")
            continue

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        board[row][col] = current_player  # Mark the board

        # Check if the current player has won
        if check_winner(board, current_player):
            display_board(board)
            print(f"\nPlayer {current_player} wins!")
            wins[f"Player {current_player}"] += 1  # Update the win count
            save_wins(file_path, wins)
            break

        # Check if the game is a draw
        if check_draw(board):
            display_board(board)
            print("\nThe game is a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'y':
        play_game()
    else:
        print(f"Final Wins - Player X: {wins['Player X']}, Player O: {wins['Player O']}")
        print("Thanks for playing!")

# Start the game
play_game()
