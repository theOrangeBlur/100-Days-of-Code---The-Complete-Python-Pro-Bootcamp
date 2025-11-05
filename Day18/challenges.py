import random
import turtle
from turtle import *
import random as rand


tim = Turtle()
tim.shape("turtle")
tim.color("aqua")
#challenge 1
# for i in range(4):
#     tim.forward(90)
#     tim.left(90)

#challenge 2
#line_width = 10
# for i in range(100):
#     tim.forward(line_width)
#     tim.penup()
#     tim.forward(line_width)
#     tim.pendown()

#challenge 3
# for side_num in range(3,11):
#     #screen.colormode
#     tim.pencolor((rand.random(), rand.random(), rand.random()))
#     for i in range(side_num):
#         tim.forward(100)
#         tim.left(360/side_num)

#challenge 4
# tim.pensize(10)
# tim.speed(0)
# turtle.colormode(255)
# for i in range(500):
#     tim.pencolor((rand.randint(0,255), rand.randint(0,255), rand.randint(0,255)))
#     directions = [0, 90, 180, 270]
#     tim.setheading(random.choice(directions))
#     tim.forward(25)

#challenge 5
tim.speed(0)
turtle.colormode(255)
steps = 100
for i in range(steps):
    tim.pencolor((rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255)))
    tim.left(360/steps)
    tim.circle(50)

screen = Screen()
screen.exitonclick()