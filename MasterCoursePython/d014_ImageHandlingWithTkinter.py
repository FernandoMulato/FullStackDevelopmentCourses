# Imports
from tkinter import *
# Import the python os module
import os
#Import parts of a module
from PIL import ImageTk, ImageColor, Image

# Store folder paths in python
# --- loading directories ---
# Main directory 
main_directory = os.path.dirname(__file__) # dynamic paths in python

# Directory images
directory_image = os.path.join(main_directory, "pictures")
directory_landscapes = os.path.join(directory_image, "landscapes")

# Creating the main window
var_root = Tk()

# Title in the window
var_root.title("Tkinter Course")

# Icon in the window
var_root.iconbitmap(os.path.join(directory_image, "live_pictures_15405.ico"))

# Load image and Resize images from code
# Round corners of an image (with Paintools)
picture = ImageTk.PhotoImage(Image.open(os.path.join(directory_landscapes, "image_002.png")).resize((350, 200)))
label = Label(image=picture)
label.pack()

# Implementation loop
var_root.mainloop()