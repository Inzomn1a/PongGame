from turtle import Turtle


class Ball:
    def __init__(self):
        self.ball = Turtle("square")
        self.ball.color("white")
        self.ball.penup()
        self.x_move = 0.5  # Higher value increases ball speed
        self.y_move = 0.5  # Higher value increases ball speed

    def move_ball(self):
        ball_xcor = self.ball.xcor() + self.x_move
        ball_ycor = self.ball.ycor() + self.y_move
        self.ball.setposition(ball_xcor, ball_ycor)
        return self.ball.ycor()

    def ball_bounce_top_bottom(self):
        self.y_move *= -1

