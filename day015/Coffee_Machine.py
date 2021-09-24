import os
import time

def safe_int_input(text):
    """turn the user input into an int. Prevents invalid input"""
    try:
        data =  int(input(text).strip())
        return data
    except:
        return safe_int_input(text)


def safe_dynamic_input(text,option_list):
    """check the user has inputed [["yes","y"],["no","n"]] for yes and no or n for no and returns 'yes' or 'no' Prevents invalid input"""

    try:
        data =  input(text).strip().lower()
        for item in option_list:
            if item.__contains__(data):
                return item[0]
        return safe_dynamic_input(text,option_list)
    except:
        return safe_dynamic_input(text,option_list)

Supplys = {
    "Water":300,
    "Milk":200,
    "Coffee":100,
    "Money":0
}

drinks ={
    "espresso":{"Water":50,"Milk":0,"Coffee":18},
    "latte":{"Water":200,"Milk":150,"Coffee":24},
    "cappuccion":{"Water":250,"Milk":100,"Coffee":24},
}

logo = """
        /~~~~~~~~~~~~~~~~~~~/|
       /              /######/ / |
      /              /______/ /  |
     ========================= /||
     |_______________________|/ ||
      |  \****/     \__,,__/    ||
      |===\**/       __,,__     ||
      |______________\====/%____||
      |   ___        /~~~~\ %  / |
     _|  |===|===   /      \%_/  |
    | |  |###|     |########| | /
    |____\###/______\######/__|/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to the coffee machine
"""

caffee = '''
                        (
                          )     (
                   ___...(-------)-....___
               .-""       )    (          ""-.
         .-'``'|-._             )         _.-|
        /  .--.|   `""---...........---""`   |
       /  /    |                             |
       |  |    |                             |
        \  \   |                             |
         `\ `\ |                             |
           `\ `|                             |
           _/ /\                             /
          (__/  \                           /
       _..---""` \                         /`""---.._
    .-'           \                       /          '-.
   :               `-.__             __.-'              :
   :                  ) ""---...---"" (                 :
    '._               `"--...___...--"`              _.'
      \""--..__                              __..--""/
       '._     """----.....______.....----"""     _.'
          `""--..,,_____            _____,,..--""`
                        `"""----"""`

'''
def has_supply(Water,Coffee,Milk):
    if Supplys["Coffee"] <= Coffee:
        return False
    if Supplys["Milk"] <= Milk:
        return False
    if Supplys["Water"] <= Water:
        return False
    return True
    
def supplys_low():
    if Supplys["Coffee"] < 30:
        print("Coffee Low")
    if Supplys["Milk"] < 150:
        print("Milk Low")
    if Supplys["Water"] < 250:
        print("Water Low")

def get_money():
    money = safe_int_input("How many quarters?: ")*0.25
    money += safe_int_input("How many dimes?: ")*0.10
    money += safe_int_input("How many nickles?: ")*0.05
    money += safe_int_input("How many pennies?: ")*0.01
    return money
    

def make_drink(name,Water,Coffee,Milk,Money):
    global Supplys
    cost = 0
    if(name == "espresso"):
        cost = 1.50
    elif(name == "latte"):
        cost = 2.50
    elif(name == "cappuccion"):
        cost = 3.00
    if Money < cost:
        print("Sorry that`s not enough money. Money refunded.")
        time.sleep(5)
        return
    print(f"Here is £{(Money-cost):0.2f} in change.")
    Supplys["Water"] -= Water
    Supplys["Coffee"] -= Coffee
    Supplys["Milk"] -= Milk
    Supplys["Money"] += Money
    print(f"Making your {name}. Please Wait...")
    time.sleep(10)
    print(caffee)
    print(f"Please enjoy your {name}")
    time.sleep(5)

while True:
    os.system("cls||clear")
    print(logo)
    supplys_low()
    drink = safe_dynamic_input("What would you like? (espresso/latte/cappuccion): ",[ ["espresso","e"], ["latte","l"], ["cappuccion","c"],["report","r"],["exit","q"] ])
    if drink == "report":
        print(f"""Water: {Supplys["Water"]}ml
Milk: {Supplys["Milk"]}ml
Coffee: {Supplys["Coffee"]}g
Money: £{Supplys["Money"]:0.2f}
""")
        time.sleep(10)
    elif drink == "exit":
        print("Turning off")
        exit()
    else:
        if has_supply(drinks[drink]["Water"],drinks[drink]["Coffee"],drinks[drink]["Milk"]):
            Money = get_money()
            make_drink(drink,drinks[drink]["Water"],drinks[drink]["Coffee"],drinks[drink]["Milk"],Money)