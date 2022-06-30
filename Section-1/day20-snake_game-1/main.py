from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Anaconda snake Game")


# todo: 1-Create a snake body.

# # way --------------1
# snake_striker = []
# x_position = [00, -20, -40]
# for _ in range(0, 3):
#     new_turtle = Turtle(shape="square")
#     new_turtle.penup()
#     new_turtle.color("White")
#     new_turtle.goto(y=0, x=x_position[_])
#     snake_striker.append(new_turtle)

# ########### Way-2

# squ_1 = Turtle(shape="square")
# squ_1.color("white")
#
# squ_2 = Turtle(shape="square")
# squ_2.color("white")
# squ_2.goto(x=-20, y=0)
#
# squ_3 = Turtle(shape="square")
# squ_3.color("white")
# squ_3.goto(x=-40, y=0)

# ########## Way-3

starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


is_game_on = True
while is_game_on:
    time.sleep(1)
    screen.update()
    # for seg in segments:
    #     seg.forward(20)
    for seg_num in range(len(segments) -1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(x=new_x, y=new_y)
    segments[0].forward(20)


screen.exitonclick()
