from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car_frequency = random.randint(1, 6)
        if car_frequency == 1: 
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid= 1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y_pos = random.randint(-250, 250)
            new_car.goto(300, random_y_pos)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def more_speed(self):
        self.speed += MOVE_INCREMENT
