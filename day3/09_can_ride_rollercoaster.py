

def safe_int_input(text):
    try:
        data =  int(input(text).strip())
        return data
    except:
        return safe_int_input(text)

def safe_yes_no_input(text):
    yes = ["yes","y"]
    no = ["no","n"]
    try:
        data =  input(text).strip().lower()
        if yes.__contains__(data):
            return "yes"
        elif no.__contains__(data):
            return "no"
        else:
            return safe_yes_no_input(text)
    except:
        return safe_yes_no_input(text)



print("#"*50)
print(" Ride the Rollercoaster ".center(50,"#"))
print("#"*50)
print("")

size = safe_int_input("What is your height in cm? ")

if size >= 120:
    print("You can ride the rollercoaster\n")
    bill = 0
    age = safe_int_input("What is your age in years? ")
    print("")
    if age >= 45 and age <= 55:
        print(f"Your Ticket is FREE!")
        exit()
    elif age > 18:
        bill = 12
    elif age > 12:
        bill = 7
    else:
        bill = 5
    what_photo = safe_yes_no_input("What a photo? ")
    if what_photo:
        bill += 3
    print(f"Your Ticket will cost £{bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")


