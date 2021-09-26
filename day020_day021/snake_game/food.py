from turtle import Turtle
import random

class Food(Turtle):
    SHAPE = "circle"
    COLOR = "blue"
    def __init__(self):
        super().__init__(shape=self.SHAPE)
        self.up()
        self.color(self.COLOR)
        self.speed(0)
        #self.shapesize(.5,.5)
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-270,270)
        random_y = random.randint(-250,250)
        self.goto(random_x,random_y)