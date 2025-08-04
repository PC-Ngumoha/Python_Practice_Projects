"""
main.py: Game entry-point.
"""
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)  # Turn auto animation OFF

# Create left and right paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Create continuously moving ball
ball = Ball()

# Initialize scoreboard
scoreboard = ScoreBoard()

# Make it listen to screen events
screen.listen()

# Right paddle controls
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

# Left paddle controls
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

# While game is on ?
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Pause
    ball.move()

    # Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320\
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


    screen.update() # Manually update screen.


screen.exitonclick()