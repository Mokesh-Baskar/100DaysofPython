from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,xcor,ycor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid= 4, stretch_len=1)
        self.color("white")
        self.goto(xcor,ycor)

    def moveup(self):
        position = self.pos()
        xpos = position[0]
        ypos = position[1]
        self.goto(xpos,ypos+20)

    def movedown(self):
        position = self.pos()
        xpos = position[0]
        ypos = position[1]
        self.goto(xpos,ypos-20)


    def moveup1(self):
        position = self.pos()
        xpos = position[0]
        ypos = position[1]
        self.goto(xpos,ypos+20)

    def movedown1(self):
        position = self.pos()
        xpos = position[0]
        ypos = position[1]
        self.goto(xpos,ypos-20)    
