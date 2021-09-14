
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
