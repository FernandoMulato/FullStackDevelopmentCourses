# Lists
lst_colors = ["Red", "Blue", "Green", "Yellow"]

# Print a list item
print(f"The second item on the list is: {lst_colors[1]}")

# Print a character of a word in the list
print(lst_colors[3][5])

# Elements from last to first
print(lst_colors[-1])
print(lst_colors[-2])

# Reassign values to a list
lst_colors[1] = "Orange"
print(lst_colors)

# Add values to lists
lst_colors.append("Blue") # Added at the end of the list
print(lst_colors)

lst_colors.insert(2, "Black") # Added to a specified list position
print(lst_colors)

# Empty lists
#lst_colors.clear() 
print(lst_colors)

# Remove item from list
lst_colors.pop(3)
print(lst_colors)

# Remove literal element from list
lst_colors.remove("Red")
print(lst_colors)

# Duplicate lists
lst_Copy = lst_colors.copy()
lst_Copy = lst_colors
print(lst_Copy)

# Count repeated values in lists
lst_new = ["Red", "Blue", "Green", "Red", "Red", "Yellow"]
print(lst_new.count("Red"))

# Find the position of the literal element in a list
print(lst_new.index("Red"))

# Invert the order of items in a list
lst_new.reverse()
print(lst_new)

# Sort list items in alphabetical order
lst_new.sort()
print(lst_new)

# Sort items in alphabetical order in descending order
lst_new.sort(reverse=True)
print(lst_new)

# Join two lists
lst_colors.extend(lst_new)
print(lst_colors)

# Add a literal string to a list with the characters separated by positions
lst_new.extend("Orange")
print(lst_new)

# Tuples (only serves the view)
tpl_colors = ("Red", "Blue", "Green", "Yellow")
print(tpl_colors[1])

# Count items from a list or tuple
print(len(lst_new))
print(len(tpl_colors))