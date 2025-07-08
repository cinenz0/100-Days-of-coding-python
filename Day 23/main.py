import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

cars = []
level = 0

game_is_on = True


screen.listen()
screen.onkey(player.walk,'w')

while game_is_on:
    screen.update()
    time.sleep(0.1)

    if random.randint(1,6) == 1:
        car = CarManager()
        car.level = level
        cars.append(car)

    for car in cars:
        car.auto_move()
        if player.distance (car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.check_level():
        level += 1 
        scoreboard.level += 1
        scoreboard.update_score()
        for car in cars:
            car.level += 1
            car.increment_speed()
screen.exitonclick()
  