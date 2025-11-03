# Structure of a decorative function
def a(b):
    def c():
        # Function code C
        b() # Call the parameter function
        # Code after the call
    return c

# Building a decorative function
# concurrent message a and concurrent message b

def op_decorative_function(prm_function_b):
    def op_function_c():
        print(f"The result of the operation is:")
        prm_function_b()
        print("Operation carried out successfully")
    return op_function_c

# Call a decorator function
@op_decorative_function
def op_sum():
    print(10 + 10)

# Call a decorator function
@op_decorative_function
def op_subtrac():
    print(10 - 20)

# Call a decorator function
@op_decorative_function
def op_multiply():
    print(45 * 2)

# Call a decorator function
@op_decorative_function
def op_divide():
    print(4 / 87)

op_sum()
op_subtrac()
op_multiply()
op_divide()

