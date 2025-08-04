"""
paddle.py: contains Paddle class definition.
"""
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(pos)

    def move_up(self):
        """Move the paddle upward (North).
        """
        y_pos = self.ycor() + 20
        self.goto(self.xcor(), y_pos)

    def move_down(self):
        """Move the paddle downward (South).
        """
        y_pos = self.ycor() - 20
        self.goto(self.xcor(), y_pos)
