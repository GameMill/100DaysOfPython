

def safe_int_input(text):
    try:
        data =  int(input(text).strip())
        return data
    except:
        return safe_int_input(text)



print("#"*50)
print(" Ride the Rollercoaster ".center(50,"#"))
print("#"*50)
print("")

size = safe_int_input("What is your height in cm? ")

if size >= 120:
    print("You can ride the rollercoaster\n")

    age = safe_int_input("What is your age in years? ")
    if age > 18:
        print("Your Ticket will cost £12")
    elif age > 12:
        print("Your Ticket will cost £7")
    else:
        print("Your Ticket will cost £5")
else:
    print("Sorry, you have to grow taller before you can ride.")


