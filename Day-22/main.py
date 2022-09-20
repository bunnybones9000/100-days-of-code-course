import time
from scoreboard import ScoreBoard
from ball import Ball
from paddle import Paddle
from turtle import Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.listen()
screen.tracer(0)

left = Paddle((-350, 0))
right = Paddle((350, 0))
ball = Ball()

score_board = ScoreBoard()

screen.onkey(left.go_up, "w")
screen.onkey(left.go_down, "s")
screen.onkey(right.go_up, "Up")
screen.onkey(right.go_down, "Down")


is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

# detect collision with the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

# detect collision with the paddles
    if ball.distance(right) < 50 and ball.xcor() > 320 or ball.distance(left) < 50 and ball.xcor() < -320:
        ball.bounce_x()


# check if the right player scores a point
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.r_point()

# check if the left player scores a point
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.l_point()

screen.exitonclick()
