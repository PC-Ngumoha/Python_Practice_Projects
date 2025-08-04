"""Hirst Painting"""

# TODO-1: Extract colors using colorgram
import colorgram
import turtle as t
import random as r

# colors = []

# # Extracting all colors in the Hirst painting
# for color in colorgram.extract('hirst.jpeg', 2000):
#     r, g, b = color.rgb
#     colors.append((r, g, b))
#
# print(colors)
# print(len(colors))

# Extracted Colors:
color_list = [(245, 239, 228), (236, 240, 247), (248, 238, 244), (235, 246, 241), (196, 158, 124), (64, 95, 125), (142, 87, 62), (139, 162, 184), (216, 209, 128), (184, 147, 159), (23, 36, 54), (122, 78, 93), (138, 179, 153), (46, 23, 16), (68, 114, 84), (54, 23, 34), (130, 25, 39), (20, 38, 29), (169, 156, 50), (188, 98, 85), (220, 174, 188), (125, 34, 25), (173, 99, 116), (226, 176, 168), (46, 59, 96), (163, 209, 179), (79, 156, 109), (113, 122, 157), (180, 187, 214), (31, 86, 62), (15, 84, 100), (69, 76, 35), (84, 145, 162), (168, 199, 208), (209, 211, 26)]

painter = t.Turtle()

screen = t.Screen()
screen.colormode(255)

"""
- Creating a 10x10 grid painting
- Each dot should be of size 20 and spaced about by 50 paces
- reset position on x and go up on y
"""
# set initial starting position
painter.setheading(225)
painter.penup()
painter.hideturtle()
painter.speed('fastest')
painter.forward(300)
painter.setheading(0)

x_coord = painter.xcor()
y_coord = painter.ycor()

dot_gap = 50
dot_size = 20
for i in range(10):
    painter.setposition(x_coord, y_coord + float(dot_gap * i))
    for _ in range(10):
        painter.pendown()
        painter.dot(dot_size, r.choice(color_list))
        painter.penup()
        painter.forward(dot_gap)

# Exit only when clicked on.
screen.exitonclick()