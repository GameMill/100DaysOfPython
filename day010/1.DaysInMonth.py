def safe_int_input(text):
    try:
        data =  int(input(text).strip())
        return data
    except:
        return safe_int_input(text)

def safe_int_input_min_max(text,min,max):
    try:
        data =  int(input(text).strip())
        if data >= min and data <= max:
            return data
        else:
            return safe_int_input_min_max(text,min,max)
    except:
        return safe_int_input_min_max(text,min,max)



print("#"*50)
print(" days in month ".center(50,"#"))
print("#"*50)
print("")

def is_leap_year(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year,month):
    """Returns the number of days in a given month of the year"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        return 29
    else:
        if month < 13:
            return month_days[month-1]
        else:
            return 0

            

year = safe_int_input("Enter a year: ")
month = safe_int_input_min_max("Enter a month: ",1,12)
days = days_in_month(year, month)
print(days)
