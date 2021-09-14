def safe_int_input(text):
    try:
        data =  int(input(text).strip())
        return data
    except:
        return safe_int_input(text)

print("#"*50)
print(" Odd or Even ".center(50,"#"))
print("#"*50)
print("")
number = safe_int_input("Which number do you want to check? ")
if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")