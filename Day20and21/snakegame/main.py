from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import random
screen = Screen()
screen.setup(width=800,height=800)
screen.bgcolor("black")
game_on = True
snake = Snake()
screen.tracer(0)
screen.listen()
food = Food()
scoreboard =Scoreboard()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
bite = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    print(snake.head)
    print(snake.head.distance(food))
    if snake.head.distance(food) <15 :
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        game_on = False
        scoreboard.game_over()

    for segment in snake.snake_position:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()


