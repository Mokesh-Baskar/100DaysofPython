import random

import turtle as t
#import the turtle as a whole as we need to set the color mode 

tim = t.Turtle()
tim.shape ="Arrow"
t.colormode(255)
screen = t.Screen()



def randcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    rancolor =(r,g,b)
    return rancolor
for _ in range(100):
    tim.pencolor(randcolor())
    head = tim.heading()
    tim.setheading(head+20)
    tim.circle(100)



screen.exitonclick()    