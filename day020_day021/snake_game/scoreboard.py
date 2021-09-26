from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed(0)
        self.up()
        self.hideturtle()
        self.color("white")
        self.goto(0,280)

    
    def draw(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 12, "bold"))

    def increase(self):
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.color("yellow")
        self.write(f"Game Over", False, align="center", font=("Arial", 24, "bold"))

        
        