from turtle import Turtle

import math

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5,stretch_len=3)
        self.color("white")
        self.penup()
        self.seth(270)
        self.speed("slowest")



    def make_dashed_line(self):
        self.hideturtle()
        self.pensize(5)
        self.goto(0, 200)
        for i in range(1, int(400/(2*15)) + 1):
            self.forward(15)
            self.pendown()
            self.forward(15)
            self.penup()

    def move_up(self):
       self.backward(10)

    def move_down(self):
        self.forward(10)



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("slowest")



    def bounce(self,last_angle):
        new_angle = 360 - last_angle
        return new_angle

    def paddle_bounce(self,last_angle):
        new_angle = 540 - last_angle
        return new_angle

    def move_ball(self,angle):
        new_x = (math.cos(math.radians(angle)) * 10) + self.xcor()
        new_y = (math.sin(math.radians(angle)) * 10) + self.ycor()
        self.goto(x = new_x,y = new_y)

