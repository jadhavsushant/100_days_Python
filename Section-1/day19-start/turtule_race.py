import time
import turtle
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
turtle.speed("slowest")
# user_bet
color_list = ["red", "green", "purple", "yellow", "Orange", "black"]
y_position = [-70, -40, -10, 20, 50, 80]

for t_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(color_list[t_index])
    tim.penup()
    tim.goto(x=-230, y=y_position[t_index])


screen.exitonclick()
