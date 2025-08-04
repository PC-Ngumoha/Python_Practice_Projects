"""Day 18:
- Turtle Graphics Library
- Python Tuples
- Importing modules.
"""
from turtle import Turtle, Screen
import random

# from module_name import * # Not a good way to import stuff
import heroes

screen = Screen()
# Setting the color mode to permit rgb values from 0 - 255
screen.colormode(255)

tim = Turtle()
tim.shape('turtle')
# tim.color('red')

# # Drawing a Square
# tim.forward(100)
# for _ in range(3):
#     tim.right(90)
#     tim.forward(100)

# print(heroes.gen())

# # Drawing a dashed line
# for _ in range(20):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

# # Draw a triangle, square, pentagon, hexagon, heptagon
# # octagon, nonagon and decagon
# def draw_shape(num_of_sides):
#     deg = 360 / num_of_sides
#     for _ in range(num_of_sides):
#         tim.forward(100)
#         tim.right(deg)
#
# def pick_random_color():
#     # Pick a random line color for each polygon you draw
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     tim.color((r, g, b))
#
# for shape_side_n in range(3, 11):
#     pick_random_color()
#     draw_shape(shape_side_n)


# # Random Walk Simulator
# """
# - change thickness of pen
# - pick a random color
# - choose a random direction
# - move 10 paces
# - repeat
# """
#
# def pick_random_color():
#     # Pick a random line color for each polygon you draw
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     tim.color((r, g, b))
#
# directions = [0, 90, 180, 270] # North, East, South, West
#
# # Change thickness of pen
# # tim.pensize(10)
# # tim.forward(100)
#
# # Pick a random color
# # pick_random_color()
# # tim.forward(100)
#
# # Choose a random direction to move
# # for _ in range(5):
# #     tim.setheading(random.choice(directions))
# #     tim.forward(100)
#
# # Repetively move in random directions while changing color
# tim.pensize(10)
# tim.speed('fastest')
# for _ in range(200):
#     pick_random_color()
#     orientation = random.choice(directions)
#     tim.setheading(orientation)
#     tim.forward(30)


# # Drawing a Spirograph
# """
# - pick a random color
# - draw a circle
# - tilt by 1 degree
# - repeat until full revolution (360 degrees) covered.
# """
#
# # # Draw a circle
# # tim.circle(100)
# # # Tilt by a given degree
# # angle = 0
# # tim.speed("fastest")
# # for _ in range(100):
# #     angle += 1
# #     tim.setheading(angle)
# #     tim.circle(100)
#
# def random_color():
#     # Pick a random line color for each polygon you draw
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
# # angle = tim.heading()
# tim.speed("fastest")
#
# def draw_spirograph(gap_size):
#     for _ in range(int(360 / gap_size)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + gap_size)
#
#
# draw_spirograph(5)


# Close display screen when user clicks on it.
screen.exitonclick()