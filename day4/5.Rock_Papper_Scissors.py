import  random

def safe_rock_paper_scissors_input(text):
    rock = ["rock","r","0"]
    paper = ["paper","p","1"]
    scissors = ["scissors","s","2"]
    try:
        data =  input(text).strip().lower()
        if rock.__contains__(data):
            return "rock"
        elif paper.__contains__(data):
            return "paper"
        elif scissors.__contains__(data):
            return "scissors"
        else:
            return safe_rock_paper_scissors_input(text)
    except:
        return safe_rock_paper_scissors_input(text)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


ai_input = random.choice(["rock", "paper", "scissors"])
user_input = safe_rock_paper_scissors_input("What do you choose? Rock, Paper, Scissors ")



if user_input == "rock":
    print(f"You choosen rock\n{rock}\n")

    
    if ai_input == "scissors":
        print(f"The computer choose scissors\n{scissors}\n")
        print("You Win!")
    elif ai_input == "rock":
        print(f"The computer choose rock\n{rock}\n")
        print("Draw")
    else:
        print(f"The computer choose paper\n{paper}\n")
        print("You Lose!")

elif user_input == "paper":
    print(f"You choosen paper\n{paper}\n")
    if ai_input == "rock":
        print(f"The computer choose rock\n{rock}\n")
        print("You Win!")
    elif ai_input == "paper":
        print(f"The computer choose paper\n{paper}\n")
        print("Draw")
    else:
        print(f"The computer choose scissors\n{scissors}\n")
        print("You Lose!")
    
elif user_input == "scissors":
    print(f"You choosen scissors\n{scissors}\n")
    if ai_input == "paper":
        print(f"The computer choose paper\n{paper}\n")
        print("You Win!")
    elif ai_input == "scissors":
        print(f"The computer choose scissors\n{scissors}\n")
        print("Draw")
    else:
        print(f"The computer choose rock\n{rock}\n")
        print("You Lose!")
    