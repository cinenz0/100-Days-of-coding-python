from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('My snake game')

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game = True

while game:

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        snake.add_segment()
        scoreboard.change_score()

    if snake.head.xcor() > 280 or snake.head.ycor() > 290 or snake.head.xcor() < -280 or snake.head.ycor() < -290:
        game = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
       
        if snake.head.distance(segment) < 10:
            game = False
            scoreboard.game_over()
screen.exitonclick()