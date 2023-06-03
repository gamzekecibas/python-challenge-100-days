## Day 6 - Beginner | Functions & Karel
## 03.06.2023
## ----
## DAY 6 PROJECT Escape the Maze in Reeborg's World
## ----
## It is tested 3 times.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def step_decision():
    if not front_is_clear():
        while not front_is_clear():
            turn_left()
        move()

while not at_goal():
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        if wall_on_right():
            step_decision()
            if front_is_clear():
                move()
        else:
            if right_is_clear():
                turn_right()
            else:
                turn_left()
            if front_is_clear():
                move()