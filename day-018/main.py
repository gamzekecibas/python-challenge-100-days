## Day 18 - Exercises
## 14.06.2023

from turtle import Turtle, Screen
import random

## Exercise - 0
tim = Turtle()
tim.shape("turtle")
tim.color("teal")
#timmy_the_turtle.forward(100)
#timmy_the_turtle.right(90)

## Challenge - 1: Draw Square
def draw_square(the_turtle):
    for _ in range(4):
        the_turtle.forward(100)
        the_turtle.left(90)

#draw_square(tim)

def dashed_line(the_turtle, n):
    for _ in range(n):
        the_turtle.forward(10)
        the_turtle.penup()
        the_turtle.forward(10)
        the_turtle.pendown()

#dashed_line(tim, 50)

def draw_shapes(the_turtle):
    for num_edges in range(3, 11):
        the_angle = 360 / num_edges

        red = random.randrange(256) / 255
        green = random.randrange(256) / 255
        blue = random.randrange(256) / 255

        # Create the RGB color tuple
        rgb = (red, green, blue)
        the_turtle.pencolor(rgb)

        for edge in range(num_edges):
            the_turtle.forward(100)
            the_turtle.right(the_angle)

#draw_shapes(tim)

def random_color():
    red = random.randrange(256) / 255
    green = random.randrange(256) / 255
    blue = random.randrange(256) / 255

    # Create the RGB color tuple
    rgb = (red, green, blue)
    return rgb

def random_walk(the_turtle, number_steps):

    the_turtle.speed(5)
    the_turtle.pensize(8)
    for _ in range(number_steps):
        the_turtle.pencolor(random_color())

        the_angle = random.choice([-90, 90])
        the_turtle.right(the_angle)
        the_turtle.forward(30)

#random_walk(tim, 50)

def draw_spirograph(the_turtle, num_circles, rad = 100):
    the_turtle.speed(20)
    for _ in range(num_circles):
        the_turtle.pencolor(random_color())
        the_turtle.circle(rad)
        the_turtle.left(360/num_circles)

#draw_spirograph(tim, num_circles = 100, rad = 100)



my_screen = Screen()
my_screen.exitonclick()