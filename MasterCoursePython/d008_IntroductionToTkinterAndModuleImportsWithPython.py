# Tkinter
# Imports of modules
# import tkinter as tk # An alias is added to tkinter
# Import everything from a module
from tkinter import *

# Creating the main window
var_root = Tk()

# Cretion of the label
var_menssage = Label(var_root, text="My first program with Tkinter.") 

# Show the label 
var_menssage.pack()

# Implementation loop
var_root.mainloop();