from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import random

GAME_SPEED = 0.075

screen = Screen()
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake(3)
food = Food()
scoreboard = Scoreboard()

# game border
border = Turtle()
border.up()
border.hideturtle()
border.color("white")
border.speed(0)
border.goto((-290,270))
border.down()
border.goto((290,270))
border.goto((290,-270))
border.goto((-290,-270))
border.goto((-290,270))
# end of game border

screen.listen()

screen.onkey(snake.Up,"Up")
screen.onkey(snake.Left,"Left")
screen.onkey(snake.Right,"Right")
screen.onkey(snake.Down,"Down")



is_alive = True
last_tick = time.time_ns()
while is_alive:
    ns = time.time_ns()
    time_delta = (time.time_ns()-last_tick)/1000000000
    last_tick = ns + ((GAME_SPEED-time_delta)*1000000000)
    print(f"Tick: {time_delta}")
    scoreboard.draw()
    screen.update()
    
    time.sleep(GAME_SPEED-time_delta)
    
    snake.Move()

    if snake.snake[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase()
        snake.add_extra_piece()
    
    is_alive = snake.not_hit_wall() and snake.not_hit_tail()

    
scoreboard.game_over()

screen.exitonclick() 