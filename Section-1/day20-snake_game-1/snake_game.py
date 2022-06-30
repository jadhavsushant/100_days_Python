from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import  Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Anaconda snake Game")

snake = Snake()
screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)
food = Food()
score = Scoreboard()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with Food.
    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()





screen.exitonclick()