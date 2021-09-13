import os

def safe_int_input(text):
    try:
        data =  int(input(text).strip())
        return data
    except:
        return safe_int_input(text)

def safe_float_input(text):
    try:
        data =  float(input(text).strip())
        return data
    except:
        return safe_int_input(text)


def clear_screen():
    os.system("cls||clear")

print("#"*50)
print(" Tip Calculator ".center(50,"#"));
print("#"*50)
print("")

total_bill = safe_float_input("What was the total bill? £");  

precentage_tip = 1 + (safe_int_input("How much tip would you like to give? 10, 12, or 15? ") / 100)

total_bill_with_tip = total_bill * precentage_tip

number_of_people = safe_int_input("How many people to split the bill? ")
each_bill = int((total_bill_with_tip / number_of_people) * 100) / 100



print(f"Eath person should pay: £{each_bill}")

