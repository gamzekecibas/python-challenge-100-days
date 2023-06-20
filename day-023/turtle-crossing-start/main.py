import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
theTurtle = Player()
manageCars = CarManager()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(theTurtle.move_north, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    manageCars.create_car()
    manageCars.move_cars()

    ## Detect collusion turtle & cars
    for car in manageCars.all_cars:
        if car.distance(theTurtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    ## Detect to reach north edge
    if theTurtle.ycor() > 280:
        theTurtle.goto(0, -280)
        manageCars.level_up()
        scoreboard.update_level()
screen.exitonclick()