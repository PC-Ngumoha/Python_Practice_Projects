"""
scoreboard.py: contains class definition for the Scoreboard
"""
from os import write
from turtle import Turtle

# Constants
ALIGNMENT = 'center'
FONT = ('Comic Sans MS', 18, 'bold')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # Make use of previous high score
        with open('data.txt', mode='r') as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.setposition(0, 360)
        self.hideturtle()
        self._print_score()

    def _print_score(self):
        """Handles displaying the score on the scoreboard."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   False, align=ALIGNMENT, font=FONT)

    def increment(self, value):
        """Increment the score displayed on the screen"""
        self.score += value
        self._print_score()

    # def game_over(self):
    #     """Writes Game over to screen"""
    #     self.setposition(0,0)
    #     self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        """Reset high score."""
        if self.score > self.high_score:
            self.high_score = self.score
            # Save the new high score
            with open('data.txt', mode='w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self._print_score()
