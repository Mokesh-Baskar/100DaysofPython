import colorgram
import turtle as t
import random
colors = colorgram.extract('hirst.jpg', 30)
allcolors = []
for color in colors:
    r =  color.rgb.r 
    g =  color.rgb.g
    b =  color.rgb.b
    allcolors.append((r,g,b))


t.colormode(255)
tim = t.Turtle()
tim.shape("arrow")
tim.speed(0)
screen = t.Screen()
#moving to left corner of screen
tim.penup()
tim.setheading(225)
tim.forward(500)
tim.setheading(0)
tim.pensize(10)

#function to reset the position
def resetposition():
    tim.setheading(90)
    tim.forward(20)
    tim.setheading(180)
    tim.forward(800)
    tim.setheading(0)
#funtion to 
def dotmaker():
    for _ in range(40) :
        tim.pencolor(random.choice(allcolors))
        tim.pendown()
        tim.forward(2)
        tim.penup()
        tim.forward(18)
for _ in range(20):
#making the dor movement
    dotmaker()
#moving the icon to start position

    resetposition()






screen.exitonclick()



