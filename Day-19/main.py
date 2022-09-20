from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def turn_left():
    tim.left(20)


def turn_right():
    tim.right(20)

def clear():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="c", fun=clear)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_left)
screen.onkey(key="a", fun=turn_right)
screen.exitonclick()