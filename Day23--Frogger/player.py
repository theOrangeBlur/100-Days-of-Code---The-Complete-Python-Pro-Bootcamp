STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.refresh()
        
    
    def refresh(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.pos()[1] <= STARTING_POSITION[1]:
            return
        self.backward(MOVE_DISTANCE)
    
    def goal_check(self):
        if self.pos()[1] >= FINISH_LINE_Y:
            self.refresh()
            return True
        return False
