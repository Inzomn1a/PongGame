from turtle import Turtle
import time


class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(1, 5)
        self.setheading(90)
        self.penup()
        self.goto(position)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)