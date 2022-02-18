from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_move = 1  # Higher value increae ball speed (steps of 0.25)
        self.y_move = 1  # Higher value increae ball speed (steps of 0.25)

    def move_ball(self):
        ball_xcor = self.xcor() + self.x_move
        ball_ycor = self.ycor() + self.y_move
        self.setposition(ball_xcor, ball_ycor)
        #return self.ycor()

    def ball_bounce_top_bottom(self):
        self.y_move *= -1

    def ball_bounce_paddle(self):
        self.x_move *= -1

