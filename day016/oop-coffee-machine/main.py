from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time
import os

drinks_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()





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
    

    

def make_drink(name,selected_drink):
    if money_machine.make_payment(selected_drink.cost) == False:
        time.sleep(5)
        return
    print(f"Making your {name}. Please Wait...")
    time.sleep(10)
    print(caffee)
    print(f"Please enjoy your {name}")
    time.sleep(5)

while True:
    os.system("cls||clear")
    print(logo)
    types = drinks_menu.get_items()
    list = []
    print(types)
    for item in types.split("/"):
        if(item != ""):
            list.append([item,item[0]])
    list.append(["report","r"])
    list.append(["exit","q"])
    
    drink = safe_dynamic_input(f"What would you like? ({types}): ",list)
    if drink == "report":
        coffee_maker.report()
        money_machine.report()
        time.sleep(10)
    elif drink == "exit":
        print("Turning off")
        exit()
    else:
        selected_drink = drinks_menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(selected_drink):
            make_drink(drink,selected_drink)