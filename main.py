from turtle import Screen
from paddle import Paddle
from ball import Ball
from grid import Grid
import time

# Setup gameScreen
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
grid = Grid()

# Create Paddles and ball. Then wait 1sec. before beginPlay
r_paddle = Paddle((350, 0), "purple")
l_paddle = Paddle((-350, 0), "green")
ball = Ball()
time.sleep(1)

# GameLoop
screen.tracer(0)  # allows the use of 'screen.update()' function
game_is_on = True
while game_is_on:
    screen.update()
    screen.listen()
    # Player Input Controls to move paddles
    screen.onkey(r_paddle.move_up, "Up")
    screen.onkey(r_paddle.move_down, "Down")
    screen.onkey(l_paddle.move_up, "w")
    screen.onkey(l_paddle.move_down, "s")
    ball.move_ball()  # forward movement of ball
    print(r_paddle.ycor())#DEBUG
    # check for top or bottom ballCollision
    if ball.ycor() >= 290 or ball.ycor() <= -300:
        ball.ball_bounce_top_bottom()

    # check for ballCollision with paddle
    paddle_bounce = 0
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        paddle_bounce += 1
        if paddle_bounce % 5 == 0:  # increase ballSpeed every 5 bounces (min2 - max6.75)
            ball.increase_ball_speed()
        ball.ball_bounce_paddle()





screen.exitonclick()
