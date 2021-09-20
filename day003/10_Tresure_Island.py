def safe_yes_no_input(text):
    yes = ["yes","y"]
    no = ["no","n"]
    try:
        data =  input(text).strip().lower()
        if yes.__contains__(data):
            return "yes"
        elif no.__contains__(data):
            return "no"
        else:
            return safe_yes_no_input(text)
    except:
        return safe_yes_no_input(text)

def safe_treasure_love_input(text):
    treasure = ["treasure","t"]
    love = ["love","l"]
    try:
        data = input(text).strip().lower()
        if treasure.__contains__(data):
            return "treasure"
        elif love.__contains__(data):
            return "love"
        else:
            return safe_treasure_love_input(text)
    except:
        return safe_treasure_love_input(text)

def safe_left_straight_right_input(text):
    left = ["left","l"]
    right = ["right","r"]
    straight = ["straight","s"]
    try:
        data =  input(text).strip().lower()
        if left.__contains__(data):
            return "left"
        elif right.__contains__(data):
            return "right"
        elif straight.__contains__(data):
            return "straight"
        else:
            return safe_left_straight_right_input(text)
    except:
        return safe_left_straight_right_input(text)

def game_over(text):
    print("")
    print(text)
    print("#"*50)
    print("       Game Over       ".center(50,"#"))
    print(" Better Luck Next Time ".center(50,"#"))
    print("#"*50)
    exit()

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************

Welcome to Treasure Island.
Your mission is to find the treasure.

You wash up after a bad stomy and there a treasure map on the floor in front of you
-----------------------
|  X         #        |
|  |                  |
|  |      #           |
|[] -------()  #      |
|  ()     |       #   |
|   #  #  |           |
|       ()^()      #  |
-----------------------''')

Which_way = safe_left_straight_right_input("Which way do you what to go? Left, Straight, Right ")

if(Which_way != "straight"):
    game_over("You get eaten by a crab. You lose")

print("")


print("""
Your Treasure Map
-----------------------
|  X         #        |
|  |                  |
|  |      #           |
|[] ------^()  #      |
|   #     |       #   |
|   #  #  |           |
|       () ()      #  |
-----------------------
""")
Which_way = safe_left_straight_right_input("You arrive at a tree. Which way do you what to go? Left, Straight, Right ")
    

if Which_way != "left":
    game_over("You have fell into a hole. You lose")
print("""
Your Treasure Map
-----------------------
|  X         #        |
|  |                  |
|  |      #           |
|[]<-------()  #      |
|  ()     |       #   |
|   #  #  |           |
|       () ()      #  |
-----------------------
""")

Which_way = safe_left_straight_right_input("You arrive at a House. Which way do you what to go? Left, Straight, Right ")


if(Which_way == "straight"):
    choice = safe_treasure_love_input("there a woman inside the house. she ask you what your looking for? Treasure, Love ")
    if choice == "treasure":
        print("")
        print("She laughs at you and tell you that the map your holding was drawn by heir.")
        print("she asks \"you can you help heir with some work.\" you reply \"yes\" and she says.")
        print("the true treasure is your heart")
        print("")
        print("#"*50)
        print(" You WIN ".center(50,"#"))
        print("#"*50)
        exit()
    elif choice == "love":
        game_over("She attacks you. you run for your live but she is faster then you. she kills you.")

if Which_way != "right":
    game_over("You have fell into a hole. You lose")


print("""
Your Treasure Map
-----------------------
|  X         #        |
|  ^                  |
|  |      #           |
|[] -------()  #      |
|  ()     |       #   |
|   #  #  |           |
|       () ()      #  |
-----------------------
""")

print("you have found a big X on the floor. You start digging. \n")
print("2 Years Later")
game_over("You did not find anything. The map was fake")