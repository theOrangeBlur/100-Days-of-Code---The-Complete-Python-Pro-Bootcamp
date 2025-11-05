import colorgram
import random
import turtle as t
from turtle import *

def get_colors(image):
    # Extract n colors from an image.
    colors = colorgram.extract(image, 30)

    color_list = []
    total_num_colors = 12
    current_num_colors = 0
    for color in colors:
        if color.rgb.r > 230 and color.rgb.g > 230 and color.rgb.b > 230:
            continue
        color_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
        current_num_colors += 1
        if total_num_colors == current_num_colors:
            break
    return color_list

color_list = get_colors('the-scream.jpg')

timmy = t.Turtle()
screen = t.Screen()
timmy.speed(0)
screen.colormode(255)
timmy.penup()
for i in range(4, -6, -1):
    timmy.home()
    timmy.setheading(180)
    timmy.forward(50*5)
    timmy.setheading(270)
    timmy.forward(25)
    timmy.forward(i*50)

    for j in range(10):
        timmy.color(random.choice(color_list))
        timmy.begin_fill()
        timmy.pendown()
        timmy.setheading(0)
        timmy.circle(20)
        timmy.end_fill()
        timmy.penup()
        timmy.forward(50)


screen.exitonclick()