from turtle import Turtle

class Paddle(Turtle):
    paddle = []
    screen = None
    up_key_pressed = False
    down_key_pressed = False
    def __init__(self,x,angle,screen):
        self.screen = screen
        super().__init__(shape="square")
        self.up()
        self.goto(x,0)
        self.speed(0)
        self.color("gray")
        self.shapesize(1,7)
        self.setheading(angle)

    def reg_input(self,Up,Down):
        self.screen.onkeypress (self.on_up_key_pressed,Up)
        self.screen.onkeypress (self.on_down_key_pressed,Down)
        self.screen.onkey (self.on_up_key_released,Up)
        self.screen.onkey (self.on_down_key_released,Down)
    
        
    def update(self):
        if(self.up_key_pressed):
            self.Up()

        if (self.down_key_pressed):
            self.Down()
    
    def has_hit(self,ball):
        pos = ball.pos()
        x = self.xcor()
        y = self.ycor()
        x_hit = (x < 0 and x+10 >= pos[0]) or (x > 0 and x-10 <= pos[0])
        if(x_hit == False):
            return False

        y_size = (self.shapesize()[1]*10)+20
        diff_y_org = self.ycor() -  pos[1]
        diff_y = abs(diff_y_org)
        y_hit = diff_y > 0 and y_size >= diff_y# or diff_y <= 0 and (0-y_size) <= diff_y)
        if(y_hit == False):
            return False
        # Ball Has Hit
        Precentage = diff_y/y_size
        angle = 45*Precentage
        if(self.heading() < 180):
            if(diff_y_org > 0):
                ball.setheading((self.heading()+90)+angle)
            else:
                ball.setheading((self.heading()+90)-angle)
            ball.current_speed += 0.5
        else:
            if(diff_y_org > 0):
                ball.setheading((self.heading()+90)-angle)
            else:
                ball.setheading((self.heading()+90)+angle)
            ball.current_speed += 0.5

        return True
    def on_down_key_pressed(self):
        self.down_key_pressed = True
    def on_up_key_pressed(self):
        self.up_key_pressed = True
    def on_down_key_released(self):
            self.down_key_pressed = False
    def on_up_key_released(self):
        self.up_key_pressed = False
        

    def Up(self):
        y = self.ycor()
        if y < 270:
            if(self.heading() < 180):
                self.forward(10)
            else:
                self.forward(-10)

    def Down(self):
        y = self.ycor()
        if y > -270:
            if(self.heading() < 180):
                self.back(10)
            else:
                self.back(-10)

        
        