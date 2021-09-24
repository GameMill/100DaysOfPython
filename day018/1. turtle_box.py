from turtle import Turtle,Screen, color

tim = Turtle()
tim.shape("turtle")
tim.color("#ff0000")

# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

for item in range(50):
    tim.down()
    tim.forward(2)
    tim.up()
    tim.forward(2)





screen = Screen()
screen.exitonclick()