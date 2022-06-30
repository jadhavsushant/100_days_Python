import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# construct the main screen of the game
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Welcome to Pong Game !!")
screen.tracer(0)

# create a paddles
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
# defined the ball
ball = Ball()
scoreboard = Scoreboard()

# moves the paddles
screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # detect collision with paddle
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() - 320:
        ball.bounce_x()

    # detect collision with missed paddle - right paddle
    if ball.xcor() > 380:
        scoreboard.clear()
        scoreboard.r_score()
        ball.reset_postion()

    # detect collision with missed paddle - left paddle
    if ball.xcor() < -380:
        scoreboard.clear()
        scoreboard.l_score()
        ball.reset_postion()




screen.exitonclick()
