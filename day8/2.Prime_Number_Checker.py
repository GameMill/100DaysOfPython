def safe_int_input(text):
    try:
        data =  int(input(text).strip())
        return data
    except:
        return safe_int_input(text)

def is_prime_number(number):
    if number < 2:
        return False
    for item in range(2,number):
        
        if number % item == 0:
            return False
    return True

number = safe_int_input("Please enter a number to check: ");
if is_prime_number(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")