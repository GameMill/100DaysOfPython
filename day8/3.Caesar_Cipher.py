import os
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ABC = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def safe_int_input_min_max(text,min,max):
    try:
        data =  int(input(text).strip())
        if data >= min and data <= max:
            return data
        else:
            return safe_int_input_min_max(text,min,max)
    except:
        return safe_int_input_min_max(text,min,max)

def safe_int_input(text):
    try:
        data =  int(input(text).strip())
        return data
    except:
        return safe_int_input(text)

def safe_input(text): # Prevents empty string
    try:
        data = input(text).strip()
        if(data != ""):
            return data
        return safe_input(text)
    except:
        return safe_input(text)

def title(project_name):
    os.system("cls||clear") 
    n = 50
    if(len(project_name) > 48):
        n = 100
    print("#"*n)
    print(f" {project_name} ".center(n,"#"))
    print("#"*n)
    print("")

def safe_yes_no_input(text):
    try:
        yes = ["yes","y"]
        no = ["no","n"]
        data =  input(text).strip().lower()
        if yes.__contains__(data):
            return "yes"
        elif no.__contains__(data):
            return "no"
        else:
            return safe_yes_no_input(text)
    except:
        return safe_yes_no_input(text)

def caesar(string,offset,direction=1): # direction=1 for encode and direction=2 for decode
    new_string = ""
    if direction == 2:
        offset = 0-offset
    for letter in string:
        if abc.__contains__(letter):
            new_string += abc[(abc.index(letter) + offset) % len(abc)]
        elif ABC.__contains__(letter):
            new_string += ABC[(ABC.index(letter) + offset) % len(ABC)]
        else:
            new_string += letter
    return new_string


def caesar_main(): 
    title("Caesar Cipher")

    option = safe_int_input_min_max("Please select an option.\n\n 1. Encode\n 2. Decode\n\nPlease enter the number here: ",1,2)

    offset = safe_int_input("Please enter an offset here: ")
    word = input("Please enter your string: ").strip()
    encode_word = caesar(word,offset,option)

    print("Decoded Message:")
    print(word)
    print(f"\n\nEncoded Message Using offset of {offset}:")
    print(encode_word)

    answer = safe_yes_no_input("\n\nenter 'Yes' if you what to go again. Otherwise type 'no': ")
    if answer == "yes":
        caesar_main()

caesar_main()