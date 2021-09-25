from turtle import Turtle,Screen, reset

tim = Turtle()
screen = Screen()


def forward():
    tim.forward(10)
def back():
    tim.back(10)
def left():
    tim.left(10)
def right():
    tim.right(10)

def reset():
    screen.mode("standard")

screen.listen()
screen.onkeypress(forward,"Up")
screen.onkeypress(back,"Down")
screen.onkeypress(left,"Left")
screen.onkeypress(right,"Right")
screen.onkeypress(forward,"w")
screen.onkeypress(back,"s")
screen.onkeypress(left,"a")
screen.onkeypress(right,"d")
screen.onkey(reset,"c")

screen.exitonclick()