import tkinter
import os
import requests
from requests.models import HTTPError
ROOT = os.path.dirname(os.path.abspath(__file__)) + "/"

def get_quote():
    try:
        response = requests.get("https://api.kanye.rest/")
        response.raise_for_status()
        data = response.json()
        canvas.itemconfigure(quote_text,text=data["quote"])
        

    except HTTPError as error:
        print(error)



window = tkinter.Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=300, height=414)
background_img = tkinter.PhotoImage(file=f"{ROOT}background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = tkinter.PhotoImage(file=f"{ROOT}kanye.png")
kanye_button = tkinter.Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()