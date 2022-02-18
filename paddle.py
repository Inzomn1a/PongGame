from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.shapesize(1, 5)
        self.paddle.setheading(90)
        self.paddle.penup()
        self.paddle.goto(position)

    def move_up(self):
        self.paddle.forward(20)

    def move_down(self):
        self.paddle.backward(20)