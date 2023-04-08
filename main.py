import time
from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
vehicle = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    vehicle.create_car()
    vehicle.move_car()

    # Detect collision with cars
    for car in vehicle.all_cars:
        if car.distance(player) < 24:
            game_on = False
            scoreboard.screen_game_over()

    # Detect when turtle reaches the other side
    if player.at_finish_line():
        player.start_again()
        vehicle.level_up()
        scoreboard.level_up_scoreboard()




screen.exitonclick()