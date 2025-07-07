from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

def main():
    screen = Screen()
    screen.setup(width = 800, height = 600)
    screen.bgcolor('black')
    screen.tracer(0)
    
    player = Paddle()
    bot = Paddle(pos = (350, 0))
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(player.go_up, "w")
    screen.onkey(player.go_down, "s")
    screen.onkey(bot.go_up, "u")
    screen.onkey(bot.go_down, "j")
    while True:
        screen.update()
        time.sleep(0.1)
        ball.move()
        #ball colision
        if 280 < ball.ycor() or ball.ycor() < -280:
            ball.bounce_y()       
        if ball.distance(bot) < 50 and ball.xcor() > 320 or ball.distance(player) < 50 and ball.xcor() < -320:
            ball.bounce_x()
            ball.speed_up()
        
        if ball.xcor() > 400:
            ball.reset_pos()
            scoreboard.player_point()
            ball.reset_speed()
        elif ball.xcor() < -400:
            ball.reset_pos() 
            scoreboard.bot_point()
            ball.reset_speed()
            
    screen.exitonclick()

if __name__ == "__main__":
    main()