# Loops
# for
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
    print(f"-{var_color}.")

# Skip certain executions in the loop
print("\n---Color list---")
for var_color in lst_colors:
    if var_color == "Blue" or var_color == "Green":
        continue
    print(f"-Color {var_color}.")

# End the loop early
print("\n---Color list---")
for var_color in lst_colors:
    if var_color == "Blue":
        break
    print(f"-Color {var_color}.")

# While
i = 1
while i < 5:
    print(f"The loop value is: {i}.")
    i += 1 # Increase the while loop

while i >= -5:
    print(f"The loop value is: {i}.")
    i -= 1 # Decrease the while loop

# "Do while"
while True:
    var_output = input('Enter "exit" to finish.\n').lower()
    if var_output == "exit":
        break