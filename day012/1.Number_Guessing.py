import os
import random
def title(project_name):
    """Generate the program title and print to console"""
    os.system("cls||clear") 
    n = 50
    if(len(project_name) > 48):
        n = 100
    print("#"*n)
    print(f" {project_name} ".center(n,"#"))
    print("#"*n)
    print("")

def safe_easy_hard_input(text):
    """check the user has inputed yes or y for yes and no or n for no and returns 'yes' or 'no' Prevents invalid input"""

    try:
        easy = ["easy","e"]
        hard = ["hard","h"]
        data =  input(text).strip().lower()
        if easy.__contains__(data):
            return "easy"
        elif hard.__contains__(data):
            return "hard"
        else:
            return safe_easy_hard_input(text)
    except:
        return safe_easy_hard_input(text)

def safe_int_input(text):
    """turn the user input into an int. Prevents invalid input"""
    try:
        data =  int(input(text).strip())
        return data
    except:
        return safe_int_input(text)


def Guess(Number,lives): 
    """Ask the user to guess the number. return true if the user guess correct. return false if out of lives"""
    user_guess = safe_int_input("Make a guess: ")
    if user_guess == Number: # The user guess correct
        return True
    else:
        lives -= 1
        if lives == 0:
            return False
        else:
            print("Lives remaining: {lives}")
            if user_guess > Number: # The user guess was too hign
                print("Too hign.")
                return Guess(Number,lives)
            else: # The user guess was too low
                print("Too low.")
                return Guess(Number,lives)

   
title("Number Guessing Game!")
if safe_easy_hard_input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
    lives = 10
else:
    lives = 5

print("I`m thinking of a number between 1 and 100")
number = random.randint(1,100)
if Guess(number,lives):
    print(f"You guess correct. the number was {number}")
else:
    print(f"Sorry. my number was {number}")