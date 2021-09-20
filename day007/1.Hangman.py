import random
import os
my_file = open(os.path.dirname(__file__)+"\Words.txt", "r")
word_list = my_file. readlines()
my_file.close()

art = ['''
#====
|   |
|          ()
|         /||\ 
|        | || 
|        |/  \ 
===---===========
|        |      |
''',
'''
#====
|   |
|   o      ()
|         /||\ 
|        | || 
|        |/  \ 
===---===========
|        |      |
''',
'''
#====
|   |
|   o      ()
|         /||\ 
|        | || 
|        |/  \ 
===---===========
|        |      |
''',
'''
#====
|   |
|   o      ()
|   |     /||\ 
|        | || 
|        |/  \ 
===---===========
|        |      |
''',
'''
#====
|   |
|   o      ()
|  /|     /||\ 
|        | || 
|        |/  \ 
===---===========
|        |      |
''',
'''
#====
|   |
|   o      ()
|  /|\    /||\ 
|        | || 
|        |/  \ 
===---===========
|        |      |
''',
'''
#====
|   |
|   o      ()
|  /|\    /||\ 
|   |    | || 
|        |/  \ 
===---===========
|        |      |
''',
'''
#====
|   |
|   o      ()
|  /|\    /||\ 
|   |    | || 
|  /     |/  \ 
===---===========
|        |      |
''',
'''
#====
|   |
|   |       ()
|   o      /||\ 
|  /|\    / ||
|   |    / /  \ 
===/ \==========
|        |     |
''']


def safe_letter_input(text):
    try:
        data = input(text).strip()
        if(data != "" and len(data) == 1):
            return data
        return safe_letter_input(text)
    except:
        return safe_letter_input(text)

chosen_word = random.choice(word_list)
letters_entered = []
word = []
chances = 8
for item in range(len(chosen_word)):
    word.append("_")



def draw():
    os.system("cls||clear")
    print("#"*50)
    print(" Hangman ".center(50,"#"));
    print("#"*50)
    print()
    print(f"Chances Remaning: {chances}\n")

    word_display = ""
    for item in letters_entered:
        word_display += item+" "
    print(f"letter entered: {word_display}\n")

    word_display = ""
    for item in word:
        word_display += item+" "
    print(f"Word: {word_display}")
    print("")
    print(art[8-chances])
    print("")

def ask_user():
    global chances
    global letters_entered
    letter = safe_letter_input("Please enter a letter: ")
    if letters_entered.__contains__(letter):
        draw()
    elif chosen_word.__contains__(letter):
        letters_entered.append(letter)
        i = 0
        for item in chosen_word:
            if letter == item:
                word[i] = letter
            i += 1
    else:
        letters_entered.append(letter)
        chances -= 1

            
        

def has_all_letters():
    for item in word:
        if item == "_":
            return False
    return True

while has_all_letters() == False and chances > 0:
    draw()
    ask_user()

draw()
if chances == 0:
    print()
    print("#"*50)
    print(" You Lose! ".center(50,"#"));
    print("#"*50)
else:
    print()
    print("#"*50)
    print(" You Win! ".center(50,"#"));
    print("#"*50)