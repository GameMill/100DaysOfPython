from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.setheading(180)
        self.shape("square")
        self.shapesize(1,2)
        self.back_to_start()
        self.current_speed = 10
        self.color(random.random(),random.random(),random.random())
    
    def has_hit(self,player):
        pos = player.pos()
        car_pos = self.pos()
        diff_pos = (abs(pos[0]-car_pos[0]),abs(pos[1]-car_pos[1]))
        if(diff_pos[1] <= 40):
            if(diff_pos[0] <= 60):
                return True
        return False
        

    def back_to_start(self):
        self.goto(280,random.randint(-250,260))
    
    def update(self):
        self.forward(self.current_speed)

        return self.xcor() < -310