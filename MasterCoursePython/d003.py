# Conditional if, else, else if
var_age = int(input("Insert your age:\n"))

# The variable is left empty
var_response = None

# Is assessed if the user is of legal age. If so, you agree to 
# purchase alcohol
if var_age >= 18:
    print("You are of legal age, you can buy alcohol. Which one do you want? Enter an option number.\n")
    var_response = input("1- Rum.\n2- Whisky.\n3- Gin.\n")
    if var_response == "1":
        print("You have chosen to buy rum.\n")
    elif var_response == "2":
        print("You have chosen to buy whisky.\n")
    elif var_response == "3":
        print("You have chosen to buy gin.\n")
    else:
        print("Option does not validates.\n")
else:
    print("You are a minor, the sale of alcohol to minors is prohibited.\n")

# Logical Ooerator: 
# and
var_color = "Red"
var_shape = "Circle" 
var_size = "Large"
if var_color == "Red" and var_shape == "Circle" and var_size == "Large":
    print("It’s a red circle.\n")
else:
    print("Not satisfy the condition.\n")

# or
if var_color == "Red" or var_shape == "Circle" or var_size == "Small":
    print("The condition is met.\n")
else:
    print("Not satisfy the condition.\n")

# not
if not(var_color == "Blue" and var_response == "Square"):
    print("The condition is met.\n")
else:
    print("Not satisfy the condition.\n")

# Conditional match (switch)
var_error = input("Enter an error code:\n")
match var_error:
    case "200":
        print("All ok.")
    case "301":
        print("Permanent page movement.")
    case "302":
        print("Temporary movement of page")
    case "404":
        print("Page not found.")
    case "500":
        print("Internal server error.")
    case "503":
        print("Service unavailable.")
    case _:
        print("Error not available.")