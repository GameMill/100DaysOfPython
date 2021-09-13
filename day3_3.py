def safe_int_input(text):
    try:
        data =  int(input(text).strip())
        return data
    except:
        return safe_int_input(text)

your_age = safe_int_input("how old are you: ");

year_remaning = 90 - your_age

if(year_remaning < 0):
    year_remaning = 0

print(f"you have {year_remaning*365} days, {year_remaning*52} weeks and {year_remaning*12} months left.")
