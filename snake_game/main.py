from turtle import Screen
from snake import Snake
from food import SmallFood, BigFood
from scoreboard import ScoreBoard
import time
import random

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0) # Turns off the automatic updating of the screen

def random_food():
    return random.choice([SmallFood, BigFood])

# create snake
snake = Snake()
food = (random_food())()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update() # Manually update screen
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        scoreboard.increment(food.value)
        snake.extend(food.value) # Grow by varied amounts based on type of food
        # Create new instance of food.
        food.erase()
        food = (random_food())()


    # Detect collision with wall.
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or\
        snake.head.ycor() > 380 or snake.head.ycor() < -380:
        scoreboard.reset()
        snake.reset()
        # game_is_on = False

    # Detect collisions with your own tail
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            # game_is_on = False

screen.exitonclick()