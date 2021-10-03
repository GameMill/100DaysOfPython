import tkinter
from typing import Text

def converter(p1,p2,p3):
    try:
        mile = int(miles.get())
        label3["text"] = f"{mile*1.609:0.2f}"
    except:
        pass 

tk = tkinter.Tk()
tk.title("Mile to Km Converter")
tk.config(padx=20,pady=20)
miles = tkinter.StringVar(value="0")
miles_input = tkinter.Entry(textvariable=miles)
miles_input.grid(column=1, row=0)
miles.trace_add("write",converter)


label1 = tkinter.Label(text="Miles")
label1.grid(column=2,row=0)

label2 = tkinter.Label(text="is equal to")
label2.grid(column=0,row=1)

label3 = tkinter.Label(text="0")
label3.grid(column=1,row=1)

label4 = tkinter.Label(text="Km")
label4.grid(column=2,row=1)

tk.mainloop()