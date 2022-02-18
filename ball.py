from turtle import Turtle


class Ball:
    def __init__(self):
        self.ball = Turtle("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.setheading(40)  # initial moveDirection(degrees) of ball on beginPlay

    def move_ball(self):
        self.ball.forward(5)  # Speed of ball
