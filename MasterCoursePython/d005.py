# Loops
for i in range(6):
    print(f"The loop value is: {i}.")
print("End of the loop\n")

# range(start, stop)
for i in range(3, 7):
    print(f"The loop value is: {i}.")
print("End of the loop\n")

# Change range increment: range(start, stop, step)
for i in range(3, 12, 3):
    print(f"The loop value is: {i}.")
print("End of the loop\n")

# Decrement
for i in range(3, -12, -3):
    print(f"The loop value is: {i}.")
print("End of the loop\n")

# Iterate lists or tuples in loops
lst_colors = ["Red", "Blue", "Green", "Yellow"]
print("---Color list---")

for var_color in lst_colors:
    print(f"-{var_color}")