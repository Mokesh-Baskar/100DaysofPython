from turtle import Turtle
import random

COLORS = ["yellow","green","silver","violet","blue","red","brown"] 
CARPOS = [-260,-240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240,260]


class CarManager:
    def __init__(self):
        self.allcars=[]

    def createcars(self) :
        if random.randint(1,4) == 1 :
            newcar = Turtle()
            newcar.penup()
            newcar.setheading(180)
            newcar.shape("square")
            newcar.color(random.choice(COLORS))
            newcar.shapesize(stretch_len=2,stretch_wid=1)
            newcar.goto(280,random.choice(CARPOS))
            self.allcars.append(newcar)
    
    def movecar(self,player):
        
        for car in self.allcars:
            car.forward(10)
            if car.distance(player) < 20 :
                return True

