def safe_float_input(text):
    try:
        data =  float(input(text).strip())
        return data
    except:
        return safe_float_input(text)

height = safe_float_input("enter your height in m: ");
weight = safe_float_input("enter your weight in kg: ");

BMI = round(weight / (height*height))
print(f"Your BMI is {BMI}")
