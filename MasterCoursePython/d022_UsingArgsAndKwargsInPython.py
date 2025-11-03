# How is *args used?
def op_test(*args):
    var_value = 0
    for i in args:
        var_value += 1
        print(f"Argument number {var_value} is: {i}")

# *args returns a tuple
op_test("Red", "Blue", "Green", "Yellow")

# How is *kwargs used?
# Kw - args
# Keyword - arguments
# Using the keys() method
def op_keys(**kwargs):
    var_number = 0
    for var_key in kwargs.keys():
        var_number += 1
        print(f"Key {var_number}: {var_key}.")

op_keys(name="Javier", last_names="Gomez de la barca", age="27")

# Using the values() method
def op_values(**kwargs):
    var_number = 0
    for var_value in kwargs.values():
        var_number += 1
        print(f"Value {var_number}: {var_value}.")

op_values(name="Javier", last_names="Gomez de la barca", age="27")

# Using the items() method
def op_keys_values(**kwargs):
    var_number = 0
    for var_key_value in kwargs.items():
        var_number += 1
        print(f"Item {var_number}: {var_key_value}.")

op_keys_values(name="Javier", last_names="Gomez de la barca", age="27")

# Create dictionaries with dict function
dict(name="Javier", last_names="Gomez de la barca", age="27")

# Dictionaries as argument for **kwargs
def op_print_dictionary(**kwargs):
    for var_item in kwargs.items():
        print(var_item)

dct_user1 = {"name":"Javier", "last_names":"Gomez de la barca", "age":"27"}

op_print_dictionary(**dct_user1)

# *args together with fixed positional parameters
def op_multiply(prm_x, prm_y, *args):
    return(prm_x * prm_y * args[0] * args[1])

print(op_multiply(10, 4, 50, 6))

def op_multiply_10(*args):
    for i in args:
        var_result = i * 10
        print(f"Result: {var_result}")

op_multiply_10(10, 56, 43, 3, 5, 6)

# *args together **kwargs and conventional arguments
def op_information(*args, **kwargs):
    print(args)
    print(kwargs)

op_information(10, 50, 60, **dct_user1)