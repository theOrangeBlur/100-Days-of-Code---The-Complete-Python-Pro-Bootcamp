from turtle import *
import random
DISTANCE = 5
ANGLE = 10
HEIGHT = 400
WIDTH = 500


def get_ready(turtle_list):
    x = -230
    y = -180
    i = 0
    spacing = HEIGHT/len(turtle_list)
    for turtle in turtle_list:
        turtle.penup()
        turtle.goto(x, y+(i*spacing))
        i+=1

def move(turtle):
    turtle.forward(random.randint(1, 10))
    if turtle.pos()[0] >= WIDTH / 2:
        print(f"{turtle.color()[0]} won!")
        return turtle
    return False

r_turt = Turtle(shape="turtle")
r_turt.color("red")
o_turt = Turtle(shape="turtle")
o_turt.color("orange")
y_turt = Turtle(shape="turtle")
y_turt.color("yellow")
g_turt = Turtle(shape="turtle")
g_turt.color("green")
b_turt = Turtle(shape="turtle")
b_turt.color("blue")
i_turt = Turtle(shape="turtle")
i_turt.color("indigo")
v_turt = Turtle(shape="turtle")
v_turt.color("violet")
my_turtles = [r_turt, o_turt, y_turt, g_turt, b_turt, i_turt, v_turt]

screen = Screen()
screen.setup(width=WIDTH,height=HEIGHT)

is_race_on = False
get_ready(my_turtles)
user_bet = screen.textinput(title="Make your bet!", prompt="Who do you think will win?")

if user_bet:
    is_race_on = True

while is_race_on:
    winner = move(random.choice(my_turtles))
    if winner:
        is_race_on = False
if winner.color()[0] == user_bet:
    print("You got it RIGHT!!!")
else:
    print("Don't gamble, kids.")
    print(f"{user_bet} != {winner.color()[0]}")



screen.exitonclick()