
from turtle import Screen, Turtle, heading
import time
import random

class Ball(Turtle):
    current_speed = 5
    def __init__(self,screen):
        super().__init__(shape="circle")
        self.screen = screen
        self.up()
        self.color("white")
        self.goto(0,80)
        self.random_direction()
    
    def random_direction(self):
        r = random.randint(0,90)
        if(random.randint(0,1) == 0):
            self.setheading((315 + r) % 360)
        if(random.randint(0,1) == 1):
            self.setheading(225-r)

    def reset_pos(self):
        self.goto(0,0)
        self.random_direction()
        self.current_speed = 5
        self.screen.update()
        time.sleep(1)

        

    def update(self):
        self.forward(self.current_speed)

    def has_hit_wall(self,screen):
        window_width = (screen.window_width()/2)-20
        window_height = (screen.window_height()/2)-20
        x = self.xcor()
        if(abs(x) >= window_width):
            return True
        heading = self.heading()
        y = self.ycor()
        if(y >= window_height):#and heading > 45 and heading < 135):
            diff = (90-self.heading())
            self.setheading(270+diff)
        elif(y <= 0-window_height):
            diff = (270-self.heading())
            self.setheading(90+diff)
        return False

