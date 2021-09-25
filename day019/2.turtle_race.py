from turtle import Turtle, Screen, position, title
import random

def create_turtle(y,color):
    tim = Turtle(shape="turtle")
    tim.up()
    tim.goto(x=0-(screen.window_width()/2)+20,y=y)
    tim.color(color)
    return tim


    

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

turtles = {
    "red":None,
    "orange":None,
    "yellow":None,
    "green":None,
    "blue":None,
    "indigo":None,
    "violet":None
}
i = 0
for item in turtles:
    y = (((screen.window_height()-100) / len(turtles))*i) - (((screen.window_height()-150)/2))
    turtles[item] = create_turtle(y,item)
    i += 1

def has_finished():
    """Check if any of the turtles has reached the end"""
    for item in turtles:
        if turtles[item].position()[0] >= 220:
            return True
    return False

def get_winner():
    """returns the winning color"""
    for item in turtles:
        if turtles[item].position()[0] >= 220:
            return item
    return ""

def move():
    for item in turtles:
        turtles[item].forward(random.randint(0,10))

while has_finished() == False:
    move()

winner = get_winner()
if user_bet.lower() == winner:
    print(f"You`ve won! The {winner} turtle is the winner!")    
else:
    print(f"You`ve lost! The {winner} turtle is the winner!")    

screen.exitonclick()