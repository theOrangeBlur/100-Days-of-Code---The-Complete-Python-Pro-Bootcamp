from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ('Arial', 8, 'bold')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.present()


    def point(self):
        self.score += 1
        self.present()

    def present(self):
        self.clear()
        self.write(f"Score = {self.score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        for i in range(50):
            self.clear()
            self.color("blue")
            self.write(f"GAME OVER. FINAL SCORE: {self.score}", False, ALIGNMENT, FONT)
            time.sleep(.5)
            self.clear()
            self.color("yellow")
            self.write(f"GAME OVER. FINAL SCORE: {self.score}", False, ALIGNMENT, FONT)
            time.sleep(.5)