import turtle as t
import random

asd = t.Turtle()
t.colormode(255)
asd.shape("turtle")
asd.color("DeepSkyBlue")
asd.speed("fastest")


def random_color():
    """returns the random color in rgb format"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        asd.color(random_color())
        asd.circle(100)
        current_head = asd.heading()
        asd.setheading(current_head + size_of_gap)


draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()