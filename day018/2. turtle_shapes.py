import random
from turtle import Turtle,Screen

my_turtle = Turtle()

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    my_turtle.color(R,G,B)

def draw_shape(sides):
    change_color()
    angle = 360 / (sides)
    for item in range(sides):
        my_turtle.forward(50)
        my_turtle.right(angle)

        




for item in range(3,24):
    draw_shape(item)
    


screen = Screen()
screen.exitonclick()