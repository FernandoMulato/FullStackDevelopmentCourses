# Functions
# Declare functions
def op_greet():
    var_name = input("Enter your name, please\n")
    print(f"Hey {var_name}, what's going on?\n")

# Call functions
op_greet();

# Parameters
def op_greet(prm_name, prm_age):
    print(f"Hey {prm_name}, what's going on?\n")
    print(f"You are {prm_age} years old.\n")

op_greet("Fernando", 18);

# return on the functions
def op_sum(prm_num1, prm_num2):
    return prm_num1 + prm_num2

var_result = op_sum(10, 50);

print(f"The result of the sum is: {var_result}")