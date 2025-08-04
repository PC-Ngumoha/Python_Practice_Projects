"""
food.py: Contains class definitions for Food objects
"""
from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.speed('fastest')

        # Move the food to a random position on the screen.
        x_pos = random.randint(-380, 380)
        y_pos = random.randint(-380, 380)
        self.goto(x_pos, y_pos)

    def erase(self):
        self.hideturtle()

class SmallFood(Food):

    def __init__(self):
        super().__init__()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('green')
        self.value = 1

class BigFood(Food):

    def __init__(self):
        super().__init__()
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.color('blue')
        self.value = 5