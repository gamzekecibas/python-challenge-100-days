## Day 19 | High Order Functions
## PROJECT: Turtle Race
## 15.06.2023

from turtle import Turtle, Screen
import random

is_race_on = False
my_screen = Screen()
my_screen.setup(width = 500, height = 400)
user_choice = my_screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color from rainbow: ")
print(f"You choose Turtle {user_choice}! Good Luck!")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_coord = 220

all_turtles = []
for color in colors:
    y_coord -= 55

    globals()[f'turtle_{color}'] = Turtle(shape = 'turtle')
    globals()[f'turtle_{color}'].color(color)
    globals()[f'turtle_{color}'].penup()
    globals()[f'turtle_{color}'].goto(x=-230, y=y_coord)
    all_turtles.append(globals()[f'turtle_{color}'])

if user_choice:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_choice:
                print(f"You win! Turtle {win_color} is winner!!")
            else:
                print(f"You lose! Turtle {win_color} is winner :((")

        rand_step = random.randint(0, 10)
        turtle.forward(rand_step)

my_screen.exitonclick()