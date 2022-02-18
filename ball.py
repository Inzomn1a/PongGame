from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_move = 2  # Initial ballSpeed
        self.y_move = 2  # Initial ballSpeed

    def increase_ball_speed(self):
        if self.x_move >= 6.75:  # stop difficult increase once it reaches Speed8
            pass
        else:
            self.x_move *= 1.5
            self.y_move *= 1.5

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

