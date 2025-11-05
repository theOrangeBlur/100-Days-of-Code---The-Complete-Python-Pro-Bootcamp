from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

WIDTH = 600
HEIGHT = 600
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

segments = []
my_snake = Snake()
my_food = Food()
my_score = Score()
screen.update()

game_is_on = True
screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.right, "Right")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")

while game_is_on:
    screen.update()
    time.sleep(.05)
    my_snake.move()
    if my_snake.head.distance(my_food) < 10:
        my_snake.eat()
        my_food.refresh()
        my_score.point()
    if my_snake.boundary_check(WIDTH, HEIGHT):
        game_is_on = False
    if my_snake.intersect_check():
        game_is_on = False

screen.tracer(1)
my_score.game_over()


screen.exitonclick()