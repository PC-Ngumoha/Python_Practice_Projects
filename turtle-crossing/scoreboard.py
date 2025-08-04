"""
scoreboard.py: contains definitions related to the Scoreboard class.
"""
from turtle import Turtle

# Constants
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self._format()


    def _format(self):
        """Utility fxn: formats level on screen.
        """
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        """Increase player level.
        """
        self.level += 1
        self._format()

    def game_over(self):
        """Displays Game over on the screen.
        """
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
