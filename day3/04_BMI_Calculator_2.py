def safe_float_input(text):
    try:
        data =  float(input(text).strip())
        return data
    except:
        return safe_float_input(text)

print("#"*50)
print(" BMI Caculator ".center(50,"#"))
print("#"*50)
print("")

height = safe_float_input("Enter your height in m: ");
weight = safe_float_input("Enter your weight in kg: ");

BMI = weight / (height*height)
print(f"Your BMI is {BMI:.2f}")

if BMI < 18.5:
    print("You are underweight")
elif BMI >= 18.5 and BMI < 25:
    print("You are normal weight")
elif BMI >= 25 and BMI < 30:
    print("You are overweight")
else:
    print("You are clinically obese")
