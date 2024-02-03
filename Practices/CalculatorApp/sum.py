#sum = 1 + 2
#print(sum)


# sum = 1 + 2
# product = sum * 2
# print(product)


import tkinter as tk

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")

        self.entry = tk.Entry(self.root, width=20, font=('Arial', 14), bd=5, insertwidth=4, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '+', '-', '*', '/',
            '%', '=', 'C'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.root, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda btn=button: self.click(btn)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click(self, button):
        if button == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button == 'C':
            self.entry.delete(0, tk.END)
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text + button)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
