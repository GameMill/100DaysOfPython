
import math


def safe_float_input(text):
    try:
        data =  float(input(text).strip())
        return data
    except:
        return safe_float_input(text)

def calc_area(width,height,cover=5):
    return math.ceil((width*height)/cover)

width = safe_float_input("Please enter the width of the wall: ")
height = safe_float_input("Please enter the height of the wall: ")

number_of_cans =  calc_area(width,height)


print(f"You will need {number_of_cans:} cans of paint")