import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Number Guessing Game")
        self.random_number = random.randint(1, 10)
        self.attempts = 0

        self.label = tk.Label(self.root, text="Enter your guess:")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.guess_button = tk.Button(self.root, text="Guess", command=self.make_guess)
        self.guess_button.pack()

    def make_guess(self):
        try:
            user_input = int(self.entry.get())
            self.attempts += 1

            if 1 <= user_input <= 10:
                if self.random_number == user_input:
                    messagebox.showinfo("Congratulations!", f"The number is matched in {self.attempts} attempts!")
                    self.root.destroy()
                elif self.random_number < user_input:
                    messagebox.showinfo("Hint", "Number is greater than the entered value")
                else:
                    messagebox.showinfo("Hint", "Number is less than the entered value")
            else:
                messagebox.showwarning("Invalid Input", "Enter a number between 1 to 10")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.root.mainloop()
