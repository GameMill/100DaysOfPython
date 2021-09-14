def safe_int_input(text):
    try:
        data =  int(input(text).strip())
        return data
    except:
        return safe_int_input(text)



print("#"*50)
print(" Is Leap Year ".center(50,"#"))
print("#"*50)
print("")

current_year = safe_int_input("What year do you want to check? ")

if(current_year % 4 == 0):
    if(current_year % 100 == 0):
        if(current_year % 400 == 0):
            print("Is a Leap Year")
        else:
            print("Not a leap year")
    else:
        print("Is a leap year")
else:
    print("Not a leap year")
