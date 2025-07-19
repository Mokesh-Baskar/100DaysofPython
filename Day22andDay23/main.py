from turtle import Screen
from paddlecreator import Paddle
from pong import Pong
import random
import time



screen = Screen()
screen.bgcolor("black") 
screen.setup(width=800,height=600)
screen.tracer(0)

paddle1 = Paddle(-350,0)
paddle2 = Paddle(350,0)
pong = Pong()

game_on = True
screen.listen()
screen.onkeypress(paddle1.moveup,"Up")
screen.onkeypress(paddle1.movedown,"Down")
screen.onkeypress(paddle2.moveup1,"w")
screen.onkeypress(paddle2.movedown1,"s")

while game_on :
    time.sleep(0.10)
    screen.update()
    pong.move()
    

    if pong.ycor() > 280 or pong.ycor() < -280 :
        pong.bounce_y()   
    if pong.distance(paddle1) < 30 :
        pong.bounce_x()
    elif pong.distance(paddle2)< 30:
        pong.bounce_x()
    elif pong.xcor() > 350 or pong.xcor() < -350 :
        game_on = False
    


    



screen.exitonclick()