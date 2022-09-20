from turtle import Turtle, Screen
import turtle
import random
turtle.colormode(255)

color_list = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="place your bet", prompt="which turtle will win")

all_turtle = []
if user_input:
    is_on = True

y = -40
for turtle_index in range(0, 6):

    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.goto(-240, y)
    new_turtle.color(color_list[turtle_index])
    y += 20
    all_turtle.append(new_turtle)

while is_on:
    for i in all_turtle:
        if i.xcor() > 230:
            winning_color = i.pencolor()
            if user_input == winning_color:
                print(f"you won thw winner was {winning_color}")
                is_on = False
            else:
                print(f"you lost the winner was {winning_color}")
                is_on = False

        random_num = random.randint(0, 10)
        i.forward(random_num)




























screen.exitonclick()
