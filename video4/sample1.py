def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row = int(input(f"Player {player}, choose row (1-3): ")) - 1
        col = int(input(f"Player {player}, choose column (1-3): ")) - 1

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        board[row][col] = player
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Congratulations! Player {winner} wins!")
            break

        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

if _name_ == "_main_":
    tic_tac_toe()