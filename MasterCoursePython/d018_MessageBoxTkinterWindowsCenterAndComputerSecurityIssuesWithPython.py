# Block 1 - Messagebox

# Imports
from tkinter import *
from tkinter.messagebox import *

# Creating the main window
var_root = Tk()

# Tittle in the window  
var_root.title("Tkinter Course")

# Messagebox showinfo
# Function for information message
def op_show_info():
    showinfo("Information", "--------Information Message--------")

# Messagebox showwarning
# Function for warning message
def op_show_warning():
    showwarning("Warning", "--------Warning Message--------")

# Messagebox showerror
# Function for error message
def op_show_error():
    showerror("Error", "--------Error Message--------")

# Messagebox askquestion
# Function for question
def op_show_question():
    askquestion("Question", "--------Question--------")

# Messagebox askyesno
# Function for question
def op_show_yesno():
    askyesno("Question", "--------Question yesno--------")

# Messagebox askokcancel
# Function for question
def op_show_okcancel():
    askokcancel("Question", "--------Menssage okcancel--------")

# Messagebox askyesnocancel
# Function for question
def op_show_yesnocancel():
    askyesnocancel("Question", "--------Menssage yesnocancel--------")

# Messagebox askretrycancel
# Function for question
def op_show_retrycancel():
    askretrycancel("Question", "--------Menssage retrycancel--------")

# Button to call the function
var_button = Button(var_root, text="Send", width=75, command=op_show_retrycancel).pack()

# Implementation loop
var_root.mainloop()


# Block 2 - Screen and window adjustment

# Center to the window #1
# Imports
import tkinter as tk

# --- MAIN WINDOW----> root

# Creating the main window
var_root =  tk.Tk()

# Tittle in the window
var_root.title("Tkinter Course")

var_root.geometry()

# Screen and window adjustment

# PlaceWindow and eval method
var_root.eval('tk::PlaceWindow . center')

#---WIDGETS----> root

# Data entry
var_input = tk.Entry(var_root).pack()

# Send button
var_button = tk.Button(var_root, text="Send").pack()

# Implementation loop
var_root.mainloop()

# Center to the window #2
# Imports
from tkinter import *
# Main window
var_root = Tk()
var_root.title("Tkinter Course")
# Method resizable: (False: cannot resize width, False: cannot resize height)
var_root.resizable(False, False)
var_window_width = 500
var_window_height = 400

# Dynamically get window size
# Screen
# Get width
var_screen_width = var_root.winfo_screenwidth()
# Get height
var_screen_height = var_root.winfo_screenheight()

coordinate_x = int((var_screen_width/2)-(var_window_width/2))
coordinate_y = int((var_screen_height/2)-(var_window_height/2))-37

var_root.geometry("{}x{}+{}+{}".format(var_window_width, var_window_height, coordinate_x, coordinate_y))

Label(text=f"Screen width: {var_screen_width} pixels.").pack()
Label(text=f"Screen height: {var_screen_height} pixels.").pack()

# Implementation loop
var_root.mainloop()

# Options for window appearance
# Imports
from tkinter import *
# Main window
var_root = Tk()
var_root.title("Tkinter Course")
# Method resizable: (False: cannot resize width, False: cannot resize height)
var_root.resizable(False, False)

# Maximized window
var_root.state("zoomed")

# The screen is not visible
var_root.state("withdrawn")
var_root.deiconify()

# Implementation loop
var_root.mainloop()

# Block 3 - Python computer security

# Exception

# try: 
#    var_number = eval(input('Enter a number: '))
#    var_result = var_number * var_number
#    print(var_result)
#except:
#    print("Error")

# Please do not run!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Remove empty folders with os module
# import os
# os.rmdir('AddressToRemove')

# Delete folders with items with shutil
# from shutil import *
# rmtree('AddressToRemove')

# Code injection with eval
# var_ result = "shutil.rmtree('AddressToRemove')" (in console)

# Inject imports in python
# __import__('shutil').rmtree('AddressToRemove')


