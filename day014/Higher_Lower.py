import random
import os
import art
import game_data


def print_line(args,Name):
    print(f"Compare {Name}: {args['name']}, a {args['description']}, from {args['country']}.")
    

def safe_a_b_input(text):
    """check the user has inputed yes or y for yes and no or n for no and returns 'yes' or 'no' Prevents invalid input"""

    try:
        a = ["a"]
        b = ["b"]
        data =  input(text).strip().lower()
        if a.__contains__(data):
            return "a"
        elif b.__contains__(data):
            return "b"
        else:
            return safe_a_b_input(text)
    except:
        return safe_a_b_input(text)

def Guess(A,B):
    

    print_line(A,"A")
    print(art.vs)
    print_line(B,"B")
    choice = safe_a_b_input("Who has more followers? Type 'A' or 'B': ")
    if A["follower_count"] > B["follower_count"]:
        if choice == "a":
            return True
        else:
            return False
    else:
        if choice == "a":
            return False
        else:
            return True
            
        

def get_b(A):
    B = random.choice(game_data.data)
    if A == B:
        return get_b(A)
    else:
        return B
        
score = 0
A = random.choice(game_data.data)

os.system("cls||clear")
print(art.logo)

while(Guess(A,get_b(A))):
    os.system("cls||clear")
    score += 1
    print(art.logo)
    print(f"You're right! Current score: {score}.")
    pass

os.system("cls||clear")
print(art.logo)

print(f"Sorry, that's wrong. Final score: {score}")