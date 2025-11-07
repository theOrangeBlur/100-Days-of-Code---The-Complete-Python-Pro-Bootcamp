COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3

from turtle import Turtle
import random

class CarManager(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2, 1)
        self.penup()
        self.setheading(180)
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.end_x = -1*screen_width/2
        self.color(random.choice(COLORS))
        self.start_y = random.randrange(int(-1*self.screen_height/2+50), int(self.screen_height/2), 1)
        self.start_x = random.randrange(int(-1*self.screen_width/2), int(self.screen_width/2), 1)
        self.goto(self.start_x, self.start_y)
    
    def move(self, level):
        self.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT*level)
        if self.pos()[0] <= self.end_x:
            self.refresh()
    
    def refresh(self):
        self.color(random.choice(COLORS))
        self.start_y = random.randrange(int(-1*self.screen_height/2+50), int(self.screen_height/2), 1)
        self.goto(self.screen_width/2, self.start_y)

