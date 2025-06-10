from turtle import Turtle,Screen
import random
colors = [
    "red", "blue", "green", "yellow", "orange", "purple",
    "pink", "brown", "black", "gray", "cyan",
    "magenta", "gold", "silver", "navy", "maroon", "lime",
    "olive", "teal", "aqua", "fuchsia", "chocolate", "coral",
    "darkgreen", "darkblue", "darkred", "lightblue", "lightgreen"
]
tim_the_turtle = Turtle()
screen = Screen()
tim_the_turtle.shape("turtle")
tim_the_turtle.turtlesize(2)
tim_the_turtle.color("yellow")
tim_the_turtle.pencolor("black")
tim_the_turtle.pensize(10)

#basic movement of the object

tim_the_turtle.forward(100)

tim_the_turtle.reset()

#since we have reset the values lets set those again
tim_the_turtle.shape("turtle")
tim_the_turtle.turtlesize(2)
tim_the_turtle.color("yellow")
tim_the_turtle.pencolor("black")
tim_the_turtle.pensize(10)

#Lets write code to create a square 
#we need to use right method and angle value in turtle class

for _ in range(4) :
    tim_the_turtle.forward(100)
    tim_the_turtle.right(90)


tim_the_turtle.reset()

tim_the_turtle.shape("turtle")
tim_the_turtle.turtlesize(2)
tim_the_turtle.color("yellow")
tim_the_turtle.pencolor("black")
tim_the_turtle.pensize(10)
tim_the_turtle.speed('normal')

#lets loop through the number of sides and create the sides with different colors

def shapecreator(numberofsides) :

    angle = 360/numberofsides
    for _ in range(numberofsides) :
        tim_the_turtle.forward(100)
        tim_the_turtle.right(angle)

for i in range(3,11) :
    tim_the_turtle.pencolor(random.choice(colors))
    shapecreator(i)

anglelist = [0,90,180,270]

#random line generator
tim_the_turtle.reset()

tim_the_turtle.shape("turtle")
tim_the_turtle.turtlesize(2)
tim_the_turtle.color("yellow")
tim_the_turtle.pencolor("black")
tim_the_turtle.pensize(10)
tim_the_turtle.speed('normal')
tim_the_turtle.hideturtle()

for _ in range(200) :
    tim_the_turtle.forward(40)
    tim_the_turtle.setheading(random.choice(anglelist))
    tim_the_turtle.pencolor(random.choice(colors))
screen.exitonclick()

