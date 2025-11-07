import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600

def screen_boundary():
    boundary = Turtle()
    boundary.hideturtle()
    boundary.speed("fastest")
    boundary.color("yellow")
    boundary.penup()
    boundary.goto(WIDTH/2, HEIGHT/2)
    boundary.pendown()
    boundary.goto(WIDTH/2, -1*HEIGHT/2)
    boundary.goto(-1*WIDTH/2, -1*HEIGHT/2)
    boundary.goto(-1*WIDTH/2, HEIGHT/2)
    boundary.goto(WIDTH/2, HEIGHT/2)

def add_cars(num):
    for i in range(num):
        my_car = CarManager(WIDTH, HEIGHT)
        car_list.append(my_car)

screen = Screen()
screen.bgcolor("black")
screen_boundary()
screen.tracer(0)

#set up screen boundary
screen.setup(width=WIDTH, height=HEIGHT)
screen.update()

#set up user input
my_player = Player()
screen.listen()
screen.onkey(my_player.move_up, "Up")
screen.onkey(my_player.move_down, "Down")

#set up cars
car_list = []
add_cars(15)

#set up score
my_scoreboard = Scoreboard(WIDTH, HEIGHT)


game_is_on = True
level = 0
while game_is_on:
    if my_player.goal_check():
        level += 1
        my_scoreboard.update_score(level+1)
        add_cars(5)
    for car in car_list:
        car.move(level)
    time.sleep(0.1)
    screen.update()
    for car in car_list:
        if car.pos()[0]+25 >= my_player.pos()[0] >= car.pos()[0]-25:
            if car.pos()[1]+15 >= my_player.pos()[1] >= car.pos()[1]-15:
                game_is_on = False
