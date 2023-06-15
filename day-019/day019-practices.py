## Day 19 | High Order Functions - Exercises
## 15.06.2023
"""
def calculator(n1, n2, func):
    return func(n1, n2)

EXP: from calculator project:
result = calculator(2, 3, mulliply)
result = 6
"""

from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')
my_screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_ccw():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_cw():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

#my_screen.listen()
#my_screen.onkey(key = 'space', fun = move_forwards)
#my_screen.exitonclick()

def etch_a_sketch():
    my_screen.listen()
    my_screen.onkey(key='w', fun=move_forwards)
    my_screen.onkey(key='s', fun=move_backwards)
    my_screen.onkey(key='a', fun=turn_ccw)
    my_screen.onkey(key='d', fun=turn_cw)
    my_screen.onkey(key='c', fun=clear_drawing)

    my_screen.exitonclick()

#etch_a_sketch()