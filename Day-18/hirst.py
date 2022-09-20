import turtle
from turtle import Turtle,Screen
import random
turtle.colormode(255)
color_list = [(231, 176, 57), (41, 123, 156), (150, 20, 58)]
tim = Turtle()
tim.width(10)
l = 0
tim.hideturtle()
for i in range(10):
    tim.setheading(0)
    tim.penup()
    tim.goto(0, l)
    for i in range(10):
        color = random.choice(color_list)
        tim.color(color)
        tim.dot()
        tim.forward(50)
        l += 5


































screen  = Screen()
screen.exitonclick()

