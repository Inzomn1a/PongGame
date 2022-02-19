from turtle import Screen
from paddle import Paddle
from ball import Ball
from gamefield import GameField
from scores import Score
import time

# Setup gameScreen
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
grid = GameField()

# Create Paddles and ball. Then wait 1sec. before beginPlay
r_paddle = Paddle((350, 0), "purple")
l_paddle = Paddle((-350, 0), "green")

# Initialise player scores and scoreboard
left_player_score = 0
scoreboard_left = Score("green", (-50, 200))
scoreboard_left.update_scoreboard(left_player_score)
right_player_score = 0
scoreboard_right = Score("purple", (50, 200))
scoreboard_right.update_scoreboard(right_player_score)
time.sleep(0.5)

# Spawn Ball
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

    # check for top or bottom ballCollision
    if ball.ycor() >= 290 or ball.ycor() <= -300:
        ball.ball_bounce_top_bottom()

    # check for ballCollision with paddle
    paddle_bounce = 0
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.ball_bounce_paddle()

    # Right paddle miss
    right_miss_counter = 0
    if ball.xcor() > 350:
        time.sleep(1.5)
        left_player_score += 1
        scoreboard_left.update_scoreboard(left_player_score)
        ball.ball_reset()
        screen.update()
        time.sleep(1)

    # Left paddle miss
    left_miss_counter = 0
    if ball.xcor() < -350:
        time.sleep(1.5)
        right_player_score += 1
        scoreboard_right.update_scoreboard(right_player_score)
        ball.ball_reset()
        screen.update()
        time.sleep(1)

screen.exitonclick()
