import tkinter
from tkinter.constants import COMMAND
import tkinter.messagebox 
import os
import random
import json

#-----------------------# Start of Constants block #-----------------------#
ROOT = os.path.dirname(os.path.abspath(__file__)) + "/"
FROM_LANG = "Japanese" 
TO_LANG = "English"
HEADER_FONT = ("Arial",40,"italic")
WORD_FONT = ("Arial",60,"bold")
BACKGROUND_COLOR = "#B1DDC6"
GUESS_TIME_S = 3
#-----------------------# End of Constants block #-----------------------#

#-----------------------# Start of Variables block #-----------------------#

current_word_index = -1

#-----------------------# End of Variables block #-----------------------#



#-----------------------# Start of Database Block #-----------------------#

database = None
def Load_Lang():
    """Replace pandas with custom implmention to allow japanese characters """
    global database

    try:
        with open(f"{ROOT}data/{FROM_LANG}_To_Learn.json") as database_file:
            database = json.load(database_file)
            print(database)
    except:
        database = {}
        try:
            header_row = None
            import data.Japanese_words as raw_data
            for line in raw_data.Data.split("\n"):
                if(header_row == None):
                    header_row = line.split(",")
                    for header in header_row:
                        database[header.strip()] = []
                else:
                    value_row = line.split(",")
                    for i in  range(len(header_row)):
                        value = value_row[i].strip()
                        try:
                            a = int(value)
                            value = a
                        except:
                            pass
                        database[header_row[i].strip()].insert(i,value)

        except print(0):
            tkinter.messagebox.showerror(title="Error",message=f"Failed to load {FROM_LANG} Database")
            exit()

Load_Lang()

#-----------------------# End of Database Block #-----------------------#


#-----------------------# Start of Function block #-----------------------#
timer = None
def select_word():
    global current_word_index
    global timer
    if(timer != None):
        tk.after_cancel(timer)

    current_word_index = random.randint(0,len(database["Count"])-1)
    display_word(FROM_LANG)
    timer = flash_card.after(GUESS_TIME_S*1000,flip)



def display_word(lang):
    flash_card.itemconfigure(header_text,text=lang,fill=text_color(lang != TO_LANG))
    flash_card.itemconfigure(word_text,text=database[lang][current_word_index],fill=text_color(lang != TO_LANG))
    flash_card.itemconfigure(canvas_image,image=background_type(lang != TO_LANG))

def flip():
    global timer
    timer = None
    display_word(TO_LANG)


def background_type(Is_front):
    if Is_front:
        return card_front
    else:
        return card_back

def text_color(Is_front):
    if Is_front:
        return "black"
    else:
        return "white"

def save():
    with open(f"{ROOT}data/{FROM_LANG}_To_Learn.json", mode="w") as database_file:
        json.dump(database,database_file)


def correct():
    database[FROM_LANG].pop(current_word_index)
    database[TO_LANG].pop(current_word_index)
    database["Count"].pop(current_word_index)
    save()
    select_word()
    
    
#-----------------------# Start of UI block #-----------------------#

tk = tkinter.Tk()
tk.title("Japanese to English flash cards")
tk.config(padx=50,pady=50,bg=BACKGROUND_COLOR)




    

card_front = tkinter.PhotoImage(file=f"{ROOT}images/card_front.png")
card_back = tkinter.PhotoImage(file=f"{ROOT}images/card_back.png")

flash_card = tkinter.Canvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas_image = flash_card.create_image(400,263,image=card_front)
header_text = flash_card.create_text(400,150,text=FROM_LANG,font=HEADER_FONT)
word_text = flash_card.create_text(400,263,text="Loading",font=WORD_FONT)
flash_card.grid(columnspan=2,column=0,row=0)

#flash_card.itemconfigure(canvas_image,image=card_front)


select_word()



wrong_image = tkinter.PhotoImage(file=f"{ROOT}images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=select_word)
wrong_button.grid(column=0,row=1)

right_image = tkinter.PhotoImage(file=f"{ROOT}images/right.png")
right_button = tkinter.Button(image=right_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=correct)
right_button.grid(column=1,row=1)


tk.mainloop()
#-----------------------# End of UI block  #-----------------------#
