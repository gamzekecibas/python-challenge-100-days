## SNAKE GAME PROJECT

from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    ## Detect collusion with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()

##  for part in snake_body:
##      part.forward(20)
##      screen.update()
##      time.sleep(1) to monitor update method

screen.exitonclick()