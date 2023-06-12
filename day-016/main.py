## Day 16 - Exercises
## 12.06.2023

##import another_module
##print(another_module.another_variable)

##import turtle
##timmy = turtle.Turtle()

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("chocolate")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()