# import colorgram
#
# # Extract colors from an image.
# color_object = colorgram.extract('dots.jpg', 30)
#
# # print(color_object[0])
# print(len(color_object))
#
# # empty list
# colors_tuple = []
#
# # loops to add the color tuple and tuples added to list
# for c in color_object:
#     # print(c.rgb)
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     rgb_colors = (r, g, b)
#     colors_tuple.append(rgb_colors)

# print(colors_tuple)
import turtle

color_list = [(254, 253, 252), (232, 254, 243), (253, 234, 245), (43, 2, 176), (79, 253, 174), (226, 149, 109), (230, 225, 253), (160, 3, 82), (4, 211, 101), (3, 138, 64), (246, 42, 127), (109, 108, 247), (252, 253, 53), (184, 184, 251), (211, 106, 5), (35, 35, 252), (177, 112, 248), (139, 1, 0), (252, 36, 35), (50, 240, 56), (216, 114, 171), (16, 127, 144), (85, 248, 252), (188, 39, 109), (23, 5, 107), (8, 209, 215), (99, 8, 50), (231, 163, 205), (204, 119, 35), (112, 6, 4)]

import turtle as turtle_module
import random
asd=turtle_module.Turtle()
asd_screen = turtle_module.Screen()
turtle_module.colormode(255)

"""
screen = 10x10
dots = 20
space = 50
"""
asd.speed("fastest")
asd.hideturtle()
asd.setheading(225)
asd.penup()
asd.forward(350)
asd.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    asd.dot(20, random.choice(color_list))
    asd.forward(50)

    if dot_count % 10 == 0:
        asd.setheading(90)
        asd.forward(50)
        asd.setheading(180)
        asd.forward(500)
        asd.setheading(0)










asd_screen.exitonclick()