#lets dive into basics of object oriented programming in python


#turtle is a inbuilt lib in python for teaching kids about coding
from turtle import Turtle,Screen

#lets create a object with the class
Rune = Turtle()

print(Rune)
Rune.shape("turtle")
Rune.color("red")
Rune.forward(100)

my_screen = Screen()

print(my_screen.canvheight) 
my_screen.exitonclick()