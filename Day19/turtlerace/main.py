import random
import turtle as t


screen = t.Screen()

screen.screensize(800,800)


color=["red","green","yellow","black","orange"]


yposition = [-400,-200,0,200,400 ]
allparticipant = []



for i in range(5):
    new_turtle = t.Turtle()
    new_turtle.shape("turtle")
    new_turtle.shapesize(2)
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.setposition(-350,yposition[i])
    allparticipant.append(new_turtle)

line_crossed = int(0)
while not(line_crossed) :
    
    for i in range(5):
        allparticipant[i].forward(random.randint(0,10))
        pos = allparticipant[i].position()
        if pos[0] > 350 :
            turtlecolor,pencolor = allparticipant[i].color()
            print(f"Winner is {turtlecolor}")
            line_crossed = 1
            break
    


screen.exitonclick()
