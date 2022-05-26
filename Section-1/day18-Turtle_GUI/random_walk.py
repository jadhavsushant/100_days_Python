# import modules with class name
import random
from turtle import Turtle, Screen

""" 
# various ways to import module-
*** Basic Import
    <Keyword> <Module_name>
    import turtle
    -------  Create object 
    asd = turtle.Turtle()

 *** from Import   
    <Keyword> <Module_name> <Keyword> <ClassName>
    from turtle import Turtle
     -------  Create object 
    asd = Turtle()

 *** import everything
     from turtle import *

  *** Aliasing Modules
     <Keyword> <Module_name> <Keyword> <aliasName>
     import module as t
"""

import turtle as t

asd = t.Turtle()
t.colormode(255)
asd.shape("turtle")
asd.color("DeepSkyBlue")


def random_color():
    """returns the random color in rgb format"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


# colors = ["DarkBlue", "DarkGreen", "DarkRed", "DeepSkyBlue", "OrangeRed", "Purple"]
direction = [0, 90, 180, 270]

for _ in range(200):
    asd.pensize(5)
    asd.pencolor(random_color())
    # asd.color(random.choice(colors))
    asd.forward(30)
    asd.speed(10)
    asd.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()
