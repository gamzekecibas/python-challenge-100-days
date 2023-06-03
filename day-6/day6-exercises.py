## Day 6 - Beginner | Functions & Karel
## 03.06.2023
## Exercises

## These script should be run on https://reeborg.ca/reeborg.html

## Exercise - 1: Turn Around
def turn_around():
    turn_left()
    turn_left()


move()
move()
turn_around()
move()
move()
turn_around()

## Exercise - 2 Turn Right
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def four_square_move():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_around()

four_square_move()

## Exercise - 3 Hurdles Loop Challenge
## https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
def hurdle1_challenge_step():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for jump in range(6):
    hurdle1_challenge_step()


## Exercise 4- While Loop
number_of_hurdles = 6
while number_of_hurdles > 0 :
    hurdle1_challenge_step()
    number_of_hurdles -= 1


## Hurdle2 - challenge (randomly change of finish Hurdle1)
while at_goal() != True:     ## while not at_goal():
    hurdle1_challenge_step()


## Hurdle3 - challenge
def hurdle_step():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        hurdle_step()
    else:
        move()

## Hurdle4 - challenge
def modified_hurdle_step():
    turn_left()
    while wall_on_right():
        move()

    turn_right()
    move()
    turn_right()

    while front_is_clear():
        move()

    turn_left()


while not at_goal():
    if wall_in_front():
        modified_hurdle_step()
    else:
        move()
