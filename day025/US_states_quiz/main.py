from turtle import Screen, Turtle
import os
import pandas

from typing import Text

pen = Turtle()
pen.up()
pen.hideturtle()

root = os.path.dirname(os.path.abspath(__file__)) + "/"
states_data = pandas.read_csv(f"{root}50_states.csv")
screen = Screen()
screen.setup(width=725,height=491)
screen.bgpic(f"{root}blank_states_img.gif")

correct_states = []
num_of_states = len(states_data)
while(num_of_states >= len(correct_states)):
    try:
        Guess = screen.textinput(title=f"{len(correct_states)}/{num_of_states} States Correct",prompt="What`s another state`s name?: ").strip().lower().title()
        if(Guess == ""):
            continue
    except:
        Guess = "Exit"
    if(Guess == "Exit"):
        break
    data = states_data.state.str.contains(Guess,case=False)
    data = states_data[states_data.index == data[data].index[0]]

    if(correct_states.__contains__(data.state.item()) == False):
        correct_states.append(data.state.item())
        x = data.x.item()
        y = data.y.item()
        pen.goto(x,y)
        pen.write(data.state.item(), move=False, align="center", font=("Arial", 8, "bold"))


incorrect_states = {"Incorrect States":[]}
incorrect_states["Incorrect States"] = [state for state in states_data.state if state not in correct_states]
# for item in states_data.state:
#     if(item not in correct_states):
#         incorrect_states["Incorrect States"].append(item)


incorrect_states = pandas.DataFrame(incorrect_states)
incorrect_states.to_csv(f"{root}incorrect_states.csv")


# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)

# screen.mainloop()
screen.exitonclick()