"""
car_manager.py: contains definitions related to the CarManager class.
"""
from turtle import Turtle
import random

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.cars = []
        self.move_pace = STARTING_MOVE_DISTANCE

    def generate_car(self):
        """Generate a new car and add to traffic
        1 out of 6 chances of creating a new car when
        called.
        """
        random_chance = random.randint(1, 6)
        if random_chance == 2:
            x_pos = 300
            y_pos = random.randint(-150, 150)
            car = Turtle('square')
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(stretch_len=2)
            car.goto(x_pos, y_pos)
            self.cars.append(car)

    def animate_cars(self):
        """Make all available cars move across the x-axis
        """
        for car in self.cars:
            car.backward(self.move_pace)
            
    def increase_speed(self):
        """Increase the speed of cars under management.
        """
        self.move_pace += MOVE_INCREMENT
