import turtle
import time 
import random
LENGTH = 800
WIDTH = 600

class Score(turtle.Turtle):
    def __init__(self,  xpos, ypos):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.loc = (xpos, ypos)
        self.goto(self.loc)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", False, "center", ('Arial', 20, 'normal'))
    
    def point(self):
        self.score += 1
        self.update_score()

class Paddle(turtle.Turtle):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.turtlesize(5, 1, 1)
        self.goto(xpos, ypos)
    
    def up(self):
        if self.pos()[1] >= WIDTH/2 - 50:
            return
        self.goto(self.pos()[0], self.pos()[1]+20)
    
    def down(self):
        if self.pos()[1] <= -1*WIDTH/2 + 50:
            return
        self.goto(self.pos()[0], self.pos()[1]-20)

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.refresh()
        self.velocity = 15

    def move(self):
        self.forward(self.velocity)
        #reflect off top or bottom
        if self.pos()[1] >= WIDTH/2 or self.pos()[1] <= -1*WIDTH/2:
            self.setheading(360 - self.heading())

    def refresh(self):
        self.penup()
        self.home()
        self.pendown()
        headings = []
        for i in range(150, 210): headings.append(i)
        for i in range(330, 359): headings.append(i)
        for i in range(0, 30): headings.append(i)
        self.setheading(random.choice(headings))
        self.velocity = 15


def setup_boundary():
    boundary_line = turtle.Turtle()
    boundary_line.hideturtle()
    boundary_line.speed("fastest")
    boundary_line.color("yellow")
    boundary_line.penup()
    boundary_line.goto(-LENGTH/2, -WIDTH/2)
    boundary_line.pendown()
    boundary_line.goto(-LENGTH/2, WIDTH/2)
    boundary_line.goto(LENGTH/2, WIDTH/2)
    boundary_line.goto(LENGTH/2, -WIDTH/2)
    boundary_line.goto(-LENGTH/2, -WIDTH/2)

def dashes():
    dashed_line = turtle.Turtle(shape="turtle")
    dashed_line.hideturtle()
    dashed_line.speed("fastest")
    dashed_line.color("white")
    dashed_line.width(3)
    dashed_line.penup()
    dashed_line.setpos(0, WIDTH/2)
    dashed_line.setheading(270)
    for i in range( int(WIDTH/2), int(-1* WIDTH/2), -20):
        dashed_line.pendown()
        dashed_line.forward(10)
        dashed_line.penup()
        dashed_line.forward(10)
    dashed_line.hideturtle()

def move_paddle(paddle, up_bool):
    if paddle.pos()[1] >= WIDTH/2-60:
        up_bool = False
    elif paddle.pos()[1] <= -1*WIDTH/2+60:
        up_bool = True

    if up_bool:
        paddle.up()
        return True
    else:
        paddle.down()
        return False

screen = turtle.Screen()
screen.screensize(LENGTH, WIDTH, "black")
screen.title("PONG")
screen.tracer(0)

setup_boundary()
dashes()

#setup scoreboards
score_left = Score(int(-1*LENGTH/4), WIDTH/2-40)
score_right = Score(int(LENGTH/4), WIDTH/2-40)

#setup paddles
left_paddle = Paddle(-1*LENGTH/2+40, 0)
right_paddle = Paddle(LENGTH/2-40, 0)
up_bool = True

#setup ball
ball = Ball()

game_is_on = True
screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

while game_is_on:
    screen.update()
    ball.move()
    #check to bounce off paddles
    if ball.pos()[0] < left_paddle.pos()[0] or ball.pos()[0] > right_paddle.pos()[0]:
        if ball.distance(left_paddle) <= 50 or ball.distance(right_paddle) <= 50:
            if ball.heading() <= 180:
                ball.setheading(180 - ball.heading())
            else:
                ball.setheading(540 - ball.heading())
            ball.velocity += 5
    #check for goal
    if ball.pos()[0] > LENGTH/2:
        score_left.point()
        left_paddle.goto(-1*LENGTH/2+40, 0)
        right_paddle.goto(LENGTH/2-40, 0)
        ball.refresh()
    if ball.pos()[0] < -1*LENGTH/2:
        score_right.point()
        left_paddle.goto(-1*LENGTH/2+40, 0)
        right_paddle.goto(LENGTH/2-40, 0)
        ball.refresh()
    time.sleep(.05)

    if score_left.score >= 7 or score_right.score >= 7:
        game_is_on = False




screen.exitonclick()