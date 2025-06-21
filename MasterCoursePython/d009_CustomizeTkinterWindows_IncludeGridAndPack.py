# Imports
from tkinter import *

# Creating the main window
var_root = Tk()

# Title in the window
var_root.title("Tkinter Course")

# Window size & Coordinates
var_root.geometry("800x600+560+240")

# Cretion of the label & Show the label 
var_message = Label(var_root, text="My first program with Tkinter.").grid(row=0, column=0)
var_message2 = Label(var_root, text="This is the second label").grid(row=0, column=1)

# Implementation loop
var_root.mainloop()