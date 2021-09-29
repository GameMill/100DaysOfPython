from turtle import Screen
from player import Player
from car import Car
from score import ScoreBoard
import random
import time

screen = Screen()
screen.title("Why cross the road?")
screen.setup(600,600)
screen.tracer(0)

player = Player()
screen.onkeypress(player.move,"Up")

screen.listen()
score = ScoreBoard()

cars = []

change = 20
is_running = True
while is_running:
    if(random.randint(0,change) == 1):
        cars.append(Car())

    for car in cars:
        if(car.update()):
            print("removing")
            car.clear()
            car.ht()
            cars.remove(car)
        elif(car.has_hit(player)):
            is_running = False
    
    if(player.ycor() > 270):
        score.Level += 1
        player.level_up()
        if(change > 2):
            change -= 1

    score.Draw()
    screen.update()
    time.sleep(0.1)

# game over
score.game_over()

screen.exitonclick()