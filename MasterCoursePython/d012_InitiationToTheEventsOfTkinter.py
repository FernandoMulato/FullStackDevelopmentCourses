# Imports
from tkinter import *

# Creating the main window
var_root = Tk()

# Title in the window
var_root.title("Tkinter Course")

# Data entry
var_input = Entry(var_root)
var_input.insert(0, "Write your name...")
#              Event         Controller
var_input.bind("<Button-1>", lambda x: var_input.delete(0, END)) # if instead of "Button-1" we put "Key" this will refer to any key on the keyboard

# Event for the button
def click_button():
    var_name = var_input.get()
    Label(var_root, text=f"{var_name}").pack()

# Button
Button(var_root, text="Push me!", command=click_button).pack()

# Implementation loop
var_root.mainloop()