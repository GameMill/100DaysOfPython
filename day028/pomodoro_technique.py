import tkinter
import os
from tkinter import font
from typing import Text
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_TIMER = ("Courier",35,"bold")
FONT_HEADER = ("Courier",45,"bold")
FONT_BUTTON = ("Arial",12,"bold")
FONT_CHECKMARK = ("Arial",22,"bold")
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 30 * 60
ROOT = os.path.dirname(os.path.abspath(__file__)) + "/"


# ---------------------------- TIMER RESET ------------------------------- # 
Running = False
def Reset_button_clicked():
    global Running
    Running = False
    label1.config(text=" Timer ")
    background.itemconfig(timer_text,text="00:00")
    label2.config(text="✔✔✔✔")
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def Start_button_clicked():
    global Running
    Running = True

    label1.config(text="Working")
    label2.config(text="")
    
    count_down(WORK_MIN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count,num=0,working=True):
    if(Running == False):
        return
    sec = int(count % 60)
    min = int((count - sec)/60)

    if(sec < 10):
        sec = f"0{sec}"
    if(min < 10):
        min = f"0{min}"
        
    background.itemconfig(timer_text,text=f"{min}:{sec}")
    if(count > 0):
        window.after(1000,count_down,count-1,num,working)
    else:
        time_up(num,working)


def raise_above_all():
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)

def time_up(num,working):
    raise_above_all()
    if(working): 
        if(num < 3):
            
            label1.config(text=" Brake ",fg=PINK)
            count_down(SHORT_BREAK_MIN,num,False)
        else:
            label1.config(text=" Brake ",fg=RED)
            count_down(LONG_BREAK_MIN,num,False)

    else:
        num = (num % 3) + 1
        label1.config(text="Working",fg=YELLOW)
        label2.config(text="✔"*num)
        count_down(WORK_MIN,num,True)

# ---------------------------- UI SETUP ------------------------------- #




window = tkinter.Tk()
window.title("Pomodoro Technique")
window.config(padx=100,pady=50,bg=YELLOW)




label1 = tkinter.Label(text=" Timer ",bg=YELLOW,fg=GREEN ,font=FONT_HEADER)
label1.grid(column=1,row=0)


bg_image = tkinter.PhotoImage(file=f"{ROOT}tomato.png")
background = tkinter.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
background.create_image(100,112,image=bg_image)
timer_text = background.create_text(100,132,text="00:00",fill="white",font=FONT_TIMER)
background.grid(column=1,row=1)



start_button = tkinter.Button(text="Start",font=FONT_BUTTON,command=Start_button_clicked)
start_button.grid(column=0,row=2)


reset_button = tkinter.Button(text="Reset",font=FONT_BUTTON,command=Reset_button_clicked)
reset_button.grid(column=2,row=2)


label2 = tkinter.Label(text="✔✔✔✔",bg=YELLOW,fg=GREEN ,font=FONT_CHECKMARK)
label2.grid(column=1,row=3)


window.mainloop()

