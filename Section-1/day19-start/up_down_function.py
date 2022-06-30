from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def up():
    tim.setheading(90)

def down():
    tim.setheading(270)

def left():
    tim.setheading(180)

def right():
    tim.setheading(0)

screen.listen()
screen.onkey(key="Up", fun=up)
screen.onkey(key="Left", fun=left)
screen.onkey(key="Right", fun=right)
screen.onkey(key="Down", fun=down)
screen.exitonclick()