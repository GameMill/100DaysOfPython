import  os
def title(project_name):
    os.system("cls||clear") 
    n = 50
    if(len(project_name) > 48):
        n = 100
    print("#"*n)
    print(f" {project_name} ".center(n,"#"))
    print("#"*n)
    print("")


def safe_input(text): # Prevents empty string
    try:
        data = input(text).strip()
        if(data != ""):
            return data
        return safe_input(text)
    except:
        return safe_input(text)

def safe_float_input(text):
    try:
        data =  float(input(text).strip())
        return data
    except:
        return safe_float_input(text)

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

