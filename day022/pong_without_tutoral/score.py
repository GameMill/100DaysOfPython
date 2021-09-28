from turtle import Turtle, up

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.goto(0,250)
        self.player1 = 0
        self.player2 = 0
        self.up()
        self.hideturtle()
    
    def Draw(self):
        self.clear()
        self.write(f"{self.player1}   {self.player2}", False, align="center", font=("Arial", 30, "bold"))
