"""
ball.py: contains Ball class definitions
"""
from turtle import Turtle
import math


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.goto(0, 0)
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Continuous motion
        """
        # Top-right motion (For NOW)
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)

    def bounce_y(self):
        """Simulates a ball bouncing
        i.e Reverse direction along y-axis
        """
        self.y_move *= -1

    def bounce_x(self):
        """Simulates a ball bouncing
        i.e Reverse direction along x-axis
        """
        self.x_move *= -1
        self.move_speed *= 0.7

    def reset_position(self):
        """Simulates ball reversal"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
