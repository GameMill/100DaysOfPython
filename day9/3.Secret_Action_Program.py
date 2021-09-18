import os
def Clear():
    os.system("cls||clear")

def safe_input(text): # Prevents empty string
    try:
        data = input(text).strip()
        if(data != ""):
            return data
        return safe_input(text)
    except:
        return safe_input(text)

def safe_float_input(text):
    try:
        data =  float(input(text).strip())
        return data
    except:
        return safe_float_input(text)

def safe_yes_no_input(text):
    try:
        yes = ["yes","y"]
        no = ["no","n"]
        data =  input(text).strip().lower()
        if yes.__contains__(data):
            return "yes"
        elif no.__contains__(data):
            return "no"
        else:
            return safe_yes_no_input(text)
    except:
        return safe_yes_no_input(text)

art = """
___________ 
\         / 
 )_______( 
 |"""""""|_.-._,.---------.,_.-._ 
 |       | | |               | | ''-.  
 |       |_| |_             _| |_..-' 
 |_______| '-' `'---------'` '-' 
 )"""""""( 
/_________\ 
`'-------'` 
"""

Clear()
print(art)
bids = []

def add_person():
    
    print("Welcome to the secret action program.")
    name = safe_input("What is your name? ")
    bid = safe_float_input("what`s your bid? £")
    bids.append({
        "name":name,
        "bid":bid
    })
     

    if safe_yes_no_input("Are there any other bidders? type 'yes' or 'no'.\n") == "yes":
        Clear() 
        add_person()
    
add_person()
Clear() 

winning_bids = []
current_bid = 0
for item in bids:
    if current_bid < item["bid"]:
        current_bid = item["bid"]
        winning_bids = [item]
    elif current_bid == item["bid"]:
        winning_bids.append(item)
Clear()
if len(winning_bids) == 1:
    print(f"The winning Bidder is {winning_bids[0]['name']} with a bid of £{winning_bids[0]['bid']}")
else:
    print("We have a draw. The winning bidder are ")
    for item in winning_bids:
        print(f"{item['name']} with a bid of £{item['bid']}")
