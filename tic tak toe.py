def printBoard(board):
    print(f"{0} | {1} | {2} ")
    print(f"--|---|---")
    print(f"{3} | {4} | {5} ")
    print(f"--|---|---")
    print(f"{6} | {7} | {8} ")

    print("Get Idea of Field From Table ")

    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"--|---|---")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"--|---|---")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def checkWin(board):
    # Define winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal wins
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical wins
        [0, 4, 8], [2, 4, 6]              # diagonal wins
    ]

    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ' ':
            return True  # Someone won
    return False


def checkDraw(board):
    return ' ' not in board  # The board is full, and no one has won


if __name__ == "__main__":
    board = [' '] * 9  # 3x3 grid initialized with empty spaces
    current_player = 'X'  # X always starts the game

    print("Welcome to Tic Tac Toe!")
    
    while True:
        printBoard(board)
        print(f"{current_player}'s turn")

        # Get player input
        try:
            move = int(input("Enter the position (0-8): "))
            if board[move] != ' ':
                print("Position already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 0 and 8.")
            continue

        # Place the move on the board
        board[move] = current_player

        # Check for a win
        if checkWin(board):
            printBoard(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a draw
        if checkDraw(board):
            printBoard(board)
            print("It's a draw!")
            break

        # Switch player turns
        current_player = 'O' if current_player == 'X' else 'X'