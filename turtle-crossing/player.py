"""
player.py: contains definitions related to the Player class
"""
from turtle import Turtle

# Constants
STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_to_start(self):
        """Set to starting position"""
        self.goto(STARTING_POSITION)

    def move(self):
        """Move up on the screen.
        """
        y_pos = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y_pos)

    def at_finish_line(self):
        """Is turtle at finish line ?
        """
        return self.ycor() > FINISH_LINE_Y
