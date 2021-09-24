import colorgram
import random
from turtle import Turtle,Screen, color
import turtle

# Extract 6 colors from an image.
colors = colorgram.extract('rect846.png', 6)
color_list = []
for item in colors:
    color_list.append((item.rgb[0],item.rgb[1],item.rgb[2]))


my_turtle = Turtle()
my_turtle.hideturtle()


screen = Screen()
my_turtle.speed("fastest")
screen.colormode(255)

my_turtle.width(0)
number = 5
for item in range(number):
    my_turtle.fillcolor(random.choice(color_list))
    my_turtle.circle(100)
    my_turtle.right(360/number)


screen.exitonclick()