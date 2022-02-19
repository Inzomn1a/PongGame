from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_move = 3  # Initial ballSpeed
        self.y_move = 3  # Initial ballSpeed

    def move_ball(self):
        ball_xcor = self.xcor() + self.x_move
        ball_ycor = self.ycor() + self.y_move
        self.setposition(ball_xcor, ball_ycor)
        if self.xcor() > 0:   # if ball is on LEFT screen
            self.color("purple")
        if self.xcor() < 0:  # if ball is on RIGHT screen
            self.color("green")

    def ball_bounce_top_bottom(self):
        self.y_move *= -1

    def ball_bounce_paddle(self):
        self.x_move *= -1

    def ball_reset(self):
        self.setposition(0, 0)
        self.x_move *= -1
