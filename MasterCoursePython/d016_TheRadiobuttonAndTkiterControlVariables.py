# Imports
from tkinter import *

# Creating the main window
var_root = Tk()

# Tittle in the window 
var_root.title("Tkinter Course")

# The control variables
# type of control variables: IntVar, DoubleVar, StringVar, BooleanVar
var_option = IntVar()
# Set values from code to control variables
var_option.set(4)

# Update function for radio buttons
def op_update_radio(prm_value):
    Label(var_root, text=prm_value).pack()

# Radiobutton
# Create a radiobutton
Radiobutton(var_root,
            text="Red",
            variable=var_option,
            value=1
            ).pack()

Radiobutton(var_root,
            text="Blue",
            variable=var_option,
            value=2
            ).pack()

Radiobutton(var_root,
            text="Green",
            variable=var_option,
            value=3
            ).pack()

Radiobutton(var_root,
            text="Yellow",
            variable=var_option,
            value=4
            ).pack()

# The get method of control variables
# Label(var_root, text=f"{var_option.get()}").pack()

# Send button
var_send_button = Button(var_root,
                        text="Send",
                        command=lambda:op_update_radio(var_option.get())).pack()

# Implementation loop
var_root.mainloop()