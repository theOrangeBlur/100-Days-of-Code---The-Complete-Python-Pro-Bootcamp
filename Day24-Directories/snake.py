from turtle import Turtle
import random

STARTING_LENGTH = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.color_progress = 0

    def create_snake(self):
        for i in range(STARTING_LENGTH):
            timmy = Turtle(shape="square")
            timmy.color("white")
            timmy.penup()
            timmy.setpos(x=i * -20, y=0)
            self.segments.append(timmy)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].setpos(self.segments[i - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == DOWN:
            return
        self.head.setheading(UP)
        #print("^^")

    def right(self):
        if self.head.heading() == LEFT:
            return
        self.head.setheading(RIGHT)
        #print(">>")

    def down(self):
        if self.head.heading() == UP:
            return
        self.head.setheading(DOWN)
        #print("vv")

    def left(self):
        if self.head.heading() == RIGHT:
            return
        self.head.setheading(LEFT)
        #print("<<")

    def eat(self):
        timmy = Turtle(shape="square")
        timmy.color(random.random(), random.random(), random.random())
        timmy.penup()
        last_pos = self.segments[-1].pos()
        last_heading = self.segments[-1].heading()
        if last_heading == 0:
            timmy.setpos(last_pos[0]-20, last_pos[1])
        if last_heading == 90:
            timmy.setpos(last_pos[0], last_pos[1]-20)
        if last_heading == 180:
            timmy.setpos(last_pos[0]+20, last_pos[1])
        if last_heading == 270:
            timmy.setpos(last_pos[0], last_pos[1]+20)
        self.segments.append(timmy)

    def boundary_check(self, screen_width, screen_height):
        if abs(self.head.pos()[0]) >= screen_width/2:
            return 1
        elif abs(self.head.pos()[1]) >= screen_height/2:
            return 1
        return 0

    def intersect_check(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return 1
        return 0
    
    def reset(self):
        for body in self.segments:
            body.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.color_progress = 0
