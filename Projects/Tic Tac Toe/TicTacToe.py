import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")

        self.current_player = 'X'
        self.board = [' '] * 9

        self.buttons = [tk.Button(self.root, text=' ', font=('Arial', 20), width=4, height=2,
                                  command=lambda idx=i: self.make_move(idx)) for i in range(9)]

        for i, button in enumerate(self.buttons):
            row_val = i // 3
            col_val = i % 3
            button.grid(row=row_val, column=col_val)

    def make_move(self, index):
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif ' ' not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def reset_game(self):
        for i in range(9):
            self.board[i] = ' '
            self.buttons[i].config(text=' ')

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    tic_tac_toe = TicTacToe()
    tic_tac_toe.run()
