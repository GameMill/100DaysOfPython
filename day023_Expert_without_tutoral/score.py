from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.goto(-250,270)
        self.Level = 1
    
    def Draw(self):
        self.clear()
        self.write(f"Level: {self.Level}", False, align="center", font=("Arial", 15, "bold"))        

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", False, align="center", font=("Arial", 25, "bold"))
