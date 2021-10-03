import tkinter



def button_clicked():
    my_label["text"] = sv.get().lower().title()

def callback(*args):
    my_label["text"] = sv.get().lower().title()
    return True




windows = tkinter.Tk()
windows.title("My First Tkinter GUI Program")
windows.minsize(width=500,height=500)
windows.config(padx=50,pady=50)

#Labels
my_label = tkinter.Label(text="I Am a Label", font=("Arial",24, "bold"))
#my_label.pack()
my_label.grid(column=0,row=0)
my_label.config(padx=20,pady=20)

button = tkinter.Button(text="Hello World",command=button_clicked)
#button.pack()
button.grid(column=1,row=1)

button = tkinter.Button(text="Hello World",command=button_clicked)
#button.pack()
button.grid(column=2,row=0)

sv = tkinter.StringVar()
entry = tkinter.Entry(width=10,textvariable=sv)
sv.trace_add("write", callback)
#entry.pack()
entry.grid(column=3,row=2)
#entry.place(x=10,y=100)

windows.mainloop()