from turtle import Screen
from player import Player
from carmanager import CarManager
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

player = Player()
car =  CarManager()

gameon = True


screen.onkeypress(player.forward,'Up')

while gameon:
    time.sleep(0.1)
    screen.update()
    car.createcars()
    collision = car.movecar(player)
    if collision == True:
        gameon = False
        print("You Lost") 

    if player.ycor()>280 :
        gameon = False
        print("You Won")
    


screen.exitonclick()