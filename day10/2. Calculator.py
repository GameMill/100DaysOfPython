def safe_float_input(text):
    """turn the user input into an float. Prevents invalid input"""
    try:
        data =  float(input(text).strip())
        return data
    except:
        return safe_float_input(text)


def safe_operations_input(text):
    """check the user has inputed an operations ["*","-","+","/"]. Prevents invalid input"""

    try:
        operations = ["*","-","+","/"]
        data =  input(text).strip()
        if operations.__contains__(data):
            return data
        else:
            return safe_operations_input(text)
    except:
        return safe_operations_input(text)


def safe_yes_no_input(text):
    """check the user has inputed yes or y for yes and no or n for no and returns 'yes' or 'no' Prevents invalid input"""

    try:
        yes = ["yes","y"]
        no = ["no","n"]
        data =  input(text).strip().lower()
        if yes.__contains__(data):
            return "yes"
        elif no.__contains__(data):
            return "no"
        else:
            return safe_yes_no_input(text)
    except:
        return safe_yes_no_input(text)


logo = """
 _____________________
|  _________________  |
| | Christopher  0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)



def action(number):
    """Basic Calculator for * + - / operations"""
    operations = safe_operations_input("Pick an operation: ")
    next_number = safe_float_input("What the next number?: ")
    new_number = 0
    if operations == "*":
        new_number = number * next_number
        print(f"{number} * {next_number} = {new_number}")

    elif operations == "+":
        new_number = number + next_number
        print(f"{number} + {next_number} = {new_number}")

    elif operations == "-":
        new_number = number - next_number
        print(f"{number} - {next_number} = {new_number}")
    elif operations == "/":
        new_number = number / next_number
        print(f"{number} / {next_number} = {new_number}")

    if safe_yes_no_input(f"Type 'y' to continue caculating with {new_number}, or type 'n' to stop caculating ") == "yes":
        return action(new_number)
    else:
        return new_number

    
number = action(safe_float_input("What`s the first number? "))

print(f"The Final Number is: {number}")
    