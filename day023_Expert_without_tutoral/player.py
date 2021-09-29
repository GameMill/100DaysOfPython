from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.current_speed = 10
        self.setheading(90)
        self.shape("turtle")
        self.back_to_start()

    def level_up(self):
        self.current_speed += 2
        self.back_to_start()
    
    def back_to_start(self):
        self.goto(0,-280)

    def move(self):
        self.forward(self.current_speed)
        