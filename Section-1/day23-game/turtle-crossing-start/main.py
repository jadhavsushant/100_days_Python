import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(key="Up", fun=player.up)
scoreboard = Scoreboard()
car_manager = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # update score
    if player.ycor() > 290:
        player.refresh()
        scoreboard.update_score()


screen.exitonclick()

