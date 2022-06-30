from turtle import Turtle, Screen

WIDTH = 5
LENGTH = 1
PADDLE_COLOR = "white"
PADDLE_SHAPE = "square"


class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.x_position = x_position
        self.y_position = y_position
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        self.penup()
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.setposition(x=self.x_position, y=self.y_position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




