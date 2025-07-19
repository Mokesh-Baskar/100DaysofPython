from turtle import Turtle



class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("red")
        self.x_new = 10
        self.y_new = 10
        self.goto(0,0)
        
    def move(self):
        newx = self.xcor() + self.x_new
        newy = self.ycor() + self.y_new
        self.goto(newx,newy)


    def bounce_y(self):

        self.y_new = self.y_new*-1

    def bounce_x(self):
        self.x_new = self.x_new*-1
