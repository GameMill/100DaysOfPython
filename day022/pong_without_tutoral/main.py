from turtle import Screen, Turtle, title
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time
import turtle

screen = Screen(title="Pong")
screen.setup(width=600,height=600)
screen.bgcolor("black")

screen.tracer(0)

border = turtle.Turtle()
border.up()
border.hideturtle()
border.goto(0,300)
border.setheading(270)
border.color("white")
for item in range(30):
    border.down()
    border.forward(10)
    border.up()
    border.forward(10)
    


left_Paddle = Paddle(-270,270,screen)
right_Paddle = Paddle(270,90,screen)

right_Paddle.reg_input("Up","Down")
left_Paddle.reg_input("w","s")

screen.listen()

score_board = ScoreBoard()
ball = Ball(screen)


is_running = True
while(is_running):
    
    if(left_Paddle.has_hit(ball) == False):
        if(right_Paddle.has_hit(ball) == False):
            if(ball.has_hit_wall(screen)):
                if(ball.xcor() < 0):
                    score_board.player2 += 1
                else:
                    score_board.player1 += 1
                ball.reset_pos()

    left_Paddle.update()
    right_Paddle.update()
    ball.update()
    score_board.Draw()
    screen.update()

    is_running = (score_board.player1 == 10 or score_board.player2 == 10) == False
    time.sleep(0.041)

screen.exitonclick()
