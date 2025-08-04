"""
turtle crossing game
"""
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # Turn off tracer


# TODO-1: Create a player that moves up when UP key pressed.
# Should reverse back to starting point when finish line crossed.
turtle = Player()

# TODO-2: Generate car
fleet = CarManager()

# TODO-5: Keeping track of score
scoreboard = Scoreboard()

# Event Listeners
screen.listen()
screen.onkeypress(turtle.move, "Up")

game_is_on = True
loop_count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update() # Refresh screen

    fleet.generate_car()
    fleet.animate_cars()

    # TODO-3: Detect collision with a car
    for car in fleet.cars:
        if car.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on = False

    # TODO-4: Detect if turtle at finish line
    if turtle.at_finish_line():
        turtle.go_to_start()
        scoreboard.level_up()
        fleet.increase_speed()

    loop_count += 1

screen.exitonclick()
