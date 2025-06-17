# Lambda functions(anonymous): are short functions, which have a very reduced syntax

# Differences of normal functions and lambda functions
def op_multiplication(prm_number_1, prm_number_2):
    return prm_number_1 * prm_number_2

var_multiplication = lambda prm_number_1, prm_number_2 : prm_number_1 * prm_number_2

var_result = var_multiplication(10,7)
print(var_result)

# Or
(lambda prm_number_1, prm_number_2 : print(prm_number_1 * prm_number_2)) (7,5)