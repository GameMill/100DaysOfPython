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

def safe_size_input(text):
    size = ["l","m","s"]
    try:
        data =  input(text).strip().lower()
        if size.__contains__(data):
            return data
        else:
            return safe_size_input(text)
    except:
        return safe_size_input(text)

print("#"*50)
print(" Order a Pizza ".center(50,"#"))
print("#"*50)
print("")

size = safe_size_input("what size pizza do you want? S, M, or L ")
add_pepperoni = safe_yes_no_input("Do you want pepperoni? Y or N ")
extra_cheese = safe_yes_no_input("Do you want extra cheese? Y or N ")

price = 0

if size == "l":
    price += 25
    if add_pepperoni:
        price += 3
elif size == "m":
    price += 20
    if add_pepperoni:
        price += 3
else:
    price += 15
    if add_pepperoni:
        price += 2

if extra_cheese:
        price += 1

print(f"Your final bill is: £{price}")