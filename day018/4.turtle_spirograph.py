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



screen = Screen()
my_turtle.speed("fastest")
my_turtle.up()
number = 10
for y in range(number):
    c_y = ((y*70) - ((screen.window_height()-70)/2)) + ((screen.window_height()-(10*70))/2)
    for x in range(number):
        c_x = ((x*70) - ((screen.window_width()-70)/2)) + ((screen.window_width()-(10*70))/2)
        change_color()
        my_turtle.setpos(c_x,c_y)
        my_turtle.dot(50)



screen.exitonclick()