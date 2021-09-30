import os
root = os.path.dirname(os.path.abspath(__file__)) + "/"

with open(f"{root}/Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
with open(f"{root}/Input/Names/invited_names.txt") as names_file:
    for item in names_file:
        item = item.strip()
        new_letter = letter.replace("[name]",item)
        with open(f"{root}/Output/ReadyToSend/Letter_For_{item}.txt","w") as newfile:
            newfile.write(new_letter)
        