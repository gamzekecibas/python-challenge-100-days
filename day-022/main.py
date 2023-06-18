from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.title("Pong")
my_screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


my_screen.listen()
my_screen.onkey(r_paddle.go_up, "Up")
my_screen.onkey(r_paddle.go_down, "Down")
my_screen.onkey(l_paddle.go_up, "w")
my_screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    my_screen.update()
    ball.move()

    ## Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    ## Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    ##Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    ##Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


my_screen.exitonclick()