
from turtle import Turtle,Screen
import random
INITIAL_POSITION = [(0,0),(-20,0),(-40,0)]

FOOD_COR = range(0,20,2)


class Snake:

    def __init__(self):
        self.snake_position = []
        
        for i in range(0,3):
            new_square = Turtle()
            new_square.shape("square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(INITIAL_POSITION[i]) 
            new_square.speed("fastest")
            self.snake_position.append(new_square)
        self.head = self.snake_position[0]    
                 
    def move(self):
            for i in range(len(self.snake_position)-1,0,-1):
                xaxis=self.snake_position[i-1].xcor()
                yaxis=self.snake_position[i-1].ycor()
                self.snake_position[i].goto(xaxis,yaxis)
            self.head.forward(20)
             

    def up(self):
         current_heading = self.head.heading()

         if current_heading !=90 and current_heading !=270 :
            self.head.setheading(90)
    
    def down(self):
         current_heading = self.head.heading()

         if current_heading !=90 and current_heading !=270 :
            self.head.setheading(270)

    def left(self):
         current_heading = self.head.heading()
         if current_heading !=180 and current_heading !=0 :
            self.head.setheading(180)

    def right(self):
         current_heading = self.head.heading()         
         if current_heading !=180 and current_heading !=0 :        
            self.head.setheading(0)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_position.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_position[-1].position())            
    
