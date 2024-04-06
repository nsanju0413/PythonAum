#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, messagebox

class MPGFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.message = ""
        self.pack()  #packing all widjets one after another in a window
        
# self is used as instance of the class in contrast to @variable name in other languages
# we always put self as the 1st argument in any function call
# variable names are -- self.varName = tk.StringVar()

        # Define string variables for text entry fields
        self.milesDriven = tk.StringVar()
        self.gallonsUsed = tk.StringVar()
        self.milesPerGallon = tk.StringVar()
# self.xx = tk.IntVar() is used for Radiobutton/Checkbutton

#sticky means widjet placed to the -- E (right), W (left) "" (center)
        
        # Display the grid of components
        ttk.Label(self, text="Miles Driven:").grid(row=0,column=0,sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.milesDriven).grid(row=0,column=1)

        ttk.Label(self, text="Gallons of Gas Used:").grid(row=1,column=0,sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.gallonsUsed).grid(row=1,column=1)

        ttk.Label(self, text="Miles Per Gallon:").grid(row=2,column=0,sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.milesPerGallon,state="readonly").grid(row=2,column=1)
    
        ttk.Button(self, text="Calculate",command=self.calculate).grid(row=3,column=1,sticky=tk.E)

        # Add padding to all components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)  # Nbr of rows = x, Nbr of cols = y
            
    def validate_inpt(self, val, fieldName):   # validation routine
        try:
            vl = float(val)
            if (vl == 0) :
                self.message += f"{fieldName} must be a non-zero number.\n"
            else:
                return vl
        except ValueError:
            self.message += f"{fieldName} must be a valid number.\n"
            
            
    def calculate(self):
        self.message = "" # clear any previous error message
        
        # Get numbers from the first two text entry fields
        milesDriven = self.validate_inpt(self.milesDriven.get(), "Miles driven")
        gallonsUsed = self.validate_inpt(self.gallonsUsed.get(), "Gallons of gas used")

        if self.message == "":
            # Calculate the miles per gallon (mpg)
            mpg = milesDriven / gallonsUsed
            mpg = round(mpg, 2)

            # Display the miles per gallon in the third text field
            self.milesPerGallon.set(mpg)
        else:
            messagebox.showerror("Error", self.message)

if __name__ == "__main__":
    root = tk.Tk()   # creates an instance of thinter frame
    root.title("Miles Per Gallon Calculator")
    MPGFrame(root)   # Frame class is called for
    root.mainloop()  #last line that executes the app until thje
                     #user exits the window or waits for other event
