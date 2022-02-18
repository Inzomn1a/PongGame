from turtle import Screen
from paddle import Paddle
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
time.sleep(0.5)  # short delay after screen init and before game being rendered
paddle = Paddle()


screen.tracer(0)  # allows the use of 'screen.update()' function
# GameLoop
game_is_on = True
while game_is_on:
    screen.update()
    screen.listen()
    screen.onkey(paddle.move_up, "Up")
    screen.onkey(paddle.move_down, "Down")




screen.exitonclick()
