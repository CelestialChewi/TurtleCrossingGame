import time
from turtle import Screen, Turtle
from player import Player
from car import Car
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = Car()

screen.listen()
screen.onkey(player.move_up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    # Detect collision with cars
    for car in car.all_car:
        if car.distance(player) < 20:
            game_on = False