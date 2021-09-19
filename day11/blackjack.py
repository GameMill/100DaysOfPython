from math import fabs
import random

def safe_int_input_min_max(text,min,max):
    """turn the user input into an int and check that is between the min and max values. Prevents invalid input"""
    try:
        data =  int(input(text).strip())
        if data >= min and data <= max:
            return data
        else:
            return safe_int_input_min_max(text,min,max)
    except:
        return safe_int_input_min_max(text,min,max)


def safe_stick_twist_input(text):
    """check the user has inputed yes or y for yes and no or n for no and returns 'yes' or 'no' Prevents invalid input"""

    try:
        stick = ["stick","s"]
        twist = ["twist","t"]
        data =  input(text).strip().lower()
        if stick.__contains__(data):
            return "stick"
        elif twist.__contains__(data):
            return "twist"
        else:
            return safe_stick_twist_input(text)
    except:
        return safe_stick_twist_input(text)

deck = []
card_suits = ["clubs", "spades", "hearts", "diamonds"]
players_cards = []
dealer_cards = []
player_bust = False
dealer_bust = False

def get_card_value(card_number,bust):
    """Get the card value. Ace card has the ability to be 11 or 1"""
    if card_number == 1:
        if bust:
            return 1
        else:
            return 11
    elif card_number > 10:
        return 10
    else:
        return card_number
        
def get_card_name(card_number):
    """get the name of the card"""
    if card_number == 1:
        return "Ace"
    elif card_number == 13:
        return "King"
    elif card_number == 12:
        return "Queen"
    elif card_number == 11:
        return "Jack"
    else:
        return card_number
        

def reset_deck():
    """Reset the deck and shuffle the deck"""
    global deck
    deck = []
    for suit in card_suits:
        for number in range(1,14):
            deck.append({"Name":get_card_name(number),"Card Number":number,"Suit":suit})
    random.shuffle(deck)

def deal_card():
    global deck
    card = deck.pop()
    return card

def deal_starting_cards():
    global players_cards
    global dealer_cards
    players_cards = [deal_card(),deal_card()]
    dealer_cards = [deal_card(),deal_card()]

def user_turn():
    global players_cards
    global player_bust
    print("")
    print("Your cards are")
    for item in players_cards:
        print(f"{item['Name']} of {item['Suit']}")

    if get_total(players_cards,True) > 21:
        return game_over()
    print("")
    if safe_stick_twist_input("Stick or twist: ") == "twist":
        players_cards.append(deal_card())
        if get_total(players_cards,False) > 21:
            player_bust = True
        user_turn()
    print("")
    dealer_turn()
def game_over():
    print("You Lose!")
    exit()

def you_win():
    print("You Win!")
    exit()

def get_total(cards,bust):
    total = 0
    for item in cards:
        total += get_card_value(item["Card Number"],bust)
    return total
    
def dealer_turn():
    print("")
    
    global dealer_cards
    global dealer_bust
    print("the dealer flip the cards")
    print("the card are")
    for item in dealer_cards:
        print(f"{item['Name']} of {item['Suit']}")

    if get_total(dealer_cards,True) > 21:
        return you_win()
    elif get_total(dealer_cards,True) < 15:
        dealer_cards.append(deal_card())
        dealer_bust = 21 < get_total(dealer_cards,False)
        
        dealer_turn()
    else:
        if get_total(dealer_cards,dealer_bust) > 21:
            you_win()
        else:
            if get_total(dealer_cards,dealer_bust) > get_total(players_cards,player_bust):
                game_over()
            else:
                you_win()
        
    
        
        
    
reset_deck()

print("Welcome to blackjack")
print("")
print("The dealer is drawing the cards")
deal_starting_cards()


user_turn()