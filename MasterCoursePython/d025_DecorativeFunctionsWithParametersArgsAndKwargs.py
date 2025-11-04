"""
def op_decorative_function(prm_function_b):
    def op_function_c(prm_a, prm_b):
        print(f"The result of the operation is:")
        prm_function_b(prm_a, prm_b)
        print("Operation carried out successfully")
    return op_function_c

# Call a decorator function
@op_decorative_function
def op_sum(prm_num1, prm_num2):
    print(prm_num1 + prm_num2)

# Call a decorator function
@op_decorative_function
def op_subtrac(prm_num1, prm_num2):
    print(prm_num1 - prm_num2)

# Call a decorator function
@op_decorative_function
def op_multiply(prm_num1, prm_num2):
    print(prm_num1 * prm_num2)

# Call a decorator function
@op_decorative_function
def op_divide(prm_num1, prm_num2):
    print(prm_num1 / prm_num2)

op_sum(10, 25)
op_subtrac(20, 40)
op_multiply(5, 80)
op_divide(20, 400)

# The use of *args in decorated functions
def op_decorative_function2(prm_function_b):
    def op_function_c(*args):
        print(f"The result of the operation is:")
        prm_function_b(*args)
        print("Operation carried out successfully")
    return op_function_c

# Call a decorator function
@op_decorative_function2
def op_subtrac2(prm_num1, prm_num2, prm_num3, prm_num4):
    print(prm_num1 - prm_num2 - prm_num3 - prm_num4)

op_subtrac2(10 , 25, 50, 14)
"""

# The use of *kwargs in decorated functions
import math 

def op_decorative_function3(prm_function_b):
    def op_function_c(*args, **kwargs):
        print(f"The result of the operation is:")
        prm_function_b(*args, **kwargs)
        print("Operation carried out successfully")
    return op_function_c

@op_decorative_function3
def op_area_rectangle(prm_base, prm_height):
    print(f"The area of the rectangle is: {prm_base * prm_height}.")

@op_decorative_function3
def op_area_triangle(prm_base, prm_height):
    print(f"The area of the triangle is: {prm_base * prm_height / 2}.")

@op_decorative_function3
def op_area_circle(prm_radius):
    print(f"The area of the triangle is: {math.pi * prm_radius ** 2}.")

op_area_rectangle(prm_height=40, prm_base=10)