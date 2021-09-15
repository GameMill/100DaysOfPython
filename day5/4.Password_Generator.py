import random

def safe_int_input(text):
    try:
        data =  int(input(text).strip())
        return data
    except:
        return safe_int_input(text)


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("#"*50)
print(" Password Generator ".center(50,"#"))
print("#"*50)
print()
number_of_letters = safe_int_input("How many letters would you like in your password? ")
number_of_numbers = safe_int_input("How many numbers would you like in your password? ")
number_of_symbols = safe_int_input("How many numbers Symbols you like in your password? ")

all_char = []
for item in range(number_of_letters):
    all_char.append(random.choice(letters))
for item in range(number_of_numbers):
    all_char.append(random.choice(numbers))
for item in range(number_of_symbols):
    all_char.append(random.choice(symbols))

random.shuffle(all_char)

password = ""
for item in range(len(all_char)):
    i = random.randint(0,len(all_char)-1);
    password += all_char[i]
    all_char.pop(i)
print(f"Your password is {password}")