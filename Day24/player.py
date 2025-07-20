from turtle import Turtle



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("yellow")
        self.penup()
        self.setheading(90)
        self.goto(0,-280)
        self.move = 10

    def forward(self):
        ypos = self.ycor()
        self.goto(0,ypos+self.move)
