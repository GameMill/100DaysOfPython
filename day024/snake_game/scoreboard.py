import fileinput
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        try:
            with open("hi_score.txt") as file:
                self.hi_score = int(file.readline())
        except:
            self.hi_score = 0
            self.save_hi_score()
        
        self.score = 0
        self.speed(0)
        self.up()
        self.hideturtle()
        self.color("white")
        self.goto(0,280)

    def save_hi_score(self):
        with open("hi_score.txt",mode="w") as file:
            file.write(str(self.hi_score))

    def draw(self):
        self.clear()
        self.write(f"Score: {self.score} | Hign Score: {self.hi_score}", False, align="center", font=("Arial", 12, "bold"))

    def increase(self):
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.color("yellow")
        self.write(f"Game Over", False, align="center", font=("Arial", 24, "bold"))

    def reset(self):
        if(self.score > self.hi_score):
            self.hi_score = self.score
            self.save_hi_score()
        self.score = 0
        self.draw()
        
        
        