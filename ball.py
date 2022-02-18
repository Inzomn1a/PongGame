from turtle import Turtle


class Ball:
    def __init__(self):
        self.ball = Turtle("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball_speed_x = 1
        self.ball_speed_y = 1

    def move_ball(self):
        ball_xcor = self.ball.xcor() + self.ball_speed_x
        ball_ycor = self.ball.ycor() + self.ball_speed_y
        self.ball.setposition(ball_xcor, ball_ycor)
        return self.ball.ycor()

    def ball_bounce_top_bottom(self):
        self.ball_speed_y *= -1

