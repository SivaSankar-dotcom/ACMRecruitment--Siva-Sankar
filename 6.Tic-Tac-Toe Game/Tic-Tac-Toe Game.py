import random

def print_board(board):
    """Prints the current state of the board."""
    print("\n".join([
        " ".join(board[0:3]),
        " ".join(board[3:6]),
        " ".join(board[6:9])
    ]))
    print()

def check_winner(board, player):
    """Checks if the specified player has won."""
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_full(board):
    """Checks if the board is full (no empty spaces)."""
    return all(cell != ' ' for cell in board)

def player_move(board):
    """Handles the player's move."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Please enter a number between 1 and 9.")
            elif board[move] != ' ':
                print("Invalid move. The cell is already occupied.")
            else:
                board[move] = 'X'
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def computer_move(board):
    """Handles the computer's move."""
    empty_cells = [i for i, cell in enumerate(board) if cell == ' ']
    move = random.choice(empty_cells)
    board[move] = 'O'
    print(f"Computer chose position {move + 1}")

def main():
    board = [' '] * 9
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        player_move(board)
        print_board(board)
        
        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        
        if is_full(board):
            print("It's a draw!")
            break
        
        computer_move(board)
        print_board(board)
        
        if check_winner(board, 'O'):
            print("Computer wins!")
            break
        
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
