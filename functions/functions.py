import os
def title(project_name):
    """Generate the program title and print to console"""
    os.system("cls||clear") 
    n = 50
    if(len(project_name) > 48):
        n = 100
    print("#"*n)
    print(f" {project_name} ".center(n,"#"))
    print("#"*n)
    print("")


def safe_input(text):
    """Prevents an empty string and removes any whitespaces at the start or end"""
    try:
        data = input(text).strip()
        if(data != ""):
            return data
        return safe_input(text)
    except:
        return safe_input(text)

def safe_float_input(text):
    """turn the user input into an float. Prevents invalid input"""
    try:
        data =  float(input(text).strip())
        return data
    except:
        return safe_float_input(text)

def safe_int_input(text):
    """turn the user input into an int. Prevents invalid input"""
    try:
        data =  int(input(text).strip())
        return data
    except:
        return safe_int_input(text)


def safe_int_input_min_max(text,min,max):
    """turn the user input into an int and check that is between the min and max values. Prevents invalid input"""
    try:
        data =  int(input(text).strip())
        if data >= min and data <= max:
            return data
        else:
            return safe_int_input_min_max(text,min,max)
    except:
        return safe_int_input_min_max(text,min,max)


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