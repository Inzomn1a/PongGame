from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
time.sleep(0.1)  # short delay after screen init and before game being rendered

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
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




screen.exitonclick()
