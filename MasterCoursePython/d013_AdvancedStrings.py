# Advanced string

var_a = "Hey"
var_b = "What's going on?"

# Concatenation with operator " "
print(var_a + var_b)
var_b = 10
print(var_a + str(var_b))

# Concatenation with commas
print(var_a, var_b)
var_b = "What's going on?"

# Concatenation with the join method
print(" ".join([var_a, var_b]))

# join metrhon with list 
lst_colors = ["Red", "Blue", "Green", "Yellow"]
var_separator = "*"
var_concatenates = var_separator.join(lst_colors)
print(var_concatenates)

# Format strings with operator %
print("%s %s" % (var_a, var_b))

# Format strings with format method
print("{} {}".format(var_a, var_b))

# Format strings with f prefix
print(f"{var_a} {var_b}")

# Split strings into multiple lines
var_text = """We offer various chain connectors 
to integrate multiple components
into one single mooring line."""
print(var_text)

# Multiply strings
print((var_a+" ")*3)

# Iterating strings in python
for i in var_b:
    print(i)

# Iterate strings with the range 
var_input = input()
for i  in range(len(var_input)):
    print(var_input[i])

# Check matches in strings
print("chain" in var_text)
print("We" not in var_text)

# Generate a dictionary from a string
dcty_text = dict(enumerate(var_b))
print(dcty_text)

# Generate a list from a string
lst_text = list(enumerate(var_b))
print(lst_text)

# Generate a tuple from a string
tpl_text = tuple(enumerate(var_b))
print(tpl_text)

# Generate a set from a string
st_text = set(enumerate(var_b))
print(st_text)

# Single, double and triple quotes
var_string = """Hey, is your nickname "Junior"?"""
print(var_string)