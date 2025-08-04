from turtle import Turtle, Screen
import random

# tim = Turtle()
# screen = Screen()
#
# def move_forward():
#     tim.forward(100)
#
# screen.listen() # Enable the screen to listen for events
# """Example of a higher-order function which takes another function
# as an argument"""
# screen.onkey(key="space", fun=move_forward)
# screen.exitonclick()
#
# """ Etch-A-Sketch Program
# 'W' = Move Forwards
# 'S' = Move Backwards
# 'A' = Orient Counter-Clockwise
# 'D' = Orient Clockwise
# 'C' = Clear drawing and return sketcher to the middle
# """
#
# sketcher = Turtle()
# screen = Screen()
#
# def move_forwards():
#     """Move the sketcher forwards by 10 paces"""
#     sketcher.forward(10)
#
# def move_backwards():
#     """Move the sketcher backwards by 10 paces"""
#     sketcher.backward(10)
#
# def orient_clockwise():
#     """Orient in the clockwise direction"""
#     sketcher.setheading(sketcher.heading() - 10)
#
# def orient_counterclockwise():
#     """Orient in the counter-clockwise direction"""
#     sketcher.setheading(sketcher.heading() + 10)
#
# def clear_screen():
#     """Clears the screen and returns the sketcher to the middle"""
#     sketcher.clear()
#     sketcher.setheading(0)
#     sketcher.penup()
#     sketcher.home()
#     sketcher.pendown()
#
#
# screen.listen()
# screen.onkeypress(key="w", fun=move_forwards)
# screen.onkeypress(key="s", fun=move_backwards)
# screen.onkeypress(key="a", fun=orient_counterclockwise)
# screen.onkeypress(key="d", fun=orient_clockwise)
# screen.onkey(key="c", fun=clear_screen)
# screen.exitonclick()

"""Turtle Race Project
"""
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet",
                 prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
# tim = Turtle(shape='turtle')
# tim.penup()
# tim.goto(x=-230, y=-100)
turtles = []

for i in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=(-100 + 30 * i))
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False # end race
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_pace = random.randint(0, 10)
        turtle.forward(random_pace)

screen.exitonclick()
