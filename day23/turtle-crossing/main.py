import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tutel = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(tutel.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    for cars in car.all_cars:
        if cars.distance(tutel) < 20:
            game_is_on = False

    if tutel.is_finish():
        tutel.starting_pos()
        car.more_speed()

screen.exitonclick()
