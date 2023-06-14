###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##

import colorgram
import turtle as T
import random
def extract_colors_from_image(path, num_colors):
    rgb_colors = []
    colors = colorgram.extract(path, num_colors)
    for color in colors:
        red = color.rgb.r / 255
        green = color.rgb.g / 255
        blue = color.rgb.b / 255

        new_color = (red, green, blue)
        rgb_colors.append(new_color)

    return rgb_colors

color_list = extract_colors_from_image('image.jpg', 30)
T.hideturtle()
T.penup()
for n in range(10):
    for _ in range(10):
        T.pencolor(random.choice(color_list))
        T.dot(20)
        T.forward(50)
    if n % 2 == 0:
        T.left(90)
    else:
        T.right(90)
    T.forward(50)
    if n % 2 == 0:
        T.left(90)
    else:
        T.right(90)