# Use of single and double quotes
print('"Azul" is blue in spanish.')

# len() funtion. Allows counting the size of a string
var_menssage = "Yellow"
print(len(var_menssage))

# Access to the positions of a strings
print(var_menssage[0])

# Integer
var_a = 100
var_b = 400

# Sum
var_sum = var_a + var_b
print(var_sum)

# Subtraction
var_subtraction = var_a - var_b
print(var_subtraction)

# Multiplication
var_multiplication = var_a * var_b
print(var_multiplication)

# Division
var_division = var_a / var_b
print(var_division)

# Exponent
var_exponent = 4**2
print(var_exponent)

# Very long number separators
var_number = 420_565_950_950_590_590_905

# Float
var_a = 53.879

# Boolean
var_boolean = True

# type() funtion. Returns the data type of a variable
print(type(var_a))
print(type(var_b))
print(type(var_boolean))

# Conversion of data types 
# Interger to string and len() funtion
var_b = 4521620
var_conversion = str(var_b)
print(len(var_conversion))

# String to Integer
var_a = "10"
var_b = "50"
var_sum = int(var_a) + int(var_b)
print(var_sum)

# String to Float
var_a = "10.56"
var_b = "50.9"
var_sum = float(var_a) + float(var_b)
print(var_sum)

# Truncation of numbers
var_a = 10.56
var_b = 50.9
var_sum = float(var_a) + float(var_b)
print(int(var_sum))

# round numbers with the round() function
var_multiplication = 7.5678 * 6.943534
print(round(var_multiplication, 2))

# Division with floor division. Returns the result of a division
var_division = 10 // 3
print(var_division)

# Module
var_division = 10 % 3
print(var_division)

# Incremental allocation operator
var_a = 10
var_a += 10
print(var_a)

# Decremental allocation operator
var_a = 100
var_a -= 25
print(var_a)

# Formatting strings
var_sum = 90 + 67
print(f"The result of the sum is: {var_sum}") 