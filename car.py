from turtle import Turtle
import random

COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car:

    def __init__(self):
        self.all_car = []

    def create_car(self):
        frequency = random.randint(1, 6)
        if frequency == 1:  # Reduce the number of cars created in each 0.1 seconds
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLOURS))
            random_y = random.randint(-245, 245)
            new_car.goto(295, random_y)
            self.all_car.append(new_car)

    def move_car(self):
        for car in self.all_car:
            car.backward(STARTING_MOVE_DISTANCE)
