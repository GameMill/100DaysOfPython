import tkinter
from tkinter import messagebox

import os
import random
import pyperclip

ROOT = os.path.dirname(os.path.abspath(__file__)) + "/"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
TEXT_FONT = ("Arial",14,"bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    number_of_letters = random.randint(8,10)
    number_of_numbers =  random.randint(2,4)
    number_of_symbols =  random.randint(2,4)

    all_char = [random.choice(LETTERS) for _ in range(number_of_letters)] 
    all_char += [random.choice(NUMBERS) for _ in range(number_of_numbers)] 
    all_char += [random.choice(SYMBOLS) for _ in range(number_of_symbols)]
    random.shuffle(all_char)
    random.shuffle(all_char)

    pass_value.set("".join(all_char))
    pyperclip.copy(pass_value.get())
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_entry():
    website = website_value.get()
    user = user_value.get()
    password = pass_value.get()
    if(website == "" or user == "" or password == ""):
        messagebox.showerror("Oops","Please don`t leave any fields empty!")
    else:
        if(messagebox.askyesno(title=f"{website}",message=f"These are the details entered: \n Email: {user}\n Password: {password} \n Is it ok to save?")):
            with open(f"{ROOT}Data.db",mode="a") as save_file:
                save_file.write(f"{website} | {user} | {password}\n")
            website_value.set("")
            pass_value.set("")


# ---------------------------- UI SETUP ------------------------------- #

tk = tkinter.Tk()
tk.config(padx=50,pady=50,bg="white")
tk.title("Password Manager")

canvas = tkinter.Canvas(width=200,height=200,bg="white",highlightthickness=0)

LOGO = tkinter.PhotoImage(file=f"{ROOT}logo.png")
canvas.create_image(100,100,image=LOGO)
canvas.grid(column=0,row=0,columnspan=3)


website_label = tkinter.Label(text="               Website:",font=TEXT_FONT,bg="white")
website_label.grid(column=0,row=1)

username_label = tkinter.Label(text="Email/Username:",font=TEXT_FONT,bg="white")
username_label.grid(column=0,row=2)

password_label = tkinter.Label(text="            Password:",font=TEXT_FONT,bg="white")
password_label.grid(column=0,row=3)

website_value = tkinter.StringVar()
website_input = tkinter.Entry(width=40,textvariable=website_value)
website_input.grid(column=1,row=1,columnspan=2)
website_input.focus()

user_value = tkinter.StringVar()
username_input = tkinter.Entry(width=40,textvariable=user_value)
username_input.insert(0,"ctboardman@msn.com")
username_input.grid(column=1,row=2,columnspan=2)

pass_value = tkinter.StringVar()
password_input = tkinter.Entry(width=21,textvariable=pass_value)
password_input.grid(column=1,row=3)

generate_password_button = tkinter.Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2,row=3)

add_button = tkinter.Button(text="Add",width=57,command=save_entry)
add_button.grid(column=0,row=4,columnspan=3,pady=20)

tk.mainloop()