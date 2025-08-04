
"""
snake.py: Contains class definitions for Snake objects
"""
from turtle import Turtle

# Reusable constants
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    """Snake class"""

    def __init__(self):
        self.body = []
        self._create_snake()
        self.head = self.body[0]

    def _create_snake(self):
        for position in STARTING_POSITIONS:
            self._add_segment(position)

    def _add_segment(self, pos):
        """Add segment to snake body"""
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        # Arrange each segment back-to-back on the screen
        segment.goto(pos)
        self.body.append(segment)

    def reset(self):
        """Recreate snake"""
        for seg in self.body:
            seg.goto(1000, 1000) # Disappear from visible screen

        self.body.clear()
        self._create_snake()
        self.head = self.body[0]

    def extend(self, num_segments=1):
        """Extends the length of the snake"""
        for times in range(num_segments):
            self._add_segment(self.body[-1].position())

    def move(self):
        """Causes the snake segments to move as a unit"""
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Causes snake to face north """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)  # 90°

    def down(self):
        """Causes snake to face south """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)  # 270°

    def left(self):
        """Causes snake to face west"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)  # 180°

    def right(self):
        """Causes snake to face east"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)  # 0°
