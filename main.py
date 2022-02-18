from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")


right_paddle = Turtle("square")
right_paddle.color("white")
right_paddle.shapesize(1, 5)
right_paddle.setheading(90)
right_paddle.penup()
right_paddle.setposition(350, 0)


def move_up():
    right_paddle.forward(20)


def move_down():
    right_paddle.backward(20)


screen.tracer(0)  # allows the use of 'screen.update()' function
# GameLoop
game_is_on = True
while game_is_on:
    screen.update()
    screen.listen()
    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")




screen.exitonclick()
