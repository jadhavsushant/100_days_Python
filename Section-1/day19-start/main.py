from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backward():
    tim.back(10)


def reset_screen():
    tim.screen.reset()


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=reset_screen)
screen.exitonclick()
