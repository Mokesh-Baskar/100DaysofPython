from turtle import Turtle
import random
class Food(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.refresh()
        


    def refresh(self):
        self.goto(random.randint(-380,380),random.randint(-380,380))