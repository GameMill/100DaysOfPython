from turtle import Turtle
import turtle



class Snake:
    MOVE_DISTANCE = 20
    STARTING_XY = (0,0)

    def __init__(self,starting_lengh):
        self.Create_Snake(starting_lengh)

    def add_extra_piece(self):
        pos1 = self.snake[-1].pos()
        pos2 = self.snake[-2].pos()
        posdiff = (pos1[0]-pos2[0],pos1[1]-pos2[1])
        self.increase(pos1[0]+posdiff[0],pos1[1]+posdiff[1])
        
    def increase(self,x,y):
        turtle = Turtle(shape="square")
        turtle.up()
        turtle.speed(0)
        turtle.color("white")
        turtle.goto(x,y)
        self.snake.append(turtle)

    def Create_Snake(self,starting_lengh):
        self.snake = []
        for item in range(starting_lengh):
            self.increase(x=self.STARTING_XY[0]+ item*-self.MOVE_DISTANCE,y=self.STARTING_XY[1])

    def Left(self):
        if(self.snake[0].heading() == 0):
            return
        self.snake[0].setheading(180)

    def Right(self):
        if(self.snake[0].heading() == 180):
            return
        self.snake[0].setheading(0)

    def not_hit_tail(self):
        for item in self.snake[1:]:
            if  self.snake[0].distance(item) < 10:
                return False
        return True

    def not_hit_wall(self):
        self.snake[0]
        x = self.snake[0].xcor()
        y = self.snake[0].ycor()
        return x < 290 and x > -290 and y < 270 and y > -270 
    
    def Up(self):
        if(self.snake[0].heading() == 270):
            return
        self.snake[0].setheading(90)

    def Down(self):
        if(self.snake[0].heading() == 90):
            return
        self.snake[0].setheading(270)
    
    def Move(self):
        for item in range(len(self.snake)-1,0,-1):
            self.snake[item].goto(self.snake[item-1].pos())
        self.snake[0].forward(self.MOVE_DISTANCE)
        