FONT = ("Courier", 24, "bold")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-1*screen_width/2+30, screen_height/2-50)
        self.score = 1
        self.update_score(self.score)

    def update_score(self, level):
        self.clear()
        self.score = level
        self.write(f"{self.score}", False, "center", FONT)

