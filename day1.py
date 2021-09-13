import os

def safe_input(text):
    try:
        data = input(text).strip()
        if(data != ""):
            return data
        return safe_input(text)
    except:
        return safe_input(text)

def clear_screen():
    os.system("cls||clear")
        
clear_screen()
print("""Welcome to the Band Name Generator.
What's name of the city you grew up in?""");
city = safe_input("")

print("What's your pet's name?")
pet_name = safe_input("")

print(f"Your band name could be {city} {pet_name}")
