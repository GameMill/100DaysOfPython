def safe_input_with_length(text,lenght):
    try:
        data =  str(int(input(text).strip()))
        if(len(data) != 2):
            return safe_input_with_length(text,lenght)
        return data
    except:
        print("Invalid input")
        return safe_input_with_length(text,lenght)

two_number = safe_input_with_length("Please type a 2 digit number: ",2)

number_1 = int(two_number[0])
number_2 = int(two_number[1])

print(f"{number_1} + {number_2} = {number_1+number_2}")
