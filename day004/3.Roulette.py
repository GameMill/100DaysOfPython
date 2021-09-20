import random

def safe_input(text):
    try:
        data = input(text).strip()
        if data == "":
            return safe_input(text)
        return data
    except:
        return safe_input(text)
    

players = ["Abgela","Ben","Jenny","Michael","Chloe"]

your_name = safe_input("Please enter your name: ").lower().capitalize()

players.append(your_name)

chosen_player = random.choice(players)

print(f"Chosen player is: {chosen_player}")