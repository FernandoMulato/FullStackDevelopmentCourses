# Imports
from tkinter import *

# Creating the main window
var_root = Tk()

# Title in the window
var_root.title("Tkinter Course")

"""# Data entry
# Customize widget entry
var_input = Entry(var_root, 
                background="springgreen", 
                border=3, 
                foreground="red", 
                width=30,
                ).pack()

# Event for the button
# Customize widget label 
def click_Send():
    Label(var_root, 
        text="The button has been pressed.",
        background="skyblue",
        width=25
        ).pack()

# Button
# Customize widget button 
var_button = Button(var_root, 
                    text="Send", 
                    command=click_Send,
                    background="deepskyblue",
                    foreground="gray98",
                    border=3,
                    width=26
                    ).pack()"""
"""
# Widget Labelframe
# Set margins between frame and window
var_frame = LabelFrame(var_root, 
                        text="Frame in the main window",
                        padx=20,
                        pady=20
                        )
var_frame.pack(padx=15, pady=15)

# Data entry
# Place items within the frame
var_input = Entry(var_frame, 
                    background="springgreen",
                    border=5,
                    foreground="red",
                    width=30
                    )

var_input.pack()
var_input.insert(0, "Write your name...")
var_input.bind("<Button-1>", lambda e: var_input.delete(0, END))

# Function for the button
def click_Send():
    var_name = var_input.get() # Gets and stores a name 
    Label(var_frame, 
        text=f"Hi {var_name}",
        background="skyblue",
        width=27
        ).pack()
var_input.delete(0, END)
var_input.insert(0, "Write your name...")

# Send button 
var_button = Button(var_frame, 
                    text="Send", 
                    command=click_Send,
                    background="deepskyblue",
                    foreground="gray98",
                    border=3,
                    width=26
                    ).pack()
"""
"""
# Create multiple frames in one window
frame_1 = LabelFrame(var_root, text="Data entry", padx=20, pady=20)
frame_1.pack(padx=15, pady=15)

frame_2 = LabelFrame(var_root, text="Send", padx=20, pady=20)
frame_2.pack(padx=5, pady=15)

frame_3 = LabelFrame(var_root, text="Result", padx=20, pady=20)
frame_3.pack(padx=5, pady=15)
"""

# Create multiple frames in one window with grid
frame_1 = LabelFrame(var_root, text="Data entry", padx=20, pady=20)
frame_1.grid(row=0, column=0, padx=15, pady=15)

frame_2 = LabelFrame(var_root, text="Send", padx=20, pady=20)
frame_2.grid(row=1, column=0, padx=5, pady=15)

frame_3 = LabelFrame(var_root, text="Result", padx=20, pady=20)
frame_3.grid(row=0, column=1, padx=5, pady=15)
# Data entry
# Place items within the frame
var_input = Entry(frame_1, 
                    background="springgreen",
                    border=5,
                    foreground="red",
                    width=30
                    )
var_input.pack()
var_input.insert(0, "Write your name...")
var_input.bind("<Button-1>", lambda e: var_input.delete(0, END))

# Function for the button
def click_Send():
    var_name = var_input.get() # Gets and stores a name 
    Label(frame_3, 
        text=f"Hi {var_name}",
        background="skyblue",
        width=27
        ).pack()
var_input.delete(0, END)
var_input.insert(0, "Write your name...")

# Send button 
var_button = Button(frame_2, 
                    text="Send", 
                    command=click_Send,
                    background="deepskyblue",
                    foreground="gray98",
                    border=3,
                    width=26
                    ).pack()

# Implementation loop
var_root.mainloop()