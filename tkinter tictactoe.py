import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic-Tac-Toe Game")
root.geometry("400x450")
root.config(bg="#282c34")

# Game state variables
current_player = "X"
board = [""] * 9

# Function to check for win or draw
def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # columns
        (0, 4, 8), (2, 4, 6)             # diagonals
    ]
    
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != "":
            highlight_winner(a, b, c)
            messagebox.showinfo("Game Over", f"Player {board[a]} wins!")
            reset_game()
            return True
    if "" not in board:
        messagebox.showinfo("Game Over", "It's a Draw!")
        reset_game()
        return True
    return False

# Function to highlight winning buttons
def highlight_winner(a, b, c):
    buttons[a].config(bg="#00b894")
    buttons[b].config(bg="#00b894")
    buttons[c].config(bg="#00b894")

# Function to handle button click
def button_click(index):
    global current_player

    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player, state="disabled", fg="#ffffff" if current_player == "X" else "#00a8ff")
        
        if check_winner():
            return
        
        current_player = "O" if current_player == "X" else "X"
        label.config(text=f"Player {current_player}'s Turn")

# Function to reset the game
def reset_game():
    global current_player, board
    current_player = "X"
    board = [""] * 9
    for button in buttons:
        button.config(text="", state="normal", bg="#2d3436")
    label.config(text="Player X's Turn")

# Create the GUI elements
buttons = [tk.Button(root, text="", font=("Helvetica", 24, "bold"), width=5, height=2,
                     bg="#2d3436", activebackground="#dfe6e9", command=lambda i=i: button_click(i))
           for i in range(9)]
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)

# Label to show the current player's turn
label = tk.Label(root, text="Player X's Turn", font=("Helvetica", 18, "bold"), fg="#dfe6e9", bg="#282c34")
label.grid(row=3, column=0, columnspan=3, pady=(20, 0))

# Reset button to restart the game
reset_button = tk.Button(root, text="Restart Game", font=("Helvetica", 14, "bold"), bg="#e17055", fg="#ffffff",
                         command=reset_game, relief="raised", borderwidth=2)
reset_button.grid(row=4, column=0, columnspan=3, pady=(15, 0))

# Run the main loop
root.mainloop()
