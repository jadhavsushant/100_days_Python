from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_axis = random.randint(-280, 280)
        y_axis = random.randint(-280, 280)
        self.goto(x=x_axis, y=y_axis)

