import random
from turtle import Turtle,Screen
import turtle

my_turtle = Turtle()
my_turtle.hideturtle()

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    my_turtle.color(R,G,B)

def walk():
    r = random.randint(0,4)
    if r > 0:
        my_turtle.right(90*r)
    my_turtle.forward(50)

screen = Screen()

my_turtle.width(10)
while True:
    change_color()
    walk()


