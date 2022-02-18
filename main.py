from turtle import Screen
from paddle import Paddle
from ball import Ball
from grid import Grid
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
#grid = Grid()
time.sleep(1)

r_paddle = Paddle((350, 0), "purple")
l_paddle = Paddle((-350, 0), "green")
time.sleep(1)

ball = Ball()
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
    ball.move_ball()
    print(r_paddle.xcor())#DEBUG
    # check for top or bottom ballCollision
    if ball.ycor() >= 290 or ball.ycor() <= -300:
        print("yCollision")#DEBUG
        ball.ball_bounce_top_bottom()

    # check for ballCollision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        print("bounce")#DEBUG
        ball.ball_bounce_paddle()




screen.exitonclick()
