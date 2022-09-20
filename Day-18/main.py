import turtle
from turtle import Turtle,Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")

"""for i in range(4):
    timmy.forward(100)
    timmy.right(90)
"""

"""for i in range(15):
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()
"""

"""n = 3
for i in range(7):
    for i in range(n):
         angle = 360/n
         timmy.forward(100)
         timmy.right(angle)
    n += 1
"""
import random
turtle.colormode(255)
timmy.width(0)
timmy.speed(15)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return timmy.color(colour)
"""
for i in range(1000):
    choice = random.randint(1, 4)
    if choice == 1:
        random_color()
        timmy.forward(20)
    elif choice == 2:
        random_color()
        timmy.back(20)

    elif choice == 3:
        random_color()
        timmy.right(90)
        choice2 = random.randint(1,2)
        if choice2 == 1 :
            timmy.forward(20)
        elif choice2 == 2:
            timmy.back(20)

    elif choice == 4 :
        random_color()
        timmy.left(90)
        choice2 = random.randint(1, 2)
        if choice2 == 1:
            timmy.forward(20)
        elif choice2 == 2:
            timmy.back(20) """





def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        current = timmy.heading()
        timmy.circle(100)
        timmy.setheading(current + size_of_gap)
        current += size_of_gap
        random_color()


draw_spirograph(5)

screen = Screen()
screen.exitonclick()