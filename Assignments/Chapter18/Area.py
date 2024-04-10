
import tkinter as tk
from tkinter import ttk, messagebox

class RectangleFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack()


        self.length = tk.StringVar()
        self.width = tk.StringVar()
        self.area = tk.StringVar()
        self.perimeter = tk.StringVar()


        ttk.Label(self, text="Length:").grid(row=0, column=0, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.length).grid(row=0, column=1)

        ttk.Label(self, text="Width:").grid(row=1, column=0, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.width).grid(row=1, column=1)

        ttk.Label(self, text="Area:").grid(row=2, column=0, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.area, state="readonly").grid(row=2, column=1)

        ttk.Label(self, text="Perimeter:").grid(row=3, column=0, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.perimeter, state="readonly").grid(row=3, column=1)

        ttk.Button(self, text="Calculate", command=self.calculate).grid(row=4, column=1, sticky=tk.E)


        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def validate_input(self, val, field_name):
        try:
            vl = float(val)
            if vl <= 0:
                messagebox.showerror("Error", f"{field_name} must be a positive number.")
                return False
            return vl
        except ValueError:
            messagebox.showerror("Error", f"{field_name} must be a valid number.")
            return False

    def calculate(self):
        length = self.validate_input(self.length.get(), "Length")
        width = self.validate_input(self.width.get(), "Width")

        if length and width:
            area = length * width
            perimeter = 2 * (length + width)

            self.area.set(round(area, 2))
            self.perimeter.set(round(perimeter, 2))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Rectangle Area and Perimeter Calculator")
    RectangleFrame(root)
    root.mainloop()
