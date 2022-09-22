import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

cars = CarManager()
player = Player()
score_board = Scoreboard()

screen.onkey(player.go_up,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()

    # Detect collision with cars
    for car in cars.all_cars:
        if car.distance(player) < 20:
            score_board.game_over()
            game_is_on = False

    # Detect a successful crossing
    if player.successful_crossing():
        player.go_to_start()
        cars.level_up()
        score_board.increase_level()


screen.exitonclick()